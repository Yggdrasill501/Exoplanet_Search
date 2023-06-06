# -*- coding: utf-8 -*-

import juliet
import numpy as np
import matplotlib.pyplot as plt


class Tess:
    """
    This class is used to download and plot TESS data.
    """
    def __init__(self, data_url):
        self.url = data_url

    def tess_data(self):

        t,f,ferr = juliet.get_TESS_data(self.url,'hlsp_tess-data-alerts_tess_phot_00403224672-'+\
                                        's01_tess_v1_lc.fits')

        plt.errorbar(t,f,yerr=ferr,fmt='.')

        plt.xlim([np.min(t),np.max(t)])
        plt.ylim([0.999,1.001])
        plt.xlabel('Time (BJD - 2457000)')
        plt.ylabel('Relative flux')
        plt.show()

        times, fluxes, fluxes_error = {}, {}, {}
        # Save data into those dictionaries:
        times['TESS'], fluxes['TESS'], fluxes_error['TESS'] = t, f, ferr

        priors = {}

        # Name of the parameters to be fit:
        params = ['P_p1', 't0_p1', 'r1_p1', 'r2_p1', 'q1_TESS', 'q2_TESS', 'ecc_p1', 'omega_p1', \
                  'rho', 'mdilution_TESS', 'mflux_TESS', 'sigma_w_TESS']

        # Distribution for each of the parameters:
        dists = ['normal', 'normal', 'uniform', 'uniform', 'uniform', 'uniform', 'fixed', 'fixed', \
                 'loguniform', 'fixed', 'normal', 'loguniform']

        # Hyperparameters of the distributions (mean and standard-deviation for normal
        # distributions, lower and upper limits for uniform and loguniform distributions, and
        # fixed values for fixed "distributions", which assume the parameter is fixed)
        hyperps = [[1., 0.1], [1325.55, 0.1], [0., 1], [0., 1.], [0., 1.], [0., 1.], 0.0, 90., \
                   [100., 10000.], 1.0, [0., 0.1], [0.1, 1000.]]

        # Populate the priors dictionary:
        for param, dist, hyperp in zip(params, dists, hyperps):
            priors[param] = {}
            priors[param]['distribution'], priors[param]['hyperparameters'] = dist, hyperp

    def run(self):

        self.tess_data()
