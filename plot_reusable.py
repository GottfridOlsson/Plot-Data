##=====================================================================##
##     Project: PLOT DATA
##        File: plot_reusable.py
##      Author: GOTTFRID OLSSON 
##     Created: 2023-05-27
##     Updated: 2023-05-27
##       About: Plot data from CSV with matplotlib.
##              1. Read CSV
##              2. Do calculations (change this dependent on your case)
##              3. Plot x_data and y_data, change any settings you want
##=====================================================================##


# LIBRARIES #
import CSV_handler as CSV
import functions as f
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as plticker

# READ CSV #
# Change this:
filename_csv = 'TIF120_UHV-lab_QMS_formatted.csv' 
filename_pdf = 'TIF120_UHV-lab_QMS_formatted.pdf'

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
vlines_x = [1, 2, 16, 17, 18, 28, 40, 44] #Da
text_strings = ['H$^+$', 'H$_2^{+}$', 'O$_2^{2+}$', 'OH$^+$', 'H$_2$O$^+$', 'N$_2^+$', 'Ar$^+$', 'CO$_2^+$']

# PLOT SETTINGS #
x_lim = [-2, 47]#[np.min(x_data), np.max(x_data)]
y_lim = [-0.05, 1.2]#[np.min(y_data), np.max(y_data)]

f.set_LaTeX_and_CMU(True) #must be before plotting
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(16/2.54, 9/2.54), sharex=False, sharey=False)

# Plot
axs.plot(x_data, y_data, label='test', linewidth=1.5, linestyle='-', marker='', color='k')
axs.vlines(vlines_x, 0, 1.05, linestyles='-', color='k', linewidth=0.8)
for i in range(len(vlines_x)):  
    axs.text(vlines_x[i], 1.05, text_strings[i], rotation='vertical', horizontalalignment='left', verticalalignment='center', rotation_mode='anchor', backgroundcolor='w', fontsize=8)

# Settings for each axis
f.set_font_size(axis=13, tick=11, legend=9)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label="Dalton ($m/q$)", y_label="Normalized intensity")
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=True, grid_major_linewidth=0.7, grid_minor_on=False, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
f.set_legend(       axs, legend_on=False, alpha=1.0, location='best')


loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals
axs.xaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
f.export_figure_as_pdf(PDF_path)
plt.show()
















# Old functions