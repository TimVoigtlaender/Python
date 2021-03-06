# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:19:19 2018

@author: Tim Voigtländer
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

# Definiere Funktionen
def f(x, tw):
    return np.exp(-x/tw)/tw

def transf(x,tw):
    return -tw*np.log(1-x)

def dttot(dt):
    long = len(dt)
    tmp = [dt[0]]
    for i in range (1,long):
        tmp = np.append(tmp,tmp[len(tmp)-1]+dt[i])
    return tmp

def ttodt(t):
    long = len(t)
    tmp = [t[0]]
    for i in range (1,long):
        tmp = np.append(tmp,t[i]-t[i-1])
    return tmp

def fPoisson(x, lam):
  return (lam**x)/np.exp(lam)/sp.gamma(x+1.)

def detektor(ti,t):
    if t-ti<0.2:
        if np.random.rand()<5.*(t-ti):
            return t
        else:
            return -1
    else:
        return t

# Startwerte
nzahl = 50000
bzahl = 500
xmin = 0
xmax = 4
twn = 1
twr = 10

# Erzeuge Zeitpunkte
wzn = transf(np.random.rand(nzahl),twn)
tdata = dttot(wzn)
tmin = tdata[0]
tmax = tdata[len(tdata)-1]
x1 = np.linspace(xmin,xmax,(xmax-xmin)*10)
x2 = np.linspace(tmin,tmax)

# Erzeuge Rauschen ab tmin
trdata = [transf(np.random.rand(),twr)]
while trdata[0]<tdata[0]:
    trdata[0] = [transf(np.random.rand(),twr)]

# bis tmax
merke = transf(np.random.rand(),twr)
while trdata[len(trdata)-1]+merke<tmax:
    trdata = np.append(trdata,trdata[len(trdata)-1]+merke)
    merke = transf(np.random.rand(),twr)

# Kombiniere Zeiten 
talle = np.sort(np.append(tdata,trdata))

# Erzeuge dt
dtalle = ttodt(talle)

# Erzeugen der detektierten Werte
tlast = -1
tdetektor = [talle[0]]
for i in range(1,len(talle)):
    temporar = detektor(tlast,talle[i])
    if temporar>0:
        tdetektor = np.append(tdetektor,temporar)
        tlast = temporar
    
#Plotten der Graphen
        
#a)
fig, axa = plt.subplots(1)
axa.set_xlim(xmin,xmax)
axa.plot(x1,f(x1,twn),'b-')
axa.hist(wzn, normed=True, bins=100)

#b)
fig, axb = plt.subplots(1)
axb.set_xlim(xmin,xmax)
axb.plot(x1,f(x1,1/(1/twn+1/twr)),'r-')
axb.plot(x1,f(x1,twn),'b--')
axb.hist(dtalle, normed=True, bins=100)

#c)
fig, axc = plt.subplots(1)
axc.set_xlim(tmin,tmax)
wertt, bint, patchest = axc.hist(talle, bins=bzahl)
wertn, binn, patchesn = axc.hist(tdata, bins=bzahl)
wertr, binr, patchesr = axc.hist(trdata, bins=bzahl)
#wertd, bint, patchest = axc.hist(tdetektor, bins=bzahl)
axc.axhline(y=np.mean(wertt), color='b')
axc.axhline(y=np.mean(wertn), color='orange')
axc.axhline(y=np.mean(wertr), color='g')
#axc.axhline(y=np.mean(wertd), color='r')

#d)
fig, axd = plt.subplots(1)
x3 = np.linspace(np.amin(wertt),np.amax(wertt))
axd.set_xlim(np.amin(wertt),np.amax(wertt))
#axd.hist(wertd,normed=True, bins=20,color='g')
axd.hist(wertt,normed=True, bins=20)
axd.plot(x3,fPoisson(x3,np.mean(wertt)),'r-')
#axd.plot(x3,fPoisson(x3,np.mean(wertd)),'b--')
plt.show()

# e)
print('Ereignisrate ohne Detektor: %.4g Ereignisse pro ZE' %float(len(talle)/(tmax-tmin)))
print('Ereignisrate mit Detektor: %.4g Ereignisse pro ZE'%float(len(tdetektor)/(tmax-tmin)))
print('Der Korrekturfaktor ist somit %.4g' %float(len(talle)/len(tdetektor)))