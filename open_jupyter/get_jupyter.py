# -*- coding: utf-8 -*-
"""File install to jupyter notebook and open on local host"""
from subprocess import call
from abc import abstractmethod
import pip
from time import sleep

class GetJupyter:
    """Class to get jupyter notebook"""
    def __init__(self) -> None:
        """Initialize class"""

    @staticmethod
    def in_venv() -> bool:
        installed_packages = pip.get_installed_distributions()
        flat_installed_packages = [package.project_name for package in installed_packages]
        if 'jupyter' in flat_installed_packages:
            return True
        else:
            return False

    @abstractmethod
    def install_jupyter(self) -> None:
        """Function to install jupyter notebook"""
        call('pip install jupyter', shell=True)

    @abstractmethod
    def get_jupyter(self) -> None:
        """Function to open jupyter notebook on local host"""
        call('jupyter notebook', shell=True)


    @abstractmethod
    def run(self) -> None:
        """Method to run whole class"""
        if not self.in_venv():
            self.install_jupyter()
            sleep(20)

        self.get_jupyter()
