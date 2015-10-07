import numpy as np
from astropy.io import ascii

def get_isochrone_struct(infile,quantities=None,age=None):
    data=ascii.read(infile)

    # option to select a certain age
    if age is not None:
        gd=np.where(data['log(age/yr)']==age)
        data=data[gd]

    # default columns
    if quantities is None:
        data.keep_columns(['Z','log(age/yr)','logTe','logL/Lo','int_IMF','stage'])
    else:
        data.keep_columns(quantities)

    # option to request certain columns
#    data.keep_columns(quantities)

    return data
