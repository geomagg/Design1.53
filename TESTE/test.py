import matplotlib.pyplot as plot
import numpy as np
from matplotlib.backend_tools import ToolBase, ToolToggleBase


#plot.rcParams['toolbar'] = 'None'
plot.rcParams['toolbar'] = 'toolmanager'

fig, ax = plot.subplots(figsize=(6, 4))

#fig.canvas.manager.toolmanager.remove_tool('zoom')

ax.set_title("Ricardo s square plot" )
plot.grid()
X=[10,30,30,10,10]
Y=[10,10,30,30,10]
ax.set_facecolor("blue")
plot.ylabel("Y", fontweight='bold')
plot.xlabel("X", fontweight='bold')
 
ax.plot(X, Y, color='red', alpha=0.9,
    linewidth=4, solid_capstyle='round', zorder=1)

plot.show()

