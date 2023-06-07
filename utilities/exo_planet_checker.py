# -*- coding: utf-8 -*-
"""File to check exo planet if exo planet has been found around star"""


class ExoPlanetChecker:
    """Class to check exo planet if exo planet has been found"""
    def __init__(self, exo_plane_id: str) -> None:
        """Initialize class"""
        self.exo_plane_id = exo_plane_id
        self.url = 'https://exo.mast.stsci.edu/'
