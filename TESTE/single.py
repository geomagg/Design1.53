import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 8))

ax.set_title('SHOOTING DIAGRAM  ------    SINGLE  SOURCE ')

ddx = 12.5              # Lateral distance between two array centers
pop = 12.5             # In line poop interval
xshot = 1.*pop        # Shot Point Interval
yshot = ddx           # Yshot = ddx 
xsail = ddx         # Sail Line Interval

# Plot parameters
nshots = 12
xmax = xsail*nshots        # Plot X max length
ymax = xshot*nshots-pop    # Plot Y max length
ymin = pop/4
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
#---------------------------------------------------------
#plt.text(795, 560,"Sail line space = ", size=9, rotation=0.,
#         ha="center", va="center",bbox=dict(boxstyle="round",
#                   ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8)))

#plt.text(640, 200, "Pop interval: 20 m", size=9, rotation=90.,
#         ha="center", va="center",bbox=dict(boxstyle="round",
#                   ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8)))
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
     ax.scatter(j*xsail+Shotx,Shoty+i*xshot+pop,s=40,c="blue",alpha=.8 )
######------------------------------------------------------------------------------------
Liney=[0,ymax-xshot]
Linex=np.array([xsail,xsail])
for j in range(nn): 
  ax.plot(Linex, Liney, color='blue', alpha=0.9,linestyle='dashed',
  linewidth=2, solid_capstyle='round', zorder=1, marker="^")
  Linex=Linex + xsail

plt.show()
