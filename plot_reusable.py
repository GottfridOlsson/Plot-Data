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


# READ CSV #
# Change this:
filename_csv = 'testdata1.csv' 
filename_pdf = 'testpdf1.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = CURRENT_PATH + "\\CSV\\" + filename_csv
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

CSV_data   = CSV.read(CSV_path)
CSV_header = CSV.get_header(CSV_data)



# FUNCTIONS #


# DATA ANLYSIS / CALCULATIONS #

# TODO




# Select data
x_data = [0, 1, 2, 3, 4, 5]
y_data = [x**2 for x in x_data]



# PLOT SETTINGS #
x_lim = [np.min(x_data), np.max(x_data)]
y_lim = [np.min(y_data), np.max(y_data)]

f.set_LaTeX_and_CMU(True) #must be before plotting
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(16/2.54, 9/2.54), sharex=False, sharey=False)

# Plot
axs.plot(x_data, y_data, label='test', linewidth=1.5, linestyle='-.', marker='s', color='r')


# Settings for each axis
f.set_font_size(axis=13, tick=11, legend=9)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label="x-axis", y_label="y-axis")
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=True, grid_major_linewidth=0.7, grid_minor_on=False, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
f.set_legend(       axs, legend_on=True, alpha=1.0, location='best')

f.align_labels(fig)
f.set_layout_tight(fig)
f.export_figure_as_pdf(PDF_path)
plt.show()
















# Old functions