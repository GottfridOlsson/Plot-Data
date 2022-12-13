##====================================================##
##     Project: PLOT DATA
##        File: heatmap.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17
##     Updated: 2022-12-13
##       About: Plot data in heatmap / colormap.
##              NOT IMPLEMENTED YET
##              here is an example of how to use it.
##====================================================##

import functions as f
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#data = np.genfromtxt() # --> matrix

z_lim_min = 0
z_lim_max = 100

f.set_LaTeX_and_CMU(True)
cols=10
rows=10
fig, ax = plt.subplots(figsize=(f.cm_2_inch(16), f.cm_2_inch(10)))
z = np.arange(rows * cols).reshape(rows, cols)
x = np.arange(cols)
y = np.arange(rows)

shading_index = 1
shadings = ["nearest", "gouraud"]
cbar_ax = ax.pcolormesh(x, y, z, shading=shadings[shading_index], vmin=z_lim_min, vmax=z_lim_max, cmap="turbo") #shading='gouraud'  ## https://matplotlib.org/stable/tutorials/colors/colormaps.html
colorbar = fig.colorbar(cbar_ax, ax=ax, label="Temperature $T$ (K)")#, ticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

f.set_axis_labels(ax, "$x$ label", "$y$ label", axNum=None)
f.set_layout_tight(fig)
f.export_figure_as_pdf("PDF/test_heatmap.pdf")
plt.show()