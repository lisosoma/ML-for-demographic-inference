import dadi
import numpy as np


def model_func(params, ns, pts):
    """
    Simple two populations model. Ancestral population of constant size splits
    into two subpopulations of constant size with asymetrical migrations.

    :param nu1: Size of subpopulation 1 after split.
    :param nu2: Size of subpopulation 2 after split.
    :param m12: Migration rate from subpopulation 2 to subpopulation 1.
    :param m21: Migration rate from subpopulation 1 to subpopulation 2.
    :param T: Time of split.
    """

    nu1, nu2, m12, m21, T = params

    xx = dadi.Numerics.default_grid(pts)
    phi = dadi.PhiManip.phi_1D(xx)

    phi = dadi.PhiManip.phi_1D_to_2D(xx, phi)
    phi = dadi.Integration.two_pops(phi, xx, T, nu1=nu1, nu2=nu2, m12=m12, m21=m21)

    fs = dadi.Spectrum.from_phi(phi, ns, [xx, xx])
    return fs
    
    
