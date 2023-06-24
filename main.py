# -*- coding: utf-8 -*-
""" File to run whole project """
from exoplanet_search_by_star_id import ExoPlaneSearchByStarId
starid = '6922244'
autor = 'kepler'

if __name__ == '__main__':
    get_planet = ExoPlaneSearchByStarId(star_id= starid, autor=autor)
