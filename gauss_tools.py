#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:39:29 2022

@author: cronin
"""

import numpy as np

def three_gaussian(x_array, amp1,cen1,sigma1, amp2,cen2,sigma2, amp3,cen3,sigma3, sepA,sepB,R):
    """
    Function that will fit three Gaussians at fixed separations.
    
    Input: initial guesses for amplitudes, centroids, and sigmas. Optional inputs of centroids for peaks 2 and 3. 
    Otherwise, input values for sepA and sepB. If cen2, cen3, sepA, and sepB are 0, this means they are None.
    
    Output: 3-peak Gaussian function
    
    Definitions: sepA = separation between first two peaks 
    sepB = separation between middle and third peak
    R = resolution, according to the telescope instrument
    
    """
    
    if cen2 == 0:
        cen2 = cen1-sepA
    if cen3 == 0:
        cen3 = cen1+sepB
        
    if sigma2 == 0:
        sigma2 = cen2/R
    if sigma3 == 0:
        sigma3 = cen3/R
    
    gauss1 = amp1*(np.exp((-1.0/2.0)*(((x_array-cen1)/sigma1)**2)))
    gauss2 = amp2*(np.exp((-1.0/2.0)*(((x_array-cen2)/sigma2)**2)))
    gauss3 = amp3*(np.exp((-1.0/2.0)*(((x_array-cen3)/sigma3)**2)))
    
    return(gauss1+gauss2+gauss3)

def two_gaussian(x_array, amp1,cen1,sigma1, amp2,cen2,sigma2):
    gaussian1 = amp1*(np.exp((-1.0/2.0)*(((x_array-cen1)/sigma1)**2)))
    gaussian2 = amp2*(np.exp((-1.0/2.0)*(((x_array-cen2)/sigma2)**2)))
    return(gaussian1+gaussian2)

def one_gaussian(x_array, amp1,cen1,sigma1):
    gaussian1 = amp1*(np.exp((-1.0/2.0)*(((x_array-cen1)/sigma1)**2)))
    return(gaussian1)

def red_chisq(obs,calc,num_params,err):
    return((np.sum((obs-calc)**2 / err))/(len(obs)-num_params))