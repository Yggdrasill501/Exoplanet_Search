# -*- coding: utf-8 -*-
"""File to download and unzip data from Tess"""
from requests import get
from abc import abstractmethod

class GetAllData:
    def __init__(self, url : str) -> None:
        """Initialize class"""
        self.url = url

    @abstractmethod
    def download_files(self) -> None:
        """Method to download files from Tess"""
        request = get(self.url)
        if request.status_code == 200:
            with open('tess_data.fits', 'wb') as file:
                file.write(request.content)

    @abstractmethod
    def run(self) -> None:
        """Method to run GetData class"""
        self.download_files()