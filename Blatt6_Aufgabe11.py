# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:50:00 2017

@author: Tim Voigtländer
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

nw=10
nr=1000
p=1/2
k=np.zeros(nr)
k2=np.zeros(nw+1)
z=0
mw=0
v=0

for i in range(0,nr):
    tmp=0
    for j in range(0,nw):
       tmp += int(np.around(np.random.rand(nw)[j]))
    k[i]=tmp
    k2[int(tmp)] +=1
for i2 in range(0,nw+1):
    mw += k2[i2]*i2/nr
#    print(i2,"...",k2[i2])
for i3 in range(0,nr):
    v += (k[i3]-mw)**2/nr

plt.hist(k-.5,bins=[-.5,.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5])

def fBinomial(x,n,p):
  k=np.around(x)
  return sp.binom(n,k) * p**k * (1.-p)**(n-k)

x = np.linspace(0,nw+1,100)

mu=nw*p

plt.plot(x, nr*fBinomial(x,nw,p), 'r-')

plt.title("Binominalverteilter Münzwurf")
plt.xlabel('Summe der Kopf-Würfe bei '+ str(nw) +  ' würfen')
plt.ylabel('absolute Häufigkeit bei '+  str(nr) + ' Messreihen')

plt.show()

print(    "Mittelwert theoretisch:   ",mu,
        "\n           experimentell: ",mw,
      "\n\nVarianz    theoretisch:   ",mu*(1-p),
        "\n           experimentell: ",v)
    