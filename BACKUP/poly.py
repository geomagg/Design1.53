#---------------------Class Poly----------------------------------------
class Poly(object):

 def __init__(self,px,py,halo):

  import numpy as np
  import math  as m
  import matplotlib.pyplot as plt
  import csv
  from shapely.geometry import Point, Polygon
  from shapely.geometry.polygon import LinearRing, Polygon
  from shapely.geometry import MultiPoint

  self.px=px
  self.py=py
  self.halo=halo
  phi = np.zeros(len(self.px))
  p1x = np.zeros(len(self.px))
  p1y = np.zeros(len(self.px))
  p2x = np.zeros(len(self.px))
  p2y = np.zeros(len(self.px))
  self.pxe = np.zeros(len(self.px))
  self.pye = np.zeros(len(self.px))
  n=len(self.px)

  for i in range(1,n-1):
    phi[i]=m.atan2(float(self.py[i+1])-float(self.py[i]),float(self.px[i+1])-float(self.px[i]))
  phi[n-1]=m.atan2(float(self.py[1])-float(self.py[n-1]),float(self.px[1])-float(self.px[n-1]))
  phi[0]=phi[n-1]

  for i in range(1,n):
      p1x[i]=float(self.px[i])-m.sin(phi[i-1])*halo
      p1y[i]=float(self.py[i])+m.cos(phi[i-1])*halo
  p1x[0]=p1x[n-1]
  p1y[0]=p1y[n-1]

  for i in range(1,n-1):
    p2x[i]=(-p1x[i]*m.tan(phi[i-1])+p1x[i+1]*m.tan(phi[i])+p1y[i]-p1y[i+1])
    p2x[i]=p2x[i]/(m.tan(phi[i])-m.tan(phi[i-1]))
    p2y[i]=(-p1x[i]*m.tan(phi[i-1])*m.tan(phi[i])+
              p1x[i+1]*m.tan(phi[i-1])*m.tan(phi[i])
             -p1y[i+1]*m.tan(phi[i-1])+p1y[i]*m.tan(phi[i]))
    p2y[i]= p2y[i]/(m.tan(phi[i])-m.tan(phi[i-1]))
    
    self.pxe[i]=p2x[i]
    self.pye[i]=p2y[i]


  p2x[n-1]=(-p1x[n-1]*m.tan(phi[n-2])
             +p1x[1]*m.tan(phi[n-1])
             +p1y[n-1]-p1y[1])
  p2x[n-1]=p2x[n-1]/(m.tan(phi[n-1])-m.tan(phi[n-2]))
  p2y[n-1]=(-p1x[n-1]*m.tan(phi[n-2])*m.tan(phi[n-1])
            +p1x[1]*m.tan(phi[n-2])*m.tan(phi[n-1])
            -p1y[1]*m.tan(phi[n-2])+p1y[n-1]*m.tan(phi[n-1]))
  p2y[n-1]=p2y[n-1]/(m.tan(phi[n-1])-m.tan(phi[n-2]))

  self.pxe[n-1]=p2x[n-1]
  self.pye[n-1]=p2y[n-1]

  p2x[0]=p2x[n-1]
  self.pxe[0]=p2x[0]
  p2y[0]=p2y[n-1]
  self.pye[0]=p2y[0]

 def getpxe(self):
      return self.pxe
 def getpye(self):
      return self.pye
