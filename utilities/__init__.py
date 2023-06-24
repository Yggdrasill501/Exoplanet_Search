# -*- coding: utf-8 -*-
"""Package to gather data from Sateliets"""
from utilities.get_single_data import GetSingleData
from utilities.parser import Parser


if __name__ == '__main__':
    getdata = GetData()
    getdata.run()
    parser = Parser()
    parser.run()
