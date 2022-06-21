##====================================================##
##     Project: PLOT DATA
##        File: main.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17, 10:56
##     Updated: 2022-06-21, 20:43
##       About: Plot data from CSV with matplotlib.
##              Plot-settings in JSON, export as PDF.
##====================================================##


#---------------#
#    IMPORTS    #
#---------------#

 #import json                             # to save/write to JSON
 #import pandas as pd                     # for CSV
import matplotlib.pyplot as plt         # to plot


import get_JSON_data as JSON
import CSV_handler as CSV
import functions as f

import errorbar



#------------#
#    MAIN    #
#------------#


if __name__ == "__main__":
    print("--- PLOT DATA Start ---")

    CSV_data   = CSV.read(JSON.filepath_csv)
    CSV_header = CSV.get_header(CSV_data)

    f.set_LaTeX_and_CMU(JSON.LaTeX_and_CMU) # needs to run before "fig, axs = [...]" to parse LaTeX correctly
    f.set_font_size(JSON.font_size_axis, JSON.font_size_tick, JSON.font_size_legend)

    fig, axs = plt.subplots(JSON.subplot_setup_rows, JSON.subplot_setup_columns, figsize=(f.cm_2_inch(JSON.figure_width), f.cm_2_inch(JSON.figure_height)))
      #TODO: different sized subplots? ; https://www.statology.org/subplot-size-matplotlib/


    for i in range(JSON.subplot_setup_subplots): # forall subplots
        for k in range(len(JSON.plot_type[i])):  # forall types of plots in each subplot

            if JSON.plot_type[i][k] == "errorbar":
                print("Plotting 'errorbar' on x: " + str(CSV_header[JSON.dataset_CSV_column_x[i][k]]) +", and y: "+ str(CSV_header[JSON.dataset_CSV_column_y[i][k]]))
                
                data_x     = CSV_data[CSV_header[JSON.dataset_CSV_column_x[i][k]]]
                data_y     = CSV_data[CSV_header[JSON.dataset_CSV_column_y[i][k]]]
                errorbar_x = CSV_data[CSV_header[JSON.errorbar_CSV_column_x[i][k]]]
                errorbar_y = CSV_data[CSV_header[JSON.errorbar_CSV_column_y[i][k]]]

                if JSON.errorbar_on[i][k] and JSON.errorbar_constant_on[i][k]:
                    errorbar_x = [JSON.errorbar_constant_x_pm[i][k] for x_pm in data_x]
                    errorbar_y = [JSON.errorbar_constant_y_pm[i][k] for y_pm in data_y]

                errorbar.plot_errorbar(
                    axs[i], data_x, data_y, JSON.errorbar_on, errorbar_x, errorbar_y, \
                    JSON.errorbar_size[i][k], JSON.errorbar_linewidth[i][k], JSON.errorbar_capthickness[i][k], \
                    JSON.dataset_label[i][k], JSON.line_color[i][k], JSON.line_style[i][k], JSON.line_width[i][k], \
                    JSON.marker_type[i][k], JSON.marker_size[i][k], JSON.marker_thickness[i][k], JSON.marker_facecolor[i][k], i
                    )

            ## HERE GOES OTHER 'plot_types' ##
            #if JSON.plot_type[i] == "blahblah"
                # ...


            else:
                print("ERROR: keyword 'plot_type' = " + str(JSON.plot_type[i][k]) + " is not implemented (yet). Sorry for the inconvenience.")

        
        f.set_legend(       axs[i], JSON.legend_on[i],  JSON.legend_alpha[i], JSON.legend_location[i], i)
        f.set_grid(         axs[i], JSON.grid_major_on[i], JSON.grid_major_linewidth[i], JSON.grid_minor_on[i], JSON.grid_minor_linewidth[i], i)
        f.set_axis_labels(  axs[i], JSON.axis_x_label[i], JSON.axis_y_label[i], i)
        f.set_axis_scale(   axs[i], JSON.axis_x_scale[i], JSON.axis_y_scale[i], i)
        #f.set_comma_decimal_with_precision(axs[i], JSON.axis_x_float_precision[i], JSON.axis_y_float_precision[i], i) # needs to run before "f.set_axis_scale" (if not, it messes up log-plots)
        f.set_axis_limits(  axs[i], JSON.axis_x_limit_min[i], JSON.axis_x_limit_max[i], JSON.axis_y_limit_min[i],JSON.axis_y_limit_max[i], i)


        # TODO: fix the bug where you can either have "axis_scale = log" OR use "set_comma_decimal_with_precision" as it is intended
        #       if you use both, there is a problem. Exponent "10^n" becomes "100[..]00" OR no decimals at all (at least not with comma)
        #  look at:  matplotlib.pyplot.ticklabel_format

        

        f.align_labels(fig)
        f.set_layout_tight(fig)
        f.export_figure_as_pdf(JSON.filepath_pdf)

    print("--- PLOT DATA End ---")      
    plt.show()









