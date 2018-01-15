#***************************************************************************
#* --------------------------------------------------------------------------
#*    generation of arbitrary  probability density functions (PDFs)
#*    - transformation of uniform random numbers
#*    - accept-reject method
#*    - accept-reject with non-uniform random numbers (importance sampling) 
#*    - histogram method
#* --------------------------------------------------------------------------
#*  adapted from initial version by Klaus Rabbertz
#*
#* modification log:
#* fc, 11.04.2013: Turn the code into Python
#* gq, 04.01.2014: some cosmetics, added importance sampling, histogram method
#***************************************************************************/
from ROOT import TFile, TH1F, TCanvas, gRandom
import numpy as np
from math import sqrt, pi, tan

# example functions
#  (exercise a)
def f1(x):
    return 3./8*(1+x**2)

# Function to genericly implement the acceptance-rejection method. 
def AcceptReject (histo, f , p, xmin, xmax, t, NumRand,ymax):
    for i in range(0,NumRand):
        while True:
            u=np.random.rand()
            x=xmin+u*(xmax-xmin)
            v=np.random.rand()
            y=v*ymax
            if y<=f(x):
                histo.Fill(x)
                break
    return histo
  #* transform uniform random numbers to numbers following a distribution
  #* described by f
  #* Input variables: 
  #* histo  : ID of histogram to fill
  #* f      : function the random numbers should follow
  #* p      : function parameters
  #* xmin   : left border of interval
  #* xmax   : right border of interval
  #* t      : transform uniform random numbers to support "importance sampling"
  #* NumRand: number of random numbers to generate 
  #*/

                
##______________________________________________________________________________

#if __name__ == '__main__':
  
NumRand = 10000   # Number of random numbers to be filled


# ------------------------------------------------------------------------
# Exercise a
# Fill histogram h100 with 3/8(1+x^2) using acceptance/rejection method.
# Put the code for this exercise in function "AcceptReject".
h100 = TH1F("f1(x)","Histogram",100,-1,1)
h100 = AcceptReject (h100, f1 ,0, -1, 1, 0, NumRand,3./4)

# ------------------------------------------------------------------------
# Exercise b   Cauchy-distribution with transformation method
h200 = TH1F("f2(x)","Histogram",100,0,tan(1)*pi)
for i in range(0,NumRand):
    h200.Fill(tan(np.random.rand())*pi)

# ------------------------------------------------------------------------
# Exercise c: random sample following histogram
hdat= np.loadtxt('elefant.dat',dtype=float) # read histogram
# cumulative distribution
# ------------------------------------------------------------------------
# finally, draw everything
c = TCanvas("c","Canvas",0, 0, 800, 800);
c.Divide(2,2);
c.cd(1);

h100.DrawCopy();
c.cd(2);
h200.DrawCopy();
#c.cd(3);
#h300.DrawCopy();
c.Update();

# eventually, save results in a file
# create ROOT file.
#hfile = TFile("pdfs.root","RECREATE","pdfs")
# save desired histograms and close ROOT file.
#h100.Write()
#h200.Write()
#h300.Write()
#h400.Write()
#hfile.Close()

raw_input('Press <ret> to end -> ')
