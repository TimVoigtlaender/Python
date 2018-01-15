# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:57:01 2018

@author: Tim Voigtländer
"""
import numpy as np

sp1= np.loadtxt('sample1.dat',dtype=float)
sp2= np.loadtxt('sample2.dat',dtype=float)
sp = list(set().union(sp1,sp2))

def d(data1, data2):    
    n1=len(data1)
    n2=len(data2)
    m1=np.mean(data1)
    m2=np.mean(data2)
    s1=np.std(data1)
    s2=np.std(data2)
    return abs(m1-m2)/(np.sqrt(s1**2/n1+s2**2/n2))

d0 = d(sp1,sp2)

niter=10000   # draw <niter> samples
di =  []
for i in range(niter):
    dii=d(np.random.choice(sp, size=len(sp1)),np.random.choice(sp, size=len(sp2)))
    di.append(dii) 
di = np.array(di)

counter=0

for i in range(len(di)):
    if di[i]>d0:
        counter +=1
        
        
print(counter/len(di))