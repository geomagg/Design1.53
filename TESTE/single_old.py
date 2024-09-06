def diagram(nsources):

 import numpy as np
 import matplotlib.pyplot as plt

 if nsources == 1:
  ddx=10000
  xmax = ddx*8
  xmin = 0

  fig, ax = plt.subplots(figsize=(8, 6))

  ax.set_title('SHOOTING DIAGRAM  ------    SINGLE SOURCE ')

# Major ticks every 20, minor ticks every 5

  xmajor_ticks = np.arange(0, xmax, int(ddx*2))
  xminor_ticks = np.arange(0, xmax, ddx)

##  ax.set_xticks(xmajor_ticks)
##  ax.set_xticks(xminor_ticks, minor=True)

#  ax.set_yticks(xmajor_ticks)
#  ax.set_yticks(xminor_ticks, minor=True)

# And a corresponding grid
#  ax.grid(which='both')

# Or if you want different settings for the grids:
  ax.grid(which='minor', alpha=0.2)
  ax.grid(which='major', alpha=0.5)

# Vessels

  Shipx = np.arange(ddx, xmax,ddx)
  Shipy = np.empty([len(Shipx)])
  Shipy.fill(xmax)
  ax.scatter(Shipx,Shipy,s=120,c="blue",alpha=.8,marker="^")

# Sources
##  dxshot=100
##  Shoty = np.arange(100, 900,100)
##  Shoty = np.empty([len(Shoty)])
##  Shoty.fill(200)
##  Shotx = Shipx
##  for i in range(7):
##     ax.scatter(Shotx,Shoty+(i*dxshot),s=60,c="black",alpha=.8 )

# Sail Line 
  Liney=[xmin,xmax]
  Linex=np.array([ddx,ddx])
  for j in range(int(xmax/ddx-1)):
   print (j,Linex)
   ax.plot(Linex, Liney, color='blue', alpha=0.9,linestyle='dashed',
     linewidth=2, solid_capstyle='round', zorder=1, marker="^")
   Linex=Linex + ddx

 plt.show()
diagram(1)
