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

#os.environ['ISOCHRONE_DIR'] = 'isochrones/'
isochrone_dir='isochrones/'

def get_isochrone_struct(infile,quantities=None,age=None,outfile=None):
    data=ascii.read(isochrone_dir+infile)

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

def plot_iso(age=9.00,feh=0.0,outfile=None,show=False,symsize=4,cmap1='terrain',cmap2='rainbow'):
    # collect some data for left side plots
    files=glob.glob(isochrone_dir+'z*dat')
    logte_all=None
    logg_all=None
    mbol_all=None
    feh_all=None
    for file in files:
        # read data and restrict to a certain age
        data=ascii.read(file)
        gd=np.where(data['log(age/yr)']==age)
        data=data[gd]

        # decompose filename to get array of [M/H] values
        tmp=file.split("z")
        tmp=tmp[1].split(".")[0]
        sign=tmp[0:1]
        feh_str=tmp[1:3]
        feh_val=float(feh_str[0:1]+'.'+feh_str[1:2])
        if sign=='m': feh_val=feh_val*-1

        # build up arrays for plots
        logte=data['logTe'].tolist()
        logg=data['logG'].tolist()
        mbol=data['mbol'].tolist()
        feh_arr=np.repeat(feh_val,len(data)).tolist()
        if logte_all is None:
            logte_all=logte
            logg_all=logg
            mbol_all=mbol
            feh_all=feh_arr
        else:
            logte_all=logte_all+logte
            logg_all=logg_all+logg
            mbol_all=mbol_all+mbol
            feh_all=feh_all+feh_arr

    # set up some plotting parameters
    fig=plt.subplots(2,2,figsize=(14, 10))
    matplotlib.rcParams.update({'font.size': 16, 'font.family':'serif'})
    xtit=r'Log $\rm T_{eff}$'
    ytit1='log g'
    ytit2=r'M$\rm_{bol}$'

    # left side plots
    p1=plt.subplot(221)
    plt.scatter(logte_all,logg_all,c=feh_all,cmap=cmap1,edgecolors='none',s=symsize)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.xticks([])
    plt.ylabel(ytit1)
    plt.text(0.5,1.04,'Age = '+str(age)+' Gyr',transform=p1.transAxes,ha='center')

    p2=plt.subplot(223)
    plt.scatter(logte_all,mbol_all,c=feh_all,cmap=cmap1,edgecolors='none',s=symsize)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.xlabel(xtit)
    plt.ylabel(ytit2)

    #            left   bot  xthick ythick
    cax=plt.axes([0.395, 0.07, 0.03, 0.88])
    cb=plt.colorbar(cax=cax, orientation='vertical')
    plt.text(0.5,0.5,'[M/H]',transform=cax.transAxes,rotation=90,ha='center',va='center')

    # get the single metallicity isochrone
    if feh < 0: pref='zm'
    if feh >= 0: pref='zp'
    bla=str(abs(feh))
    strfeh=pref+bla[0:1]+bla[2:3]

    data=ascii.read(isochrone_dir+strfeh+'.dat')

    # right side plots
    p3=plt.subplot(222)
    plt.scatter(data['logTe'],data['logG'],c=data['log(age/yr)'],cmap=cmap2,edgecolors='none',s=symsize)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.xticks([])
    plt.ylabel(ytit1)
    plt.text(0.5,1.04,'[M/H] = '+str(feh),transform=p3.transAxes,ha='center')

    p4=plt.subplot(224)
    plt.scatter(data['logTe'],data['mbol'],c=data['log(age/yr)'],cmap=cmap2,edgecolors='none',s=symsize)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.xlabel(xtit)
    plt.ylabel(ytit2)

    cax=plt.axes([0.919, 0.07, 0.03, 0.88])
    cb=plt.colorbar(cax=cax, orientation='vertical')
    plt.text(0.5,0.5,'log(age/yr)',transform=cax.transAxes,rotation=90,ha='center',va='center')

    plt.subplots_adjust(left=0.053, bottom=0.07, right=0.915, top=0.95, wspace=0.55, hspace=0.1)

    # option to display on screen
    if show: 
        plt.show()

    # option to write an output file (only works if show=False)
    if outfile is not None:
        plt.savefig(outfile)


    return

