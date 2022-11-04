##====================================================##
##     Project: PLOT DATA
##        File: main.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17, 10:56
##     Updated: 2022-10-27, 09:56
##       About: Plot data from CSV with matplotlib.
##              Plot-settings in JSON, export as PDF.
##====================================================##


#---------------#
#    IMPORTS    #
#---------------#

import matplotlib.pyplot as plt         # to plot
import get_JSON_data as JSON
import CSV_handler as CSV
import functions as f
import errorbar
import os



#------------#
#    MAIN    #
#------------#


def main():
    print("===== PLOT DATA Start =====")

    CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
    CSV_path = CURRENT_PATH + "//" + JSON.filepath_csv
    PDF_path = CURRENT_PATH + "//" + JSON.filepath_pdf

    CSV_data   = CSV.read(CSV_path)
    CSV_header = CSV.get_header(CSV_data)

    f.set_LaTeX_and_CMU(JSON.LaTeX_and_CMU) # needs to run before "fig, axs = [...]" to parse LaTeX correctly
    f.set_font_size(JSON.font_size_axis, JSON.font_size_tick, JSON.font_size_legend)

    fig, axs = plt.subplots(JSON.subplot_setup_rows, JSON.subplot_setup_columns, figsize=(f.cm_2_inch(JSON.figure_width), f.cm_2_inch(JSON.figure_height)))
      #TODO: different sized subplots? ; https://www.statology.org/subplot-size-matplotlib/
  



    for i in range(JSON.subplot_setup_subplots): # forall subplots

        if JSON.subplot_setup_subplots == 1:
            axs_ij = axs     # necessary to avoid several for-loops (since object "AxesSubplot" is not subscriptable)
        else:

            if JSON.subplot_setup_columns == 1 and JSON.subplot_setup_rows >= 2:
                axs_ij = axs[i]
            else:
                if JSON.subplot_setup_rows < 2:
                    axs_ij = axs[i]
                else:
                    if i+1 <= JSON.subplot_setup_rows:
                        axs_ij = axs[0][i]
                    else:
                        if 1+i <= 2*JSON.subplot_setup_rows:
                            mod_i = i % JSON.subplot_setup_columns
                            axs_ij = axs[1][mod_i]
                        else:
                            if 1+i <= 3*JSON.subplot_setup_rows:
                                mod_i = i % JSON.subplot_setup_columns
                                axs_ij = axs[2][mod_i]
                            #and so on for higher orders of subplots.
                            # this is ugly - yes.
                            # this can be done with clever modulus calculations - yes.
                            # I'll eventually find an even better way of doing this - yes.
                            # but not today. //2022-10-27
                            # had to add an extra if if you wanted columns and not row - FIX THIS MESS! //2022-11-04
                


        for k in range(len(JSON.plot_type[i])):  # forall types of plots in each subplot

            if JSON.plot_type[i][k] == "errorbar":
                print("Plotting 'errorbar' on x: " + str(CSV_header[JSON.dataset_CSV_column_x[i][k]]) +", and y: "+ str(CSV_header[JSON.dataset_CSV_column_y[i][k]]) + " on axs: " + str(i))
                
                data_x = CSV_data[CSV_header[JSON.dataset_CSV_column_x[i][k]]]
                data_y = CSV_data[CSV_header[JSON.dataset_CSV_column_y[i][k]]]

                if JSON.errorbar_on[i][k]: #### TEST 2022-09-22, remove this and below if it fucks something up later on
                    if JSON.errorbar_CSV_column_x[i][k] == -1:
                        errorbar_x = None
                    else:
                        errorbar_x = CSV_data[CSV_header[JSON.errorbar_CSV_column_x[i][k]]]
                        
                    if JSON.errorbar_CSV_column_y[i][k] == -1:
                        errorbar_y = None
                    else:
                        errorbar_y = CSV_data[CSV_header[JSON.errorbar_CSV_column_y[i][k]]]
                        
                                    
                    if JSON.errorbar_on[i][k] and JSON.errorbar_constant_on[i][k]:
                        errorbar_x = [JSON.errorbar_constant_x_pm[i][k] for x_pm in data_x]
                        errorbar_y = [JSON.errorbar_constant_y_pm[i][k] for y_pm in data_y]
                
                else:#### TEST 2022-09-22, remove this and two rows below if it fucks something up later on
                        errorbar_x = [[0] for x in data_x]
                        errorbar_y = [[0] for x in data_y]
                        
             

                errorbar.plot_errorbar(
                    axs_ij, data_x, data_y, JSON.errorbar_on[i][k], errorbar_x, errorbar_y, \
                    JSON.errorbar_size[i][k], JSON.errorbar_linewidth[i][k], JSON.errorbar_capthickness[i][k], \
                    JSON.dataset_label[i][k], JSON.line_color[i][k], JSON.line_style[i][k], JSON.line_width[i][k], \
                    JSON.marker_type[i][k], JSON.marker_size[i][k], JSON.marker_thickness[i][k], JSON.marker_facecolor[i][k], i
                    )

            ## HERE GOES OTHER 'plot_types' ##
            #if JSON.plot_type[i] == "blahblah"
                # ...

            else:
                print("ERROR: keyword 'plot_type' = " + str(JSON.plot_type[i][k]) + " is not implemented (yet). Sorry for the inconvenience.")



        f.set_axis_scale(   axs_ij, JSON.axis_x_scale[i], JSON.axis_y_scale[i], i)
        f.set_axis_labels(  axs_ij, JSON.axis_x_label[i], JSON.axis_y_label[i], i)
        f.set_axis_invert(  axs_ij, JSON.axis_x_invert[i], JSON.axis_y_invert[i], i)
        f.set_axis_limits(  axs_ij, JSON.axis_x_limit_min[i], JSON.axis_x_limit_max[i], JSON.axis_y_limit_min[i],JSON.axis_y_limit_max[i], i)
  
        f.set_grid(         axs_ij, JSON.grid_major_on[i], JSON.grid_major_linewidth[i], JSON.grid_minor_on[i], JSON.grid_minor_linewidth[i], i) # set_grid must be after set_axis_scale for some reason (at least with 'log')
        f.set_legend(       axs_ij, JSON.legend_on[i], JSON.legend_alpha[i], JSON.legend_location[i], i)
        
        if JSON.commaDecimal:
            if JSON.axis_x_scale[i] != 'log':
                f.set_commaDecimal_with_precision_x_axis(axs_ij, JSON.axis_x_float_precision[i], i)
            if JSON.axis_y_scale[i] != 'log':
                f.set_commaDecimal_with_precision_y_axis(axs_ij, JSON.axis_y_float_precision[i], i)
        if JSON.pointDecimal:
            if JSON.axis_x_scale[i] != 'log':
                f.set_pointDecimal_with_precision_x_axis(axs_ij, JSON.axis_x_float_precision[i], i)
            if JSON.axis_y_scale[i] != 'log':
                f.set_pointDecimal_with_precision_y_axis(axs_ij, JSON.axis_y_float_precision[i], i)
                    
            
    f.set_title(JSON.figure_title)
    f.align_labels(fig)
    f.set_layout_tight(fig)
    f.export_figure_as_pdf(PDF_path)

    print("===== PLOT DATA End =====")      
    plt.show()



if __name__ == "__main__":
    main()


## EOF ##