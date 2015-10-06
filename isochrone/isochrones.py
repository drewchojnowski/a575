import numpy as np
from astropy.io import ascii

def get_isochrone_struct(infile,quantities=['Z','log(age/yr)','logTe','logL/Lo','int_IMF','stage'],age=8):
    data=ascii.read(infile)
    gd=np.where(data['log(age/yr)']==age)
    data=data[gd]
    data.keep_columns(quantities)

    return data