def plot_hess(infile='zp00.dat',age=8.0,plotfile=None,fitsfile=None,quantities=['logTe','logL/Lo'],show=False,m_tot=1000.0,nbins=[20]):
    data=get_isochrone_struct(infile,age=age)
    xdata=np.array(data[quantities[0]])
    ydata=np.array(data[quantities[1]])

    # decompose filename to get array of [M/H] values
    tmp=infile.split("z")
    tmp=tmp[1].split(".")[0]
    sign=tmp[0:1]
    feh_str=tmp[1:3]
    feh_val=float(feh_str[0:1]+'.'+feh_str[1:2])
    if sign=='m': feh_val=feh_val*-1
    feh=str(feh_val)

#    yr=[-3.5,4.5]
#    xr=[3.3,4.25]
    xr=[min(xdata),max(xdata)]
    yr=[min(ydata),max(ydata)]

    imf=np.array(data['int_IMF'])

#   allow for different # of bins in x and y directions
    nbinsX=nbins[0]
    if len(nbins)==2:
        nbinsY=nbins[1]
    else:
        nbinsY=nbins[0]

    xbinsize=abs(xr[1]-xr[0])/nbinsX
    ybinsize=abs(yr[1]-yr[0])/nbinsY

    ximage=np.floor((xdata-min(xdata))/xbinsize).astype('int')
    yimage=np.floor((ydata-min(ydata))/ybinsize).astype('int')

    hess=np.zeros([nbinsX+1,nbinsY+1])

    for i in range(len(ximage)-1):
        nstars=(imf[i+1]-imf[i])*m_tot
        for ix in range(min(ximage[i],ximage[i+1]),max(ximage[i],ximage[i+1])+1):
            for iy in range(min(yimage[i],yimage[i+1]),max(yimage[i],yimage[i+1])+1):
                hess[ix,iy]+=nstars/(nbinsX*nbinsY)

    fig=plt.subplots(1,1,figsize=(10, 10))
    matplotlib.rcParams.update({'font.size': 16, 'font.family':'serif'})
    im=plt.imshow(hess.T,interpolation='none',extent=(xr[0],xr[1],yr[0],yr[1]),aspect='auto',cmap='jet',origin='lower')
    cb=plt.colorbar(im)
    plt.scatter(xdata,ydata)
    msunstr=r'$\rm M_{tot} = '+str(m_tot)+' M_{\odot}$'
    plt.title(str(age)+' GYr,  [M/H] = '+feh+',  '+msunstr)
    plt.xlabel(r'Log $\rm T_{eff}$')
    plt.ylabel('Log L')
    plt.tight_layout()

    if plotfile is not None:
        plt.savefig(plotfile)

    if fitsfile is not None:
        hdu=pyfits.PrimaryHDU(hess)
        hdulist=pyfits.HDUList([hdu])
        hdu.writeto(fitsfile)

    return hess

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

    fig, (ax0,ax1) = plt.subplots(nrows=2,figsize=(10, 10))
    p0=ax0.hist(m,bins=npts)
    ax0.set_ylabel('N')
#    ax0.set_xticks([])
    ax0.set_title(str(npts)+' random deviates')
    p0=ax1.hist(m,bins=npts,log=True)
    ax1.set_ylabel('N')
    ax1.set_xlabel(r'$\rm M_{\odot}$')
    matplotlib.rcParams.update({'font.size': 16, 'font.family':'serif'})
    plt.tight_layout() 

    if plotfile is not None:
        plt.savefig(plotfile)

    return m



