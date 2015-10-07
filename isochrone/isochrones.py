import numpy as np
from astropy.io import ascii

def get_isochrone_struct(infile,quantities=None,age=None,outfile=None):
    data=ascii.read(infile)

    # option to select a certain age
    if age is not None:
        gd=np.where(data['log(age/yr)']==age)
        data=data[gd]

    # default columns
    if quantities is None:
        data.keep_columns(['Z','log(age/yr)','logTe','logL/Lo','int_IMF','stage'])
    # option to extract specified columns
    else:
        data.keep_columns(quantities)

    # option to write an output file
    if outfile is not None:
        cols=data.colnames
        header=''
        for col in cols:
            header=header+'   '+col
        np.savetxt(outfile,data,fmt='%.5f',header=header)

    return data
