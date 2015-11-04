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

def plot_iso(infile,age=None,outfile=None,show=False):
    import matplotlib.pyplot as plt

    data=ascii.read(infile)

    # option to select a certain age
    if age is not None:
        gd=np.where(data['log(age/yr)']==age)
        data=data[gd]

    fig, axes = plt.subplots(2,2)
    ax0, ax1, ax2, ax3 = axes.flat

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.1)

    ax0.plot(data['logTe'],data['logG'])
    ax2.plot(data['logTe'],data['mbol'])
    ax1.plot(data['logTe'],data['logG'])
    ax3.plot(data['logTe'],data['logG'])

    ax2.set_xlabel(r'Log $\rm T_{eff}$')
    ax3.set_xlabel(r'Log $\rm T_{eff}$')

    ax0.set_ylabel('Log g')
    ax2.set_ylabel('Mbol')
    ax1.set_ylabel('Log g')
    ax3.set_ylabel('Log g')

    ax0.set_xlim((4.2,3.4))
    ax2.set_xlim((4.2,3.4))
    ax1.set_xlim((4.2,3.4))
    ax3.set_xlim((4.2,3.4))

    ax0.set_xticklabels([])
    ax1.set_xticklabels([])

    # option to write an output file
    if outfile is not None:
        plt.savefig(outfile)

    if show: plt.show()

    return data
