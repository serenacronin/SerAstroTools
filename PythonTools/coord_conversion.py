#!/usr/bin/env python
# coding: utf-8


def ra_to_degrees(ra_time):
    """ Input:  RA in hrs:mins:secs
        Output: RA in degrees
    """
    ra_time = ra_time
    ra_time = ra_time.split(':')
    hours   = float(ra_time[0])
    mins    = float(ra_time[1])
    
    # if some are already in degrees
    try:
        arcmins = float(ra_time[1])
    except:
        arcmins = 0.0
    
    # if some already have the secs converted to decimal
    try:
        secs = float(ra_time[2])
    except:
        secs = 0.0
    
    time_in_hours = hours + mins/60.0 + secs/3600.0
    ra_in_degrees = time_in_hours*15.0
    
    return ra_in_degrees
        

def dec_to_degrees(dec_time):
    """ Input:  DEC in degree:arcmin:arcsec
        Output: DEC in degrees
    """
    dec_time  = dec_time.split(':')
    degs      = float(dec_time[0])
    
    # if some are already in decimal degrees
    try:
        arcmins = float(dec_time[1])
    except:
        arcmins = 0.0
    
    # if some already have the arcsecs converted to decimal
    try:
        arcsecs = float(dec_time[2])
    except:
        arcsecs = 0.0
    
                             # handle +/- degrees
    deg_in_degrees = abs(degs) + (arcmins/60.0) + (arcsecs/3600.0)
    
    # make the degrees negative if they were negative before
    if degs < 0:
        deg_in_degrees = np.negative(deg_in_degrees)
    
    return deg_in_degrees

