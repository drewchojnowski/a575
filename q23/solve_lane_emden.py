import numpy as np
import math
import os.path
from astropy.io import ascii
from astropy import constants as const

def solve_lane_emden(n=None,dx=None):
    # Defaults for n and dx, in case not provided
    if n is None: n=2.0
    if dx is None: dx=0.0001

    # BOUNDARY CONDITIONS:
    #    1. t(x)=1 at x=0
    #    2. dt/dx=0 at x=0
    t=1.0
    dtdx=0.0

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

def calculate_values(n=None,xfrac=None,zfrac=None,mass=None,radius=None):
    if n is None: n=2.0

    # check for the polytrope outfile
    # create it if it doesn't exist
    polyfile='polytrope_n'+str(n)+'.dat'
    x=os.path.exists(polyfile)
    if x is not True:
        solve_lane_emden(n)

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
    print 'Xi_1'+str(x1)+'\n'

    rhofrac=-1.0*(x1/(3.0*dtdx1))
    print 'rho_c/rho_mean'+str(rhofrac)+'\n'

    n_n=((4.0*math.pi)**(1.0/n))/(n+1.0) * ((-1.0*(x1**((n+1.0)/(n-1.0))))*dtdx1)**((1.0-n)/n)
    print 'N_n'+str(n_n)+'\n'

    w_n=(4.0*math.pi*(n+1.0)*(dtdx1**2.0))**(-1.0)
    print 'W_n'+str(w_n)+'\n'

    bigtheta=(-1.0*(n+1.0)*x1*dtdx1 )**(-1.0)
    print 'Theta_n'+str(bigtheta)+'\n'

    rho_c=rhofrac*((3.0*mass)/(4.0*math.pi*(radius**3.0)))
    print 'Rho_c'+str(rho_c)+'\n'

    p_c=(w_n*grav*(mass**2.0))/(radius**4.0)
    print 'P_c'+str(p_c)+'\n'

    t_c=(bigtheta*grav*mass*mmw*u)/(kb*radius)
    print 'T_c'+str(t_c)+'\n'

    return data
