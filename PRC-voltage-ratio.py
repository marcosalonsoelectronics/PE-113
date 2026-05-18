# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:46:11 2026

@author: jmarc
"""

from math import pi, sqrt

L=36e-6; C=470e-9; Re=19.4
fs=41.6e3; ws= 2*pi*fs
Vg=10

M= (8/pi**2)*(Re/(ws*C)) / sqrt( (L/C)**2 + \
                              
    Re**2*(ws*L - 1/(ws*C) )**2 )
    
print("M= ", M) 

print("Vo= ", M*Vg)   