
#---------------Polyarea ------------------------------------

class Polyarea(object):

 import math

 def __init__(self,xp,yp):

  self.xp=xp
  self.yp=yp
  dd=0
  ss=0
  for j in range(0,len(self.xp)-1):
     dd+=float(self.xp[j])*float(self.yp[j+1])
     ss+=float(self.xp[j+1])*float(self.yp[j])

  self.A=-(dd-ss)/2000000;

  if self.A > 0 :
   self.order = 'true'

 def getarea(self):
     return self.A
 def getorder(self):
      return self.order
