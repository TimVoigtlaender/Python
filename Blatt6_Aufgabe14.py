# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

nw=100000
tmp = np.random.rand(nw)

x1 = np.linspace( 0., 1., 100 )
x2 = np.linspace( 1., np.exp(1), 100 )
x3 = np.linspace( 0, np.tan(1), 100 )
x4 = np.linspace( 0., np.log(2), 100 )

t1=tmp**2
t2=np.exp(tmp)
t3=np.tan(tmp)
t4=np.log(tmp+1.)


plt.figure(1,figsize=(16,12))

plt.subplot(221)
plt.title("t(r)=r²       g(r)=1/2*r^(-1/2)")
plt.xlim(0,1)
plt.hist(t1,normed=True)
plt.plot(x1, 1/(2*np.sqrt(x1)), 'r-')

plt.subplot(222)
plt.title("t(r)=exp(r)       g(r)=1/r")
plt.xlim(1,np.exp(1))
plt.hist(t2,normed=True)
plt.plot(x2, 1./x2 , 'r-')

plt.subplot(223)
plt.title("t(r)=tan(r)       g(r)=1/(1+r²)")
plt.xlim(0,np.tan(1))
plt.hist(t3,normed=True)
plt.plot(x3, 1./(x3**2+1.), 'r-')

plt.subplot(224)
plt.title("t(r)=log(1.+r)       g(r)=exp(r)")
plt.xlim(0,np.log(2))
plt.hist(t4,normed=True)
plt.plot(x4,np.exp(x4), 'r-')

plt.show()