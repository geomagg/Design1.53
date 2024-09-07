
#def diagram(nfontes.get(),shotx.get(),shoty.get()),
#             velshot.get(),wd.get()):
def diagram(nsources,shotx,shoty,velshot,wd):



 import numpy as np
 import matplotlib.pyplot as plt

### nsources = nfontes.get()
 nfontes=nsources

#---------SINGLE SOURCE
#
 if nsources == 1:

  fig, ax = plt.subplots(figsize=(10, 8))
  ax.set_title('SHOOTING DIAGRAM  ------    SINGLE  SOURCE ')

  ddx = shoty              # Lateral distance between two array centers
  pop = shotx              # In line poop interval
  xshot = pop        # Shot Point Interval
  xsail = ddx         # Sail Line Interval
  yshot = ddx           # Yshot = ddx  

# Plot parameters
  nshots = 8
  xmax = xsail*nshots        # Plot X max length
  ymax = xshot*nshots-pop    # Plot Y max length
  ymin = 0
  nn = nshots -2                 # Number of shots to plot

# Major ticks every 20, minor ticks every 5
  major_ticksx = np.arange(0,xmax , xshot)
  minor_ticksx = np.arange(0,xmax, pop)
  major_ticksy = np.arange(0,ymax , xshot)
  minor_ticksy = np.arange(0,ymax, pop)

  ax.set_xticks(major_ticksx)
  ax.set_xticks(minor_ticksx, minor=True)
  ax.set_yticks(major_ticksy)
  ax.set_yticks(minor_ticksy, minor=True)

# And a corresponding grid
  ax.grid(which='both')

# Or if you want different settings for the grids:
  ax.grid(which='minor', alpha=0.4)
  ax.grid(which='major', alpha=0.8)

  factor = 1000./3600.
  knots = 1.852*factor   
  vell= velshot*knots
  extra=float(wd)/1500.
  ttime= round(float(pop/vell+extra),2)
  timel=str(ttime)
  binx=str(float(round(nfontes*shotx/2,2)))
  biny=str(float(round(yshot/2,2)))
  saill=str(float(shoty))
#  ESTOU NO BRANCH DIAGRAM
# MAI SUMA LINHA
  plt.text(6*xsail-xsail/5, xshot/6,"BinX x BinY : "+binx+" x "+biny+" m", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5), fc=(1.0, 0.9, 0.8)))

  plt.text(6*xsail-xsail/5, xshot/6+xshot/3, "Sail Line Interval: "+saill+" m", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),fc=(1.0, 0.9, 0.8)))

  plt.text(6*xsail-xsail/5, xshot/6+2*xshot/3, "Max Unblended time: "+timel+" s", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),fc=(1.0, 0.9, 0.8)))
#---------------------------------------------------------

# Vessels
  Shipx = np.arange(xsail,xmax,xsail)
  Shipy = np.empty([len(Shipx)])
  Shipy.fill(ymax-pop)
  ax.scatter(Shipx,Shipy,s=120,c="blue",alpha=.8,marker="^")
  Shoty = np.arange(100,ymax,100)
# Center Sources
  Shotx = np.empty([len(Shoty)])
  Shoty.fill(ymin)
  Shotx.fill(xsail)
  for j in range(len(Shipx)):
   for i in range(nn-1):
     ax.scatter(j*xsail+Shotx,Shoty+i*xshot+pop,s=60,c="blue",alpha=.8 )
