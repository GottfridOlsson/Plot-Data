##====================================================##
##     Project: PLOT DATA
##        File: main.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17
##     Updated: 2022-12-28
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
import numpy as np # for ceiling



#------------#
#    MAIN    #
#------------#  


def main():
    print("\n===== PLOT DATA: Plot (start) =====")

    ## READ CSV ##
    CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
    CSV_path = CURRENT_PATH + "//" + JSON.filepath_csv
    PDF_path = CURRENT_PATH + "//" + JSON.filepath_pdf

    CSV_data   = CSV.read(CSV_path)
    CSV_header = CSV.get_header(CSV_data)


    ## CREATTE fig AND axs WITH FORMATTING ##
    f.set_LaTeX_and_CMU(JSON.LaTeX_and_CMU) # needs to run before "fig, axs = [...]" to parse LaTeX correctly
    f.set_font_size(JSON.font_size_axis, JSON.font_size_tick, JSON.font_size_legend)

    # implemented share_x and share_y 2022-11-25
    fig, axs = plt.subplots(JSON.subplot_setup_rows, JSON.subplot_setup_columns, figsize=(f.cm_2_inch(JSON.figure_width), f.cm_2_inch(JSON.figure_height)), sharex=JSON.subplot_setup_share_x, sharey=JSON.subplot_setup_share_y)


    #TODO: different sized subplots? ; https://www.statology.org/subplot-size-matplotlib/
  

    ## SELECT axs_ij FROM axs DEPENDING ON ROWS/COLS ##
    for i in range(JSON.subplot_setup_subplots): # forall subplots; subplot_i = i

        axs_ij = get_axs_ij(axs, i, JSON.subplot_setup_rows, JSON.subplot_setup_columns, JSON.subplot_setup_subplots)
      
        ## PLOT ##
        for k in range(len(JSON.plot_type[i])):  # forall types of plots in each subplot

            
            ## PLOT IN A CERTAIN TYPE OF PLOT ##

            # ERRORBAR #
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
                    JSON.marker_type[i][k], JSON.marker_size[i][k], JSON.marker_thickness[i][k], JSON.marker_facecolor[i][k], i, JSON.errorbar_color[i][k], JSON.errorbar_alpha[i][k]
                    )
                

                

            # HEATMAP #
            # if JSON.heatmap_on[i][k]:
                #...
            #                

            ## HERE GOES OTHER 'plot_types' ##
            #if JSON.plot_type[i] == "blahblah"
                # ...


            else:
                print("ERROR: keyword 'plot_type' = " + str(JSON.plot_type[i][k]) + " is not yet implemented. Sorry for the inconvenience.")


        ## SET AXIS, GRID, LEGEND, DECIMAL PRECISION ##
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
        

        #plt.axis('square') #works for last subplot
        #axs_ij.set_aspect('equal', adjustable="datalim")

        # TEST TO SET AXIS IN SUBPLOT TO A RATIO #
        #define y-unit to x-unit ratio
        #ratio = 1.0

        #get x and y limits
        #x_left, x_right = axs_ij.get_xlim()
        #y_low, y_high = axs_ij.get_ylim()

        #set aspect ratio
        #axs_ij.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio) #somehow doesnt work...
                    
    
    ## SET NICE LAYOUT AND EXPORT ##
    #plt.axis('square') #makes only last subplot square /comment out or in depeinding on case. should fix this some time //2022-11-25
    f.set_title(JSON.figure_title)
    f.align_labels(fig)
    f.set_layout_tight(fig)
    f.export_figure_as_pdf(PDF_path)
    #if JSON.subplot_axis_ratio_square_axis: #implemented 2022-22-25 //not yet
    
    

    print("===== PLOT DATA: Plot (end) =====")  
    #plt.show()



def get_axs_ij(axs, subplot_i, rows, cols, total_number_of_subplots):
    if total_number_of_subplots == 1:
        return axs 
    else:
        if rows == 1 or cols == 1:  #the if-case above catches the case where both are ==1, ensuring here that only one of these are == 1
            return axs[subplot_i] # subplot being only rows/cols, it has shape 1xN or shape Nx1, but axs has shape 1xN in either case
        else:
            row_i = int(np.floor(subplot_i / cols)) #floor since we want index (otherwise we could have done ciel and then - 1)
            col_i = subplot_i % cols
            return axs[row_i][col_i] #this is the last case, where subplots are shape rows x cols


if __name__ == "__main__":
    main()


## EOF ##