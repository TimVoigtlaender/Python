#***************************************************************************
#* --------------------------------------------------------------------------
#* Solution to exercise ROOT Introduction
#* -> Plot a normalized Gaussian with mean = 5.0 and sigma = 1.5
#*    and its derivative and integral in the range of 0 to 10
#* --------------------------------------------------------------------------
#* adapted from initial version by Klaus Rabbertz
#*
#* modification log:
#* fc, 10.04.2013: Turn the code into Python + modifications
#* gq, Dec. 2013: small cosmetic modifications
#***************************************************************************/

from ROOT import TFile, TF1, TCanvas, TGraph
from math import sqrt, pi, exp


# Define new function ngauss with two parameters
def ngauss(x, par):  
    return 1./(par[1]*sqrt(2*pi))*exp(-1./2*((x[0]-par[0])/par[1])**2)



def PlotGauss():
  # Version 1
  # Create a new one-dimensional function myng1 in the limits 0 ... 10
  # with two parameters
  myng1 = TF1("myng1",ngauss,0,10,2)
  
  # Set the corresponding mean and sigma to 5.0 and 1.5
  myng1.SetParameter(0,5.)
  myng1.SetParameter(1,1.5)
  
  
  # Version 2
  # Create a new one-dimensional function myng2 in the limits 0 ... 10
  # with the two parameters [0] and [1] 
  myng2 = TF1("myng2","1./([1]*sqrt(2*pi))*exp(-1./2*((x-[0])/[1])**2)",0,10)

  # Set the corresponding mean and sigma to 5.0 and 1.5
  myng2.SetParameter(0,5.)
  myng2.SetParameter(1,1.5)
  
  
  # Create a new canvas
  c1 = TCanvas("c1","c1",2*700,2*500)
  c1.Divide(2,2)
  
  # Goto first pad and draw function version 1
  c1.cd(1)
  myng1.SetTitle("Normalverteilung Variante 1")
  myng1.Draw()
  
  # Goto second pad and draw function version 2
  c1.cd(2)
  myng2.SetTitle("Normalverteilung Variante 2")
  myng2.Draw()
  
  # Goto third pad and draw derivative of version 1
  c1.cd(3)
  myng2.DrawDerivative()
  
  # Goto fourth pad and draw integral of version 2
  c1.cd(4) 
  myng2.DrawIntegral()
  raw_input('Press <ret> to end -> ')

# Eventually, save wanted objects in a ROOT file ... 
#  hfile = TFile("fermi.root","RECREATE","fermi") # open file
#  c1.Write()    # write canvas
#  hfile.Close() # ... and close it.
  return

  #* Create a new ROOT binary machine independent file.
  #* Note that this file may contain any kind of ROOT objects, histograms,
  #* pictures, graphics objects, detector geometries, tracks, events, etc..
  #* But only histograms and trees are written by default.
  #* This file is now becoming the current directory.
 
  #myng1.Write()
  #myng2.Write()
  #f1.Close() # close file
 
##______________________________________________________________________________

PlotGauss()
  