######------------------------------------------------------------------------------------
  Liney=[0,ymax-xshot]
  Linex=np.array([xsail,xsail])
  for j in range(nn+1): 
    ax.plot(Linex, Liney, color='blue', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")
    Linex=Linex + xsail

 plt.show()



#-----DUAL SOURCE---------------------------------------------------------------------
 if nsources == 2:

   fig, ax = plt.subplots(figsize=(10, 8))
   ax.set_title('SHOOTING DIAGRAM  ------    DUAL  SOURCE ')

   ddx = shoty              # Lateral distance between two array centers
   pop = shotx              # In line poop interval
   xshot = 2*pop        # Shot Point Interval
   xsail = 2*ddx         # Sail Line Interval
   yshot = ddx           # Yshot = ddx  

# Plot parameters
   nshots = 6
   xmax = xsail*nshots        # Plot X max length
   ymax = xshot*nshots-pop    # Plot Y max length
   ymin = pop
   nn = nshots -1                 # Number of shots to plot

# Major ticks every 20, minor ticks every 5
   major_ticksx = np.arange(0,xmax , xshot)
   minor_ticksx = np.arange(0,xmax, pop)
   major_ticksy = np.arange(0,ymax , xshot)
   minor_ticksy = np.arange(0,ymax, pop)

   ax.set_xticks(major_ticksx)
   ax.set_xticks(minor_ticksx, minor=True)
   ax.set_yticks(major_ticksy)
   ax.set_yticks(minor_ticksy, minor=True)

# And a corresponding grid
   ax.grid(which='both')

# Or if you want different settings for the grids:
   ax.grid(which='minor', alpha=0.4)
   ax.grid(which='major', alpha=0.8)
#---------------------------------------------------------
   factor = 1000./3600.
   knots = 1.852*factor   
   vell= velshot*knots
   extra=float(wd)/1500.
   ttime= round(float(pop/vell+extra),2)
   timel=str(ttime)
   binx=str(float(round(nfontes*shotx/2,2)))
   biny=str(float(round(yshot/2,2)))
   saill=str(float(2*shoty))

   plt.text(5*xsail-xsail/5, xshot/5,"BinX x BinY : "+binx+" x "+biny+" m", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5), fc=(1.0, 0.9, 0.8)))

   plt.text(5*xsail-xsail/5, xshot/5+xshot/3, "Sail Line Interval: "+saill+" m", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),fc=(1.0, 0.9, 0.8)))

   plt.text(5*xsail-xsail/5, xshot/5+2*xshot/3, "Max Unblended time: "+timel+" s", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),fc=(1.0, 0.9, 0.8)))
# Vessels
   Shipx = np.arange(xsail,xmax,xsail)
   Shipy = np.empty([len(Shipx)])
   Shipy.fill(ymax-pop)
   ax.scatter(Shipx,Shipy,s=120,c="blue",alpha=.8,marker="^")
   Shoty = np.arange(100,ymax,100)
# Port Source
   Shotx = np.empty([len(Shoty)])
   Shoty.fill(ymin)
   Shotx.fill(xsail)
   for j in range(len(Shipx)):
    for i in range(nn-1):
     ax.scatter(j*xsail+Shotx-ddx/2,Shoty+i*xshot,s=40,c="red",alpha=.8 )
# SB Source
   Shoty = np.empty([len(Shoty)])
   Shoty.fill(ymin)
   Shotx.fill(xsail)
   for j in range(len(Shipx)):
    for i in range(nn-1):
     ax.scatter(j*xsail+Shotx+ddx/2,Shoty+i*xshot+pop,s=40,c="green",alpha=.8 )
######------------------------------------------------------------------------------------
   Liney=[0,ymax-xshot]
# Port Shooting line
   Linex=np.array([xsail,xsail])-ddx/2
   for j in range(nn): 
     ax.plot(Linex, Liney, color='red', alpha=0.9,linestyle='dashed',
     linewidth=2, solid_capstyle='round', zorder=1, marker="^")
     Linex=Linex + xsail
