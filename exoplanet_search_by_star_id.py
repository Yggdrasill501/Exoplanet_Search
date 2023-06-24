# -*- coding: utf-8 -*-
"""File thet will find if there is exoplanet atomaticly by id"""

import lightkurve as lk
import numpy as np

from lightkurve import search_targetpixelfile
from lightkurve import TessTargetPixelFile
from matplotlib import pyplot

class ExoPlaneSearchByStarId:

    def __init__(self, star_id : str, autor : str) -> None:

        self.pixel_file = search_targetpixelfile(f'Kic {star_id}', autor= f'{autor}', cadence='long', quarter=4).download()

    def get_light_curve(self):
        light_curve = self.pixel_file.to_lightcurve(aperture_mask=self.pixel_file.pipeline_mask)
        flat_light_curve = light_curve.flatten()
        folded_light_curve = self.flat_light_curve.fold(period=3.5225)
        
