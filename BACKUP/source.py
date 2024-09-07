#--------------Class Source

class Source(object):

 def __init__(self,x,y,dx,ang,ort):
  import math
  import numpy as np

  self.ort=ort
  self.x=x
  self.y=y
  self.ang=ang
  self.dx=dx
  
  ang1 = self.ang*np.pi/180.

  if self.ort==0:
    self.deltax1=(dx/2)*-math.sin(ang1)
    self.deltay1=(dx/2)*math.cos(ang1)
    self.deltax2=(dx/2)*-math.sin(ang1)*-1
    self.deltay2=(dx/2)*math.cos(ang1)*-1

  else:
    self.deltay1=(dx/2)*math.sin(ang1)
    self.deltax1=(dx/2)*math.cos(ang1)
    self.deltay2=(dx/2)*math.sin(ang1)*-1
    self.deltax2=(dx/2)*math.cos(ang1)*-1

  self.sourcex=np.zeros(len(self.x))
  self.sourcey=np.zeros(len(self.y)) 
  k=0
  for i in range(0,len(self.x)):
     if (i%2) == 0:
      self.sourcex[k]=float(self.x[i])+self.deltax1
      self.sourcey[k]=float(self.y[i])+self.deltay1
     if (i%2) == 1 :
      self.sourcex[k]=float(self.x[i])+self.deltax2
      self.sourcey[k]=float(self.y[i])+self.deltay2
     k+=1
     
 def getsourcex(self):
      return self.sourcex
 def getsourcey(self):
      return self.sourcey

