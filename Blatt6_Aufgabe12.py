# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:35:33 2017

@author: Tim Voigtländer
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read columns from file:
if len(sys.argv)==2:
  infile=sys.argv[1]
else:
  infile='A12_data.txt'
#print('*==* script ' + sys.argv[0] +  ' reading from file ' + infile)

#read columns from file:
x, y =np.loadtxt(infile,unpack=True)
ye=[0.2]*len(x)

def poly1(x,  b=1.0, c=0.0):
    return  b * x + c 

par, cov = curve_fit( poly1, x, y, sigma=ye, absolute_sigma=True )
print("Fit parameters:\n", par)
print("Covariance matrix:\n", cov)

# plot fit result
xp = np.linspace( 0., 12., 100 )
ffit = poly1( xp, par[0], par[1] )
plt.errorbar( x, y, yerr=ye, fmt='o' )
plt.plot( xp, ffit, '-' )
plt.xlim( 0, 11 )
plt.ylim( 0, 8 )
plt.xlabel('x-Wert', size='x-large')
plt.ylabel('y-Wert', size='x-large')
plt.show()

chi2=0
for i in range (0,len(x)):
    chi2 +=(y[i]-poly1(x[i],b=par[0],c=par[1]))**2/(ye[i]**2)
print('Chi**2:\n[',chi2,']')