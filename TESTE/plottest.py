import numpy as np
import matplotlib.pyplot as plt

#def plot1():
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('SHOOTING DIAGRAM  ------    DUAL SOURCE ')
x1 = np.linspace(0, 1000, 1)
x2 = np.linspace(0, 1000, 1, endpoint=True)
ax.scatter(x1,x2,s=1,c="green",alpha=.01 )

plt.grid()


# Vessels
Shipx=[[150],[350],[550],[750],[950]]
Shipy=[[1000],[1000],[1000],[1000],[1000]]
ax.scatter(Shipx,Shipy,s=400,c="blue",alpha=.8,marker="^")

# Port and Stb Sources
pxx= np.array([200,400,600,800,1000])
Px=np.array([pxx,pxx,pxx,pxx,pxx,pxx,pxx])
Py=[[750,750,750,750,750],
    [650,650,650,650,650],
    [550,550,550,550,550],
    [450,450,450,450,450],
    [350,350,350,350,350],
    [250,250,250,250,250],
    [150,150,150,150,150]]

sxx = np.array([100,300,500,700,900])
Sx  = np.array([sxx,sxx,sxx,sxx,sxx,sxx,sxx])
Sy=[[800,800,800,800,800],
    [700,700,700,700,700],
    [600,600,600,600,600],
    [500,500,500,500,500],
    [400,400,400,400,400],
    [300,300,300,300,300],
    [200,200,200,200,200]]

ax.scatter(Px,Py,s=50,c="green",alpha=.8 )
ax.scatter(Sx,Sy,s=50,c="red",alpha=.8)

# Port Shooting line
y = np.transpose([[100,900],[100,900],[100,900],[100,900],[100,900]])
Lp1 =np.transpose( [[100,100],[300,300],[500,500],[700,700],[900,900]])
ax.plot(Lp1,y, color='red', alpha=0.9,linestyle='dotted',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")

# Starboard Shooting line
y1 = np.transpose([[100,900],[100,900],[100,900],[100,900],[100,900]])
Ls1 = np.transpose([[200,200],[400,400],[600,600],[800,800],[1000,1000]])
ax.plot(Ls1, y1, color='green', alpha=0.9,linestyle='dotted',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")

# Sail Line 
y3 = np.transpose([[100,1000],[100,1000],[100,1000],[100,1000],[100,1000]])
Vs1 = np.transpose([[150,150],[350,350],[550,550],[750,750],[950,950]])
ax.plot(Vs1, y3, color='blue', alpha=0.9,linestyle='dashed',
    linewidth=2, solid_capstyle='round', zorder=1, marker="^")

plt.show()
