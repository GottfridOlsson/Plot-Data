##======================================================================##
##     Project: PLOT DATA
##        File: plot_reusable.py
##      Author: GOTTFRID OLSSON 
##     Created: 2023-05-27
##     Updated: 2024-01-29
##       About: Plot data from CSV with matplotlib.
##              1. Read CSV
##              2. Do calculations (change this dependent on your case).
##              3. Plot x_data and y_data, change any settings you want.
##              4. Save a copy of the code in another place (ARCHIVE).
##======================================================================##



# LIBRARIES #
import CSV_handler as CSV
import functions as f
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as plticker
import pandas as pd


# READ CSV #
# Change these:
filename_csv = 'TRA280_coin-cell-lab_cycle-data_formatted.csv' 
filename_pdf = 'TRA280_coin-cell-lab_LFP-Gr_V_vs_mAhg.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = CURRENT_PATH + "\\CSV\\" + filename_csv
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

cycle_data = CSV.read(CSV_path)
cycle_data_header = CSV.get_header(cycle_data)


# FUNCTIONS #


# DATA ANLYSIS / CALCULATIONS #

print(cycle_data_header)
# Select data
cycles = cycle_data[cycle_data_header[0]]
Coulombic_efficiency = cycle_data[cycle_data_header[1]]
charging_capacity = cycle_data[cycle_data_header[5]]
discharging_capacity = cycle_data[cycle_data_header[8]]



# PLOT SETTINGS #
fig_width_cm = 16
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = "Specific capacity / $\\mathrm{mAh}\\,\\mathrm{g}^{-1}$"
y_label = "Cell voltage / $\\mathrm{V}$"

x_lim = [np.min(cycles), np.max(cycles)]
y_lim = [0, 5]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting






# PLOT # 

# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# Plot your data (axs.plot, .errorbar, .hist, ...)
axs.plot(cycles, charging_capacity, linewidth=1.5, linestyle='', color='k', marker='o', markersize='4.5', label='Charging')
axs.plot(cycles, discharging_capacity, linewidth=1.5, linestyle='', color='k', marker='o', markersize='4.5', label='Discharging')
axs.plot(cycles, Coulombic_efficiency, linewidth=1.5, linestyle='', color='k', marker='o', markersize='4.5', label='Coulombic efficiency')


# Settings for each axis (axs)
f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='best')

#loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals determined by base
#axs.xaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
f.export_figure_as_pdf(PDF_path)
plt.show()