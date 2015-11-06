import os
import numpy as np
from astropy.io import ascii
import matplotlib
import matplotlib.pyplot as plt
import math
import glob

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

def plot_hess(infile='zp00.dat',outfile=None,quantities=['logTe','logL/Lo'],show=False,m_tot=100.0,nbins=50):
    data=ascii.read(infile)
    ndata=len(data['Z'])
    x=data['logTe']
    y=data['logL/Lo']
    imf=[]
    for i in range(ndata):
        if i==0:
            imf.append(0.0)
        else:
            imf.append((data['int_IMF'][i]-data['int_IMF'][i-1])*1000.0)

    fig=plt.figure(1,figsize=(8, 7))
    matplotlib.rcParams.update({'font.size': 16, 'font.family':'serif'})
#    plt.scatter(data[quantities[0]],data[quantities[1]],zorder=1,edgecolors='none',s=1,c='black')

#    Z, xedges, yedges = np.histogram2d(data['logTe'],data['logL/Lo'],bins=(300,300))
#    x = 0.5*(xedges[:-1] + xedges[1:])
#    y = 0.5*(yedges[:-1] + yedges[1:])
#    Y, X = np.meshgrid(y, x)
#    Z = np.ma.array(Z, mask=(Z==0))
#    levels = [0, 0.5, 1, 2, 4, 8]
#    cntr=plt.contourf(X,Y,Z,levels,cmap='terrain',zorder=2)

    plt.hist2d(x, y, bins=nbins,cmap='jet',weights=imf,cmin=0.0001,cmax=5)

    plt.xlabel(quantities[0])
    plt.ylabel(quantities[1])
    plt.gca().invert_xaxis()

    # option to display on screen
    if show: 
        plt.show()

    # option to write an output file (only works if show=False)
    if outfile is not None:
        plt.savefig(outfile,dpi=300)

    return imf


