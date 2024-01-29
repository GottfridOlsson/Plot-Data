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



# READ CSV #
# Change these:
filename_csv = 'testdata1.csv' 
filename_pdf = 'testdata1.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = CURRENT_PATH + "\\CSV\\" + filename_csv
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

CSV_data   = CSV.read(CSV_path)
CSV_header = CSV.get_header(CSV_data)



# FUNCTIONS #


# DATA ANLYSIS / CALCULATIONS #


# Select data
x_data = CSV_data[CSV_header[0]]
y_data = CSV_data[CSV_header[1]]
LSPR_peaks = x_data
concentrations = y_data
fit_x = CSV_data[CSV_header[2]]
fit_y = CSV_data[CSV_header[3]]
fit_y_oneSigma = CSV_data[CSV_header[4]]





# PLOT SETTINGS #
fig_width_cm = 16
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = "X-axis, example time $\\sigma$"
y_label = "Y-axis, example $f(\\sigma)$"

x_lim = [np.min(x_data), np.max(x_data)]
y_lim = [np.min(y_data), np.max(y_data)]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting






# PLOT # 

# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# Plot your data (axs.plot, .errorbar, .hist, ...)
axs.plot(x_data, y_data, linewidth=1.5, linestyle='', color='k', marker='o', markersize='4.5', label='Measured data')
axs.plot(fit_x, fit_y, color='k', linestyle='-', label='Linear fit')

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