# -*- coding: utf-8 -*-
"""File to download and unzip data from Tess"""
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
from abc import abstractmethod


class GetData:
    """Class to download and unzip data from Tess"""

    def __init__(self, product_group_id: str) -> None:
        """Initialize class
        :param product_group_id: id of star from Tess
        """
        self.zip_file = None
        self.http_response = None

        self.url = 'https://www.mast.stsci.edu/api/v0.1/Download/bundle.zip?previews=false&obsid='
        self.url.join(product_group_id)

        self.destination = '/tess_data/'

    @abstractmethod
    def download_files(self) -> None:
        """Method to download files from Tess"""
        self.http_response = urlopen(self.url)

    @abstractmethod
    def unzip_files(self) -> None:
        """Method to unzip files from Tess"""
        self.zip_file = ZipFile(BytesIO(self.http_response.read()))
        self.zip_file.extractall(self.destination)

    @abstractmethod
    def run(self) -> None:
        """Method to run GetData class"""
        self.download_files()
        self.unzip_files()
