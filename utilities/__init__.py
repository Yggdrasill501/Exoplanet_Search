# -*- coding: utf-8 -*-
"""Package to gather data from Sateliets"""
from utilities.get_data import GetData
from utilities.parser import Parser


if __name__ == '__main__':
    getdata = GetData()
    getdata.run()
    parser = Parser()
    parser.run()