# Sail Shooting Line 
   Linex=np.array([xsail,xsail])
   for j in range(nn): 
    ax.plot(Linex, Liney, color='blue', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")
    Linex=Linex + xsail
# SB Shooting Line
   Linex=np.array([xsail,xsail])+ddx/2
   for j in range(nn): 
    ax.plot(Linex, Liney, color='green', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")
    Linex=Linex + xsail

   plt.show()

#--TRIPLE SOURCE--------------------------------------------------------------------------------
 if nsources == 3:

   fig, ax = plt.subplots(figsize=(10, 8))

   ax.set_title('SHOOTING DIAGRAM  ------    Triple  SOURCE ')

   ddx = shoty              # Lateral distance between two array centers
   pop = shotx              # In line poop interval
   xshot = 3.*pop        # Shot Point Interval
   yshot = ddx           # Yshot = ddx 
   xsail = 3*ddx         # Sail Line Interval

# Plot parameters
   nshots = 6
   xmax = xsail*nshots        # Plot X max length
   ymax = xshot*nshots-pop    # Plot Y max length
   ymin = pop
   nn = nshots -1                 # Number of shots to plot

# Major ticks every 20, minor ticks every 5
   major_ticksx = np.arange(0,xmax , xshot)
   minor_ticksx = np.arange(0,xmax, pop)
   major_ticksy = np.arange(0,ymax , xshot)
   minor_ticksy = np.arange(0,ymax, pop)

   ax.set_xticks(major_ticksx)
   ax.set_xticks(minor_ticksx, minor=True)
   ax.set_yticks(major_ticksy)
   ax.set_yticks(minor_ticksy, minor=True)

# And a corresponding grid
   ax.grid(which='both')

# Or if you want different settings for the grids:
   ax.grid(which='minor', alpha=0.4)
   ax.grid(which='major', alpha=0.8)
#---------------------------------------------------------
#  PORRA TRIPLE SOURCE
   factor = 1000./3600.
   knots = 1.852*factor   
   vell= velshot*knots
   ttime= float(round(pop/vell,2))
   timel=str(ttime)
   binx=str(float(round(nfontes*shotx/2,2)))
   biny=str(float(round(yshot/2,2)))
   saill=str(float(nfontes*shoty))

   plt.text(5*xsail-xsail/5, xshot/5,"BinX x BinY : "+binx+" x "+biny+" m", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5), fc=(1.0, 0.9, 0.8)))

   plt.text(5*xsail-xsail/5, xshot/5+xshot/3, "Sail Line Interval: "+saill+" m", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),fc=(1.0, 0.9, 0.8)))

   plt.text(5*xsail-xsail/5, xshot/5+2*xshot/3, "Max Unblended time: "+timel+" s", size=9, rotation=0.,
         ha="center", va="center",bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),fc=(1.0, 0.9, 0.8)))

# Vessels
   Shipx = np.arange(xsail,xmax,xsail)
   Shipy = np.empty([len(Shipx)])
   Shipy.fill(ymax-pop)
   ax.scatter(Shipx,Shipy,s=120,c="blue",alpha=.8,marker="^")
   Shoty = np.arange(100,ymax,100)
# Port Source
   Shotx = np.empty([len(Shoty)])
   Shoty.fill(ymin)
   Shotx.fill(xsail)
   for j in range(len(Shipx)):
    for i in range(nn-1):
     ax.scatter(j*xsail+Shotx-xshot,Shoty+i*xshot,s=40,c="red",alpha=.8 )
# Center Sources
   Shotx = np.empty([len(Shoty)])
   Shoty.fill(ymin)
   Shotx.fill(xsail)
   for j in range(len(Shipx)):
    for i in range(nn-1):
     ax.scatter(j*xsail+Shotx,Shoty+i*xshot+pop,s=40,c="blue",alpha=.8 )
# SB Source
   Shoty = np.empty([len(Shoty)])
   Shoty.fill(ymin)
   Shotx.fill(xsail)
   for j in range(len(Shipx)):
    for i in range(nn-1):
     ax.scatter(j*xsail+Shotx+xshot,Shoty+i*xshot+2*pop,s=40,c="green",alpha=.8 )
######------------------------------------------------------------------------------------
   Liney=[0,ymax-xshot]
# Port Shooting line
   Linex=np.array([xsail,xsail])-xshot
   for j in range(nn): 
    ax.plot(Linex, Liney, color='red', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")
    Linex=Linex + xsail
# Sail Shooting Line 
   Linex=np.array([xsail,xsail])
   for j in range(nn): 
    ax.plot(Linex, Liney, color='blue', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")
    Linex=Linex + xsail
# SB Shooting Line
   Linex=np.array([xsail,xsail])+xshot
   for j in range(nn): 
    ax.plot(Linex, Liney, color='green', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")
    Linex=Linex + xsail


   plt.show()

