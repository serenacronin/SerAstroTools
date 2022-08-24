#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Aug 23 14:50:53 2022

@author: Serena A. Cronin

Functions that allow you to calculate the coefficients and vertex of a parabola.

"""

def calc_parabola_coeffs(x1, y1, x2, y2, x3, y3):
    
    '''
    Calculate the coefficients of a parabola.
    
    Adapted from: http://chris35wills.github.io/parabola_python/
    
    '''
    
    denom = (x1-x2) * (x1-x3) * (x2-x3)
    A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
    B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
    C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom
    
    return A, B, C


def calc_parabola_vertex(a, b, c):
    
    '''
    Calculate the vertex of a parabola given the coefficients A, B, and C.
    
    '''
    
    # get the coordinates of the vertex (h, k)
    h = -b / (2*a)
    k = c - b*b / (4*a)
    
    return h, k