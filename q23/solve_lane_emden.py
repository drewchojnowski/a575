import numpy as np
import math
import os.path
from astropy.io import ascii
from astropy import constants as const
from astropy.table import Table, Column
import matplotlib.pyplot as plt

default_n=2.0
default_dx=0.0001

def integrate_le(n=None,dx=None):
    # Defaults for n and dx, in case not provided
    if n is None: n=default_n
    if dx is None: dx=default_dx

    # BOUNDARY CONDITIONS:
    #    1. t(x)=1 at x=0
    #    2. dt/dx=0 at x=0
    t=1.000
    dtdx=0.000

    # give x a small, non-zero starting value:
    x=0.0000000001

    # Do the integration via Euler method, writing results to file 
    outfile=open('polytrope_n'+str(n)+'.dat','wb')
    outfile.write('x            ')
    outfile.write('t            ')
    outfile.write('dtdx    \n')
    while (t >= 0):
        dtdx=dtdx-((2.0*dtdx/x)+(t**n))*dx
        t=t+(dtdx*dx)
        x=x+dx
        outfile.write(str(x)+' ')
        outfile.write(str(t)+' ')
        outfile.write(str(dtdx)+'\n')

    outfile.close()

    return x

def calculate_values(n=None,dx=None,xfrac=None,zfrac=None,mass=None,radius=None,display=None):
    # Defaults for n and dx, in case not provided
    if n is None: n=default_n
    if dx is None: dx=default_dx

    # check for the polytrope outfile
    # create it if it doesn't exist
    polyfile='polytrope_n'+str(n)+'.dat'
    if os.path.exists(polyfile) is not True:
        integrate_le(n)

    # read the polytrope outfile
    data=ascii.read(polyfile)
    x=data['x']
    t=data['t']
    dtdx=data['dtdx']

    # set default abundances if not provided
    if xfrac is None: xfrac=0.7
    if zfrac is None: zfrac=0.02
    # calculate mean molecular weight
    mmw=4.0/(3.0+(5.0*xfrac)-zfrac)

    # set default mass and radius if not provided
    if mass is None: mass=1.0
    if radius is None: radius=1.0
    # mass and radius should be provided in terms of M_sun/R_sun
    mass=mass*const.M_sun.cgs
    radius=radius*const.R_sun.cgs

    # other needed constants
    grav=const.G.cgs
    u=const.u.cgs
    kb=const.k_B.cgs
    
    # find where xi first crosses zero
    firstzero=np.where(abs(t)==min(abs(t)))
    x1=x[firstzero]
    dtdx1=dtdx[firstzero]

    # calculate values for Jason's table (http://astronomy.nmsu.edu/jasonj/565/polytable.html)
    rhofrac=-1.0*(x1/(3.0*dtdx1))
    n_n=((4.0*math.pi)**(1.0/n))/(n+1.0) * ((-1.0*(x1**((n+1.0)/(n-1.0))))*dtdx1)**((1.0-n)/n)
    k=n_n*grav*(mass**((n-1.0)/n))*(radius**((3.0-n)/n))
    w_n=(4.0*math.pi*(n+1.0)*(dtdx1**2.0))**(-1.0)
    bigtheta=(-1.0*(n+1.0)*x1*dtdx1 )**(-1.0)
    rho_c=rhofrac*((3.0*mass)/(4.0*math.pi*(radius**3.0)))
    p_c=(w_n*grav*(mass**2.0))/(radius**4.0)
    t_c=(bigtheta*grav*mass*mmw*u)/(kb*radius)

    # put the values in a Table, print the Table, and return the Table.
    out=Table()
    out['M_tot']=mass; out['Radius']=radius; 
    out['n']=[n];         out['xi_1']=[x1[0]]; out['rho_c/rho_mean']=[rhofrac[0]]
    out['N_n']=[n_n[0]];  out['W_n']=[w_n[0]]; out['Theta_n']=[bigtheta[0]]
    out['rho_c']=[rho_c]; out['P_c']=[p_c];    out['T_c']=[t_c]
    out['K']=[k]

    if display is not None: print out

    return out

def make_plot(n=None,dx=None,save=None,show=None):
    # Defaults for n and dx, in case not provided
    if n is None: n=default_n
    if dx is None: dx=default_dx

    # check for the polytrope outfile
    # create it if it doesn't exist
    polyfile='polytrope_n'+str(n)+'.dat'
    if os.path.exists(polyfile) is not True:
        integrate_le(n)

    # read the polytrope outfile
    data=ascii.read(polyfile)
    x=data['x']
    t=data['t']
    dtdx=data['dtdx']

    # get values needed for plotting q
#    vals=calculate_values(n,dx=dx)

#    mass_int=(-4.0*math.pi)*((((n+1)*vals['k'])/(4.0*math.pi*const.G.cgs))**(3/2.0))*((x**2.0)*dtdx)
#    q=mass_int/vals['M_tot']

    # find where xi first crosses zero
    firstzero=np.where(abs(t)==min(abs(t)))
    x1=x[firstzero]
    dtdx1=dtdx[firstzero]

    plt.plot(x,t,'r',x,t**n,'b',x,t**(n+1.0),'g')
    plt.xlim(0,x1)
    plt.ylim(0,1)
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\theta$')

    plt.text(3.0,0.93,'n='+str(n))
    plt.text(3.0,0.85,r'$\theta(\xi) = T/T_{c}$',color='r')
    plt.text(3.0,0.78,r'$\theta^{n}(\xi) = \rho/\rho_{c}$',color='b')
    plt.text(3.0,0.71,r'$\theta^{n+1}(\xi) = P/P_{c}$',color='g')

    if save is not None: plt.savefig('polytrope_n'+str(n)+'.png')
    if show is not None: plt.show()


