'''
Write a routine to convolve a vector of length 8192 pixels that consists of a 
series of delta functions spaced every 10 pixels, with a Gaussian with 
$ \sigma$ = 5 pixels. Do the convolution in physical space, writing the 
convolution integral explicitly (i.e., don't use a canned convolution 
routine!) Then do it in Fourier space by taking the Fourier transform of 
the vector and the Gaussian, multiplying them, and then Fourier transforming 
back (canned routines OK!). Plot both results. 
'''

import matplotlib.pyplot as plt
import numpy as np
import math

def q32():
    datasize=8192
    delta_height=1
    delta_spacing=10

    # make a single array with 10 zeros and a one
    y_single=np.array([0]*delta_spacing+[delta_height])

    # figure out how many times to replicate y_single, based on npix.
    n=int(np.floor(datasize/len(y_single)))
    # get the remainder
    rem=(datasize-n*len(y_single))*[0]
    
    # replicate x_single n times
    y=np.tile(y_single,n)
    # tack on zeros for the remainder array elements
    y=np.array(y.tolist()+rem)

    # make the guassian kernel
    kernelsize=23
    sigma=5
    # take the gaussian center as median of kernelsize
    b=np.median(np.arange(kernelsize))
    kernel=[]
    for i in range(kernelsize):
        t=(1.0/sigma*np.sqrt(2*math.pi))*np.exp((-0.5*(i-b)**2)/(2*sigma^2))
        kernel.append(t)

    kernel=np.array(kernel)
    # Now we've got the delta function array and gaussian kernel
    # Time to convolve these motherfuckers.

    # how to do this with np.convolve
#    yconv=np.convolve(y,kernel,mode='same')

    output_len=kernelsize+datasize-1
    yconv=np.zeros(output_len)

    for i in range(datasize):
        for j in range(kernelsize):
            yconv[i+j]+=y[i]*kernel[j]
            
    fig=plt.figure()
    plt.plot(y)
    plt.plot(yconv)
    plt.xlim([0,100])
    plt.ylim(0,1.2)

    return y,kernel,yconv
