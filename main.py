from settings import *
from tess import Tess

if __name__ == '__main__':
    tess = Tess(TESS_DATA_URL)
    tess.run()

