# script nlLExample.py
''' example of negative Log Likelihood
         for Poisson distribution
.. author:: Guenter Quast <g.quast@kit.edu>

'''

import sys, numpy as np, matplotlib.pyplot as plt, scipy.special as sp
# ------------------------------------------------------

# ---- define some distributions ------
def fBinomial(x, p, n):
#Binomial distribution
  k=np.round(x)
  return sp.binom(n,k) * p**k * (1.-p)**(n-k)

def fPoisson(x, lam):
# Poisson distribution
  k=np.round(x)
  return (lam**k)/np.exp(lam)/sp.gamma(k+1.)

def fGauss(x, mu=0., sigma=1.):
# Gauss distribution
    return (np.exp(-(x-mu)**2/2./sigma**2)/np.sqrt(2.*np.pi)/sigma)

# ---- end distributions ------

def negLogL(p, f, x, *args, **kwargs):
# calulate neg logl L for lists of 
#   - parameters p_i and 
#   - observations x_i
#  for a pdf f(x, p, <other parameters>)
# ------------------------------------  
  nlL=np.zeros(len(p))
  for i, p_i in enumerate(p):
    nlL[i]=np.sum(-np.log(f(x, p_i, *args, **kwargs) ) )
  return nlL
  
# ---------------------------------------------------------------
##### ---- main Program starts here -----
if __name__ == "__main__":

  print( '*==* script ' + sys.argv[0]+ ' executing \n'),\

# get a random sample
  Ns=9      # sample size               
  lam=3.   
  m= np.loadtxt('Poisson.dat',dtype=float)  # ex: draw Poisson numbers
  
  # plot sample
  figd = plt.figure(figsize=(5.,5.) )
  axd = figd.add_subplot( 1, 1, 1)
  xmx=-1
  xmn=10
  x = np.linspace(xmn, xmx, 100)
  mxy = fPoisson(lam,lam)*1.1
  axd.set_ylim(0., mxy)
  axd.plot(x, fPoisson(x,lam), 'r-', label='Normalverteilung')   
#     make plot nicer:
  axd.set_xlabel('m') # axis labels
  axd.set_ylabel('Dichte')
  axd.plot(m, np.ones(len(m))*0.1*mxy, 'b|', 
          markersize=40, alpha=0.5, label='Stichprobenwerte')
  plt.legend(loc='best')
  
  
# set parameter range to be considered:
  pmin, pmax = max(0.001, lam-3.*np.sqrt(lam)), lam+3.*np.sqrt(lam) 
  parname=r'$\lambda$'
  name = "negLogL Poisson"

# construct a subplot array, max. 5*5
  npl=np.int32(np.sqrt(Ns))
  npl=min(npl,25)
  fig, axarr = plt.subplots(npl, npl, figsize=(3. * npl, 3.1 * npl))
  fig.canvas.set_window_title(name)

#
# plot likelihood function for 1, ..., Ns measurements  
  nppoints=150  # number of points for plot of parameter dependence
  p=np.linspace(pmin, pmax, nppoints, endpoint=True)
  print ('*==*: sample of random numbers \n', m) 
  i=0
  j=0
  for n in range(0, npl*npl): 
    axl=axarr[i,j]
    nL=negLogL(p, fPoisson, m[:n+1]) # first n measurements
    axl.plot(p, nL-min(nL), '-', color='steelblue', linewidth=3)
    axl.text(0.25, 0.9, 'n= %i'%(n+1), color='darkblue', 
          transform=axl.transAxes, size='medium')
    axl.set_ylim(0.,5.)
    if(i==(npl-1) and j==0):
      axl.set_xlabel(parname, size='x-large')
      axl.set_ylabel(r'$\Delta\, -{\rm ln}{\cal{L}}($'+parname+'$)$', 
                   size='large')
    j+=1
    if j==npl: 
      i+=1
      j=0
  
  idx_min = np.argmin(nL)
  mu_hat = p[idx_min]
  print ('Mimimum of Likelihood: %.4g'%mu_hat)
  print('Mean of Mesurements: %.4g'%m.mean())
  plt.show()