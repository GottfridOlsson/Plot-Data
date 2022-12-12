##====================================================##
##     Project: PLOT DATA
##        File: errorbar.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17
##     Updated: 2022-12-12
##       About: Plot data with errorbars.
##====================================================##



## FUNCTIONS ##

def plot_errorbar(ax, data_x, data_y, errorbar_on, errorbar_x, errorbar_y, errorbar_size, errorbar_linewidth, errorbar_capthickness, data_label, line_color, line_style, line_width, marker_type, marker_size, marker_thickness, marker_facecolor, ax_num, ecolor=None):
    if errorbar_on:  
        out = ax.errorbar(data_x, data_y, label=data_label, color=line_color, linestyle=line_style, linewidth=line_width, \
            marker=marker_type, markersize=marker_size, markeredgewidth=marker_thickness, markerfacecolor=marker_facecolor, \
                xerr=errorbar_x, yerr=errorbar_y, elinewidth=errorbar_linewidth, capsize=errorbar_size, capthick=errorbar_capthickness, ecolor=ecolor)
        print("DONE: Plotted data with 'errorbar' on axs: " + str(ax_num))
    else:
        out = ax.plot(data_x, data_y, label=data_label, color=line_color, linestyle=line_style, linewidth=line_width, \
        marker=marker_type, markersize=marker_size, markeredgewidth=marker_thickness, markerfacecolor=marker_facecolor)
        print("DONE: Plotted data with 'errorbar' (without errorbars) on axs: " + str(ax_num))
    
    return out
