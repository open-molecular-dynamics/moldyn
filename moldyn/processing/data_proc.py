import os

import numpy as np
import numexpr as ne
from matplotlib.tri import TriAnalyzer, Triangulation, UniformTriRefiner
from scipy.spatial import Voronoi, ConvexHull
import moderngl

from moldyn.simulation.builder import Model
from moldyn.utils import gl_util


def PDF(pos, nb_samples, rcut, bin_count):
    """
    Pair Distribution Function. Returns normalized histogram of distance between atoms.

    Parameters
    ----------
    pos : np.array
        Array containing atoms position
    nb_samples : int
        Number of atoms from which to generate the histogram
    rcut : number
        Maximum distance to consider
    bin_count : int
        Number of bins of the histogram

    Returns
    -------
    bins, hist : tuple(np.array, np.array)
        `bins` being the distances, `hist` the normalized (regarding radius) histogram

    """
    bins = np.linspace(0, rcut, bin_count)
    samples = np.random.choice(range(len(pos)), nb_samples)
    hist = np.zeros(len(bins)-1)
    for s in samples:
        sample = pos[s,:]
        dists = np.array([a for a in np.sqrt(ne.evaluate("sum((pos-sample)**2,axis=1)")) if a])
        hist += np.histogram(dists, bins=bins, weights=1/dists)[0]
    return bins[:-1], hist/nb_samples


def density(model, refinement=0):
    """
    Create a Voronoi mesh and calculate the local particle density on its vertices.

    The local density is calculated as follows:
    for each vertex, compute the density of each neighbour region as
    one over the area and assign the average of
    the neighbouring density to the vertex.

    Parameters
    ----------
    model : simulation.builder.Model
        the Model object containing
    refinement : int (defaults : 0)
        number of subdivision for refining the mesh (0 == None)
    Returns
    -------
    tri : matplotlib.tri.Triangulation
        the triangulation mesh (refined if set as)
    vert_density : numpy.array
        the array containing the local denstity associated with the tri mesh

    Examples
    -----
    To plot the result using matplotlib use :
    .. code-block:: python
        import matplotlib.pyplot as plt
        tri, density = data_proc.density(model)
        plt.tricontour(tri, density) # to draw contours
        plt.tricontourf(tri, density) # ot draw filled contours
        plt.show()

    Note
    ----
    As of now, the numerical results may not be quantitatively accurate
    but should qualitatively represent the density.
    """
    vor = Voronoi(model.pos)
    vert_density = np.zeros(max(vor.vertices.shape)) # density vector
    reg_num = np.zeros(max(vor.vertices.shape)) # nbr of regions per vertex --> averaging
    for point_index, reg in enumerate(vor.point_region):
        vertices = vor.regions[reg]
        if vertices:
            if -1 not in vertices:
                area = ConvexHull(vor.vertices[vertices]).area # gets the area
                vert_density[vertices] += 1 / area # makes it a density (sort-of)
                reg_num[vertices] += 1
    vert_density /= reg_num # averaging

    # getting rid of really ugly border points
    new_vert, vert_density = (vor.vertices[vor.vertices[:, 0] >= np.min(model.pos[:, 0])],
                              vert_density[vor.vertices[:, 0] >= np.min(model.pos[:, 0])])

    new_vert, vert_density = (new_vert[new_vert[:, 0] <= np.max(model.pos[:, 0])],
                              vert_density[new_vert[:, 0] <= np.max(model.pos[:, 0])])

    new_vert, vert_density = (new_vert[new_vert[:, 1] >= np.min(model.pos[:, 1])],
                              vert_density[new_vert[:, 1] >= np.min(model.pos[:, 1])])

    new_vert, vert_density = (new_vert[new_vert[:, 1] <= np.max(model.pos[:, 1])],
                              vert_density[new_vert[:, 1] <= np.max(model.pos[:, 1])])

    # for triangulation refinement
    tri2 = Triangulation(*new_vert.T)
    if refinement:
        tri2.set_mask(TriAnalyzer(tri2).get_flat_tri_mask(0.1))
        refiner = UniformTriRefiner(tri2)
        print(len(tri2.neighbors), vert_density.shape)
        tri, vert_density = refiner.refine_field(vert_density, subdiv=refinement)
    else:
        tri, vert_density = tri2, vert_density

    return tri, vert_density


class StrainComputeGPU:

    def __init__(self, consts, compute_npart=None):
        """

        Parameters
        ----------
        consts : dict
            Dictionary containing constants used for calculations.

        """

        self.npart = consts["NPART"]
        self.compute_npart = compute_npart or consts["NPART"]

        max_layout_size = 256  # Probablement optimal (en tout cas d'après essais et guides de bonnes pratiques)
        self.groups_number = int(np.ceil(self.compute_npart / max_layout_size))
        self.layout_size = int(np.ceil(self.compute_npart / self.groups_number))

        consts["LAYOUT_SIZE"] = self.layout_size

        self.compute_npart = min(self.compute_npart, self.npart)
        self.compute_offset = 0

        self.context = moderngl.create_standalone_context(require=430)
        self.compute_shader = self.context.compute_shader(gl_util.source(os.path.dirname(__file__)+'/strain.glsl', consts))

        self.consts = consts

        # Buffer de positions au temps t
        self._BUFFER_P_T = self.context.buffer(reserve=2 * 4 * self.npart)
        self._BUFFER_P_T.bind_to_storage_buffer(0)

        # Buffer de positions au temps t - dt
        self._BUFFER_P_DT = self.context.buffer(reserve=2 * 4 * self.npart)
        self._BUFFER_P_DT.bind_to_storage_buffer(1)

        # Buffer d'epsilon
        self._BUFFER_E = self.context.buffer(reserve= 4 * 4 * self.npart)
        self._BUFFER_E.bind_to_storage_buffer(2)

        self.array_shape = (self.npart, 2, 2)

    def set_post(self, pos):
        """

        Parameters
        ----------
        pos : np.ndarray
            Array of positions.

        Returns
        -------

        """
        self._BUFFER_P_T.write(pos.astype('f4').tobytes())

    def set_posdt(self, pos):
        """
        Parameters
        ----------
        pos : np.ndarray
            Array of positions.

        Returns
        -------

        """
        self._BUFFER_P_DT.write(pos.astype('f4').tobytes())

    def compute(self):
        """
        Compute the strain.
        Returns
        -------

        """
        self.compute_shader.run(group_x=self.groups_number)

    def get_eps(self):
        """

        Returns
        -------
        np.ndarray
            Computed inter-atomic forces.
        """
        return np.frombuffer(self._BUFFER_F.read(), dtype=np.float32).reshape(self.array_shape)


def compute_strain(model0:Model, model1:Model, rcut):
    params = model0.params.copy()
    params["RCUT"] = rcut
    strain_compute = StrainComputeGPU(params)
    strain_compute.set_post(model0.pos)
    strain_compute.set_posdt(model1.pos)
    strain_compute.compute()
    return strain_compute.get_eps()