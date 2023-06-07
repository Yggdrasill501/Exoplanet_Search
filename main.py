# -*- coding: utf-8 -*-
""" File to run whole project """
from utilities.get_data import GetData
from utilities.parser import Parser
#from settings import *
#from tess import Tess

from juliet import get_all_TESS_data

juliet_data = get_all_TESS_data()

if __name__ == '__main__':
    print(type(juliet_data))
# tess = Tess(TESS_DATA_URL)
#tess.run()
