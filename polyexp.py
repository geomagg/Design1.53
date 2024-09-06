#---------------Cio Polyexp rounding-------------------------------------

class Polyexp(object):

 def __init__(self,px,py,halo):

  import numpy as np
  import math  as math

  self.X=px
  self.Y=py
  self.halo=halo
  phi = np.zeros(len(self.X))
  phi1 = np.zeros(len(self.X))
  A1 = np.zeros(len(self.X))
  pex,pey=[],[]

  self.N=len(self.X)

  phi[0] =math.atan2(self.Y[1]-self.Y[0],self.X[1]-self.X[0])
  phi1[0]=math.atan2(self.Y[self.N-2]-self.Y[0],self.X[self.N-2]-self.X[0])

  for  ij in range(1,self.N-1):
       phi1[ij]=math.atan2(self.Y[ij-1]-self.Y[ij],self.X[ij-1]-self.X[ij])
       phi[ij]=math.atan2(self.Y[ij+1]-self.Y[ij],self.X[ij+1]-self.X[ij])

# Find the concave vertices please
  halo1 =self.halo
  halo2 =self.halo

#  print 'N',self.N
  for i in range(0,self.N-1):
     concv=(self.X[i]-self.X[i-1])*(self.Y[i+1]-self.Y[i])-(self.X[i+1]-self.X[i])*(self.Y[i]-self.Y[i-1])
     if concv>0 :
      pex.append(self.X[i])
      pey.append(self.Y[i])
     else:
# Compute the distance to next and previous vertices
      if i==0:
         A1[i]=math.sqrt((self.Y[self.N-2]-self.Y[i])**2+(self.X[self.N-2]-self.X[i])**2)
      else:
         A1[i]=math.sqrt((self.Y[i-1]-self.Y[i])**2+(self.X[i-1]-self.X[i])**2)
         A1[i]=math.sqrt((self.Y[i+1]-self.Y[i])**2+(self.X[i+1]-self.X[i])**2)
      if A1[i]<self.halo:
         halo1=A1[i]
      if A1[i]<self.halo:
         halo2=A1[i]

#      Compute the new vertices  and Bezier

      pex.append(math.cos(phi1[i])*halo1/(math.tan ((phi[i]-phi1[i])/2))+self.X[i])
      pey.append(math.sin(phi1[i])*halo1/(math.tan ((phi[i]-phi1[i])/2))+self.Y[i])
      pex.append(math.cos(phi[i])*halo2/(math.tan ((phi[i]-phi1[i])/2))+self.X[i])
      pey.append(math.sin(phi[i])*halo2/(math.tan ((phi[i]-phi1[i])/2))+self.Y[i])
      halo1=self.halo
      halo2=self.halo

  pex.append(pex[0])
  pey.append(pey[0])
  self.ixn=len(pex)

  self.pp=pex
  self.qq=pey

 def getixn(self):
     return self.ixn
 def getpex(self):
     return self.pp
 def getpey(self):
     return self.qq
