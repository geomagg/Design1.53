#-----------------------------Class grid--------------------

class Grid(object):

 import numpy as np
 import math

 def __init__(self,x0,y0,dx,dy,nx,ny,angle,angle1,stagger,ort):

  import numpy as np
  import math
  import matplotlib.pyplot as plt

  self.ort=ort
  self.x0=x0
  self.y0=y0
  self.dx=dx
  self.dy=dy
  self.nx=nx
  self.ny=ny
  self.angle=angle
  self.angle1=angle1
  self.stag=stagger
  ang = self.angle*np.pi/180.
  ang1 = self.angle1*np.pi/180.

  if self.ort==1:
    ydx=self.dy*math.cos(ang);
    ydy=self.dy*math.sin(ang);
    xdx=self.dx*-math.sin(ang1);
    xdy=self.dx*math.cos(ang1);
  else:
    xdx=self.dx*math.cos(ang);
    xdy=self.dx*math.sin(ang);
    ydx=self.dy*-math.sin(ang1);
    ydy=self.dy*math.cos(ang1);

  self.gridx=[]
  self.gridy=[]

  for j in range(0,self.ny):
   self.gridx.append([])
   self.gridy.append([])
   for i in range (0,self.nx): 
      if j%2 == 0:
       extrax=self.stag*(xdx/2)
       extray=self.stag*(xdy/2)
      else:
       extrax=0
       extray=0
      xx=self.x0+(i)*xdx +extrax
      yy=self.y0+(i)*xdy +extray
      self.gridx[j].append(xx)
      self.gridy[j].append(yy)
   self.x0+=ydx
   self.y0+=ydy

  self.xx = np.array(self.gridx)
  self.yy = np.array(self.gridy)

  self.nnx = np.size(self.xx,1)
  self.nny = np.size(self.yy,0)

 def getarrx(self):
      return self.xx
 def getarry(self):
      return self.yy
 def getnnx(self):
      return self.nnx
 def getnny(self):
      return self.nny
