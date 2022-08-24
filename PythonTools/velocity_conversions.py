#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:07:12 2022

@author: Serena A. Cronin

These are common conversions between velocity, wavelength, and frequency.

"""

def velocity_to_wavelength(vels, restwl, convention='optical'):
    
    """
    This function takes in velocities and a rest wavelength and converts
    the velocities to wavelength using the optical convention of velocity.
    
    Adapted from https://www.gb.nrao.edu/~fghigo/gbtdoc/doppler.html
    and https://github.com/keflavich/pyspeckit-obsolete/blob/57e36b705a1eea2a3d8b20a75dfd0c32ff61f832/pyspeckit/spectrum/units.py#L1169
    
    ------
    Input
    ------
    
    vels : array, list, float, or int
        Input velocities in km/s
        
    restwl : float or int
        Rest wavelength in Angstroms
       
    ------
    Output
    ------
    
    wls : wavelengths in Angstroms
    
    """
    
    # wls = restwl*(vels + c)/c
    
    c_ms = 3.0*10**8
    restwl_m = restwl*(1e-10) # Angstroms to m
    vels_ms = vels*1e3
    restfreq_hz = c_ms / restwl_m  # center frequency
    
    if convention == 'optical':
        freqs_hz = (vels_ms / c_ms + 1.0)**-1 * restfreq_hz
    elif convention == 'radio':
        freqs_hz = (vels_ms / c_ms - 1.0)**-1 * restfreq_hz * -1
    elif convention == 'relativisitic':
        freqs_hz = (-(vel_ms / c_ms)**2 + 1.0)**0.5 / (1.0 + vel_ms/c_ms) * restfreq_hz
    else:
        raise ValueError('Choose a convention: optical, radio, or relativistic.')
    
    wls_m = (3.0*10**8) / freqs_hz  # shifted freqs to wavelength
    wls_ang = wls_m / (1e-10)  # wavelength from meters to angstroms
    
    return wls_ang


def wavelength_to_velocity(wls, restwl, convention='optical'):
    
    """
    This function takes in velocities and a rest wavelength and converts
    the velocities to wavelength using the optical convention of velocity.
    
    Adapted from https://www.gb.nrao.edu/~fghigo/gbtdoc/doppler.html
    and https://github.com/keflavich/pyspeckit-obsolete/blob/57e36b705a1eea2a3d8b20a75dfd0c32ff61f832/pyspeckit/spectrum/units.py#L1169
    
    ------
    Input
    ------
    
    wls : array, list, float, or int
        Input wls in Angstroms
        
    restwl : float or int
        Rest wavelength in Angstroms
       
    ------
    Output
    ------
    
    vels : velocities in km/s
    
    """
    
    c_ms = 3.0*10**8
    restwl_m = restwl*(1e-10)  # Angstroms to m
    wls_m = wls*(1e-10)  # Angstroms to m
    restfreq_hz = c_ms / restwl_m  # center frequency
    freqs_hz = c_ms / wls_m  # wavelength to frequency
    
    if convention == 'optical':
        vels_ms = (freqs_hz - restfreq_hz ) / freqs_hz * c_ms * -1
    elif convention == 'radio':
        vels_ms = (freqs_hz - restfreq_hz ) / restfreq_hz * c_ms * -1
    elif convention == 'relativistic':
        vels_ms = (freqs_hz**2 - restfreq_hz**2 ) / (restfreq_hz**2 + freqs_hz )**2 * c_ms * -1
    else:
        raise ValueError('Choose a convention: optical, radio, or relativistic.')
    
    vels_kms = vels_ms/(1e3)  # m/s to km/s
    
    return vels_kms
