#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:31:17 2022

@author: Serena A. Cronin

Handy functions to perform a convolution.

"""
from astropy.convolution import Gaussian2DKernel
import numpy as np

def gauss_2d_kernel(sigma):
    
    """
    
    Input : 
        sigma for a 2D Gaussian Kernel.
        
    Output: 
        kernel array where the center is negative, the surrounding values
        are positive, and the entire kernel averages to 0.
        
    Requires Gaussian2DKernel from astropy.convolution
    
    """
    
    # create the kernel
    kernel = Gaussian2DKernel(x_stddev=sigma)
    
    # get the center of the kernel; this should be the max of the kernel, too
    center_index = kernel.shape[0]//2, kernel.shape[1]//2  # integer divide
    kern_arr = kernel.array  # get the kernel array
    
    # make the center pixel positive and the rest negative
    kern_arr[center_index]*=-1
    kern_arr*=-1
    
    # make sure the entire kernel averages to 0
    kern_arr[center_index] = -1*np.sum(kern_arr[kern_arr<0.])
    
    return kern_arr