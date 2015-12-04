import os
import numpy as np
from astropy.io import ascii
import matplotlib
import matplotlib.pyplot as plt
import math
import glob
from matplotlib.colors import LogNorm
from matplotlib.ticker import MultipleLocator
import pdb
import pyfits as pyfits

def imf_random_deviates(npts=1000,plotfile=None):
    # mass limits
    minM=0.5
    maxM=100.0
    # exponent of the IMF
    expo=-2.35

    # create the random deviates and an empty mass array
    rand=np.random.uniform(0,1,npts)
    m=np.zeros(npts)

    # calculate the normalization constant by integrating
    # and setting the result equal to 1.
    # On paper, I get const=0.5300091178
    tmp=expo+1.0
    const=abs(tmp)/((minM**tmp)-(maxM**tmp))

    # loop over the random deviates and calculate masses based 
    # the inverted integral set equal to the random deviates.
    # i.e. m[i]=(-1.35X/const + 0.5^-1.35)^(1/-1.35)
    for i in range(npts):
        m[i]=(((tmp*rand[i])/const)+(0.5**tmp))**(1.0/tmp)

    x=np.arange(minM,maxM,1./npts)

    fig, (ax0,ax1) = plt.subplots(nrows=2,figsize=(10, 10))
    p0=ax0.hist(m,bins=npts)
    ax0.plot(x,x**(-2.35),linewidth=3)
    ax0.set_ylabel('N')
    ax0.set_xlim([minM,maxM])
#    ax0.set_xticks([])
    ax0.set_title(str(npts)+' random deviates')

    p1=ax1.hist(m,bins=npts,log=True)
#    ax1.plot(x,np.log10(x**(-2.35)),linewidth=3)
    ax1.set_ylabel('N')
    ax1.set_xlabel(r'$\rm M_{\odot}$')
    ax1.set_xlim([minM,maxM])

#    p2=ax2.loglog(m)

    matplotlib.rcParams.update({'font.size': 16, 'font.family':'serif'})
    plt.tight_layout() 

    if plotfile is not None:
        plt.savefig(plotfile)

    return m



