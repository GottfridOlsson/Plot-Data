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
filename_csv = 'TRA280_coin-cell-lab_waveform-data_formatted.csv' 
filename_pdf = 'TRA280_coin-cell-lab_LFP-Gr_V_vs_mAhg.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = CURRENT_PATH + "\\CSV\\" + filename_csv
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

waveform_data = CSV.read(CSV_path)
header = CSV.get_header(waveform_data)



# PLOT SETTINGS #
A4_paper_width_cm = 21
margins_in_Latex_cm = 2*2.8
fig_width_cm = A4_paper_width_cm - margins_in_Latex_cm
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = "Specific capacity / $\\mathrm{mAh}\\,\\mathrm{g}^{-1}$"
y_label = "Cell voltage / $\\mathrm{V}$"

x_lim = [-2, 67] #[np.min(x_data), np.max(x_data)]
y_lim = [2.4, 3.9] #[np.min(y_data), np.max(y_data)]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting


area_cm2 = 0.7854 # cm2
volume_cell = 1.0 # cm3
mass_cell = 3.64 # g
    
# from data sheet of LFP
areal_capacity_LFP = 1.0 # mAh / cm2
specific_capacity_LFP = 150 # mAh / g
m_LFP = areal_capacity_LFP*area_cm2/specific_capacity_LFP # (mAh / cm2) * (cm2) / (mAh / g) = g

cycle = 50
df = waveform_data.loc[waveform_data[header[0]]==cycle] # df.loc[df['column_name'].isin(some_values)]
df_cycle = df.loc[df[header[0]]==cycle]

current_cycle = df_cycle[header[3]].to_numpy() # mA
voltage_cycle = df_cycle[header[2]].to_numpy() # V
time_cycle    = df_cycle[header[7]].to_numpy() # minutes from start of cycle

current_charge = current_cycle[np.where(current_cycle > 0)]
voltage_charge = voltage_cycle[np.where(current_cycle > 0)]
time_charge    = time_cycle[np.where(current_cycle > 0)]

current_discharge = current_cycle[np.where(current_cycle < 0)]
voltage_discharge = voltage_cycle[np.where(current_cycle < 0)]
time_discharge    = time_cycle[np.where(current_cycle < 0)]

time_charge = time_charge/60 # minutes --> hours
time_discharge = time_discharge/60 # minutes --> hours


Q_charge = np.trapz(current_charge, time_charge) # mAh
Q_discharge = np.trapz(current_discharge, time_discharge) # mAh
E_charge = np.trapz(voltage_charge*current_charge, time_charge) # mAh*V = mWh
E_discharge = np.trapz(voltage_discharge*current_discharge, time_discharge) # mAh*V = mWh
P_charge = E_charge/(time_charge[-1] - time_charge[0])
P_discharge = E_discharge/(time_discharge[-1] - time_discharge[0])


print(f"\nDURING CHARGE CYCLE {cycle}")
print(f"Q: {Q_charge:.3f} mAh")
print(f"E: {E_charge:.3f} mWh")
print(f"P: {P_charge:.3f} mW\n")

print(f"DURING DISCHARGE CYCLE {cycle}")
print(f"Q: {Q_discharge:.3f} mAh")
print(f"E: {E_discharge:.3f} mWh")
print(f"P: {P_discharge:.3f} mW")
print(f"E/m: {E_discharge/mass_cell:.3f} mWh/g")
print(f"E/V: {E_discharge/volume_cell:.3f} mWh/cm3\n")

plt.plot(time_discharge, current_discharge, marker='o')
plt.plot(time_discharge, voltage_discharge, marker='^')
plt.show()
quit()



# PLOT # 

# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# FUNCTIONS #
cycles = [10, 15, 20, 30, 60]
colors = ['#6a4c93', '#1982c4', '#88c724', '#ffca3a', '#ff595e'] #['#e12729', '#f37324', '#f8cc1b', '#72b043', '#007f4e']

df = waveform_data.loc[waveform_data[header[0]].isin(cycles)] # df.loc[df['column_name'].isin(some_values)]

for i, cycle in enumerate(cycles):
    df_to_plot = df.loc[df[header[0]]==cycle]
    color = colors[i]

    # Select data
    cycle_numbers = df_to_plot[header[0]]
    capacity_cycle = df_to_plot[header[1]]
    cell_voltage = df_to_plot[header[2]]
    specific_capacity_cycle = capacity_cycle / m_LFP

    x_data = specific_capacity_cycle
    y_data = cell_voltage


    # Plot your data (axs.plot, .errorbar, .hist, ...)
    axs.plot(x_data, y_data, linewidth=1.35, linestyle='-', color=color, marker='', markersize='2.5', label=f"Cycle {cycle}")
#axs.plot(x_data, discharging_capacity, linewidth=1.5, linestyle='', color='r', marker='x', markersize='3', label='Discharging ($\\mathrm{mAh}\\,\\mathrm{g}^{-1}$)')


# Settings for each axis (axs)
f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='lower right')

#loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals determined by base
#axs.xaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
f.export_figure_as_pdf(PDF_path)
plt.show()