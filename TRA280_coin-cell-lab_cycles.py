##======================================================================##
##     Project: PLOT DATA
##        File: TRA280_coin-cell-lab_cycles.py
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
filename_pdf = 'TRA280_coin-cell-lab_LFP-Gr_cycles.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = CURRENT_PATH + "\\CSV\\" + filename_csv
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

cycle_data = CSV.read(CSV_path)
cycle_data_header = CSV.get_header(cycle_data)


# FUNCTIONS #




# Select data
cycle_data = cycle_data[:-1] #drop last row (cycle 70 was not performed but cut short)
cycles = cycle_data[cycle_data_header[0]]
Coulombic_efficiency = cycle_data[cycle_data_header[1]]
charging_capacity = cycle_data[cycle_data_header[5]]
discharging_capacity = cycle_data[cycle_data_header[8]]
Energy_efficiency = cycle_data[cycle_data_header[2]]

area_cm2 = 0.7854

# from data sheet of LFP
areal_capacity_LFP = 1.0 # mAh / cm2
specific_capacity_LFP = 150 # mAH / g
m_LFP = areal_capacity_LFP*area_cm2/specific_capacity_LFP # mAh / cm2 * cm2 * g / mAh = g

charging_specific_capacity = charging_capacity / m_LFP
discharging_specific_capacity = discharging_capacity / m_LFP



# DATA ANLYSIS / CALCULATIONS #

avg_charging_specific_capacity = np.average(charging_specific_capacity[9:70])
avg_discharging_specific_capacity = np.average(discharging_specific_capacity[9:70])
avg_CE_cycles_10_to_69 = np.average(Coulombic_efficiency[9:70])
avg_EE_cycles_10_to_69 = np.average(Energy_efficiency[9:70])

print(f"\nAverage CE during cycle 10 through 69 is: {avg_CE_cycles_10_to_69:.3f} %")
print(f"Average EE during cycle 10 through 69 is: {avg_EE_cycles_10_to_69:.3f} %")
print(f"Average charging specific capacity during cycle 10 through 69 is: {avg_charging_specific_capacity:.3f} mAh / g")
print(f"Average discharging specific capacity during cycle 10 through 69 is: {avg_discharging_specific_capacity:.3f} mAh / g\n")




# PLOT SETTINGS #
A4_paper_width_cm = 21
margins_in_Latex_cm = 2*2.8
fig_width_cm = A4_paper_width_cm - margins_in_Latex_cm
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = "Cycle number"
y_label = "Specific capacity / $\\mathrm{mAh}\\,\\mathrm{g}^{-1}$"

x_lim = [-2.5, 72.5] #[np.min(cycles), np.max(cycles)]
y_lim = [0, 165]

grid_major = False
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting

colors = ['#6a4c93', '#1982c4', '#88c724', '#ffca3a', '#ff595e']




# PLOT # 

# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# Plot your data (axs.plot, .errorbar, .hist, ...)
axs.plot(cycles, charging_specific_capacity, linewidth=1.25, linestyle='-', color=colors[1], marker='o', markersize='2.8', label='Charging ($\\mathrm{mAh}\\,\\mathrm{g}^{-1}$)')
axs.plot(cycles, discharging_specific_capacity, linewidth=1.25, linestyle='-', color=colors[4], marker='x', markersize='3.3', label='Discharging ($\\mathrm{mAh}\\,\\mathrm{g}^{-1}$)')

ax2 = axs.twinx()  # instantiate a second axes that shares the same x-axis

ax2.plot(cycles, Coulombic_efficiency, linewidth=1.25, linestyle='-', color=colors[0], marker='^', markersize='3.3', label='Coulombic efficiency (\%)')
ax2.set_ylabel("Coulombic efficiency / $\%$")

# Settings for each axis (axs)
f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
#f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='center')

# get legend entries of both axis in the same legend (don't set legent as usual, why the above is commented out)
lines, labels = axs.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines2 + lines, labels2 + labels, loc='best', framealpha=1.0)

loc = plticker.MultipleLocator(base=25) # this locator puts ticks at regular intervals determined by base
axs.yaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
f.export_figure_as_pdf(PDF_path)
plt.show()