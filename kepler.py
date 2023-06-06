# -*- coding: utf-8 -*-

import lightkurve as lk
import juliet
from settings import *


class Kepler:

    def __init__(self):
        self.url = KEPLER_DATA_URL

    def kepler_data(self):
      #  t, f, ferr = juliet.(self.url)
        pass

    def get_data(self):
        pass

    def plot(self):
        pass

    def run(self):
        self.get_data()
