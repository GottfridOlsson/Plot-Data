##====================================================##
##     Project: PLOT DATA
##        File: get_JSON_data.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17, 11:54
##     Updated: 2022-06-18, 19:09
##       About: Reads and stores standard settings if
##              not overwritten by user data in JSON
##====================================================##

# Q. that remains: 
# https://stackoverflow.com/questions/19993795/how-would-i-access-variables-from-one-class-to-another


import JSON_handler as JSON


##### TODO: fix this s.t. one gets a prompt and pop-up window from which user can select JSON-file

readJSONFilePathStringTEMP = "CONFIG"
JSON_readFilePath = "JSON/"+ readJSONFilePathStringTEMP + ".json" #make it such that you can ask for what file it is or smht//2022-02-18
J = JSON.read(JSON_readFilePath) #Jason-file



#--------------------#
# GET DATA FROM JSON #
#--------------------#

filename_csv            = J['filename']['csv']
filename_pdf            = J['filename']['pdf']

figure_height           = J['figure_size']['height_cm'] # [cm]
figure_width            = J['figure_size']['width_cm']  # [cm]
# textwidth_external    = J['figure_size']['textwidth'] # [cm]

font_size_axis          = J['font_size']['axis']   # [pt]
font_size_tick          = J['font_size']['tick']   # [pt]
font_size_legend        = J['font_size']['legend'] # [pt]
# font_size_external    = J['font_size']['external'] # [pt]

LaTeX_and_CMU           = J['LaTeX_and_CMU']

subplot_setup_x_cols    = J['subplot_setup']['x']
subplot_setup_y_cols    = J['subplot_setup']['y']
subplot_setup_subplots  = J['subplot_setup']['total_subplots'] #TODO: raise error if "total != x*y"


## DECLARE VARIABLE NAMES ##

subplots = range(subplot_setup_subplots)

subplot_num            = [i for i in subplots]
plot_type              = []

dataset_label          = []
dataset_col_x          = []
dataset_col_y          = []

line_color             = []
line_style             = []
line_width             = []

marker_type            = []
marker_size            = []
marker_thickness       = []
marker_facecolor       = []

errorbar_on            = []
errorbar_constant_on   = []
errorbar_constant_x_pm = []
errorbar_constant_y_pm = []
errorbar_x_col         = []
errorbar_y_col         = []
errorbar_size          = []
errorbar_linewidth     = []
errorbar_capthickness  = []

axis_x_label           = []
axis_x_limit_min       = []
axis_x_limit_max       = []
axis_x_scale           = []
axis_x_invert          = []
axis_x_float_precision = []

axis_y_label           = []
axis_y_limit_min       = []
axis_y_limit_max       = []
axis_y_scale           = []
axis_y_invert          = []
axis_y_float_precision = []

legend_on              = []
legend_alpha           = []
legend_location        = []

grid_major_on          = []
grid_major_linewidth   = []
grid_minor_on          = []
grid_minor_linewidth   = []




#---------------#
# ASSIGN VALUES #
#---------------#

###### TODO: do this for standard JSON-values
###### TODO: figure out how to "check" if a value in JSON exists (if not, don't overwrite standard values; if exists, do write over)
 

## PER SUBPLOT ##

for i in subplots:
    plot_type.append(               J['subplot_settings'][i]['datasets']['plot_type']                                   )
    dataset_label.append(           J['subplot_settings'][i]['datasets']['dataset_label']                               )  

    dataset_col_x.append(           J['subplot_settings'][i]['datasets']['column_x']                                        )
    dataset_col_y.append(           J['subplot_settings'][i]['datasets']['column_y']                                        )

    axis_x_label.append(            J['subplot_settings'][i]['datasets']['axis']['x']['label']                              )
    axis_x_limit_min.append(        J['subplot_settings'][i]['datasets']['axis']['x']['limit']['min']                       )
    axis_x_limit_max.append(        J['subplot_settings'][i]['datasets']['axis']['x']['limit']['max']                       )
    axis_x_scale.append(            J['subplot_settings'][i]['datasets']['axis']['x']['scale']                              )
    axis_x_invert.append(           J['subplot_settings'][i]['datasets']['axis']['x']['invert']                             )
    axis_x_float_precision.append(  J['subplot_settings'][i]['datasets']['axis']['x']['float_precision']                    )   

    axis_y_label.append(            J['subplot_settings'][i]['datasets']['axis']['y']['label']                              )
    axis_y_limit_min.append(        J['subplot_settings'][i]['datasets']['axis']['y']['limit']['min']                       )
    axis_y_limit_max.append(        J['subplot_settings'][i]['datasets']['axis']['y']['limit']['max']                       )
    axis_y_scale.append(            J['subplot_settings'][i]['datasets']['axis']['y']['scale']                              )
    axis_y_invert.append(           J['subplot_settings'][i]['datasets']['axis']['y']['invert']                             )
    axis_y_float_precision.append(  J['subplot_settings'][i]['datasets']['axis']['y']['float_precision']                    )

    legend_on.append(               J['subplot_settings'][i]['datasets']['legend']['on']                                    )
    legend_alpha.append(            J['subplot_settings'][i]['datasets']['legend']['alpha']                                 )
    legend_location.append(         J['subplot_settings'][i]['datasets']['legend']['location']                              )   

    grid_major_on.append(           J['subplot_settings'][i]['datasets']['grid']['major']['on']                             )
    grid_major_linewidth.append(    J['subplot_settings'][i]['datasets']['grid']['major']['linewidth']                      )
    grid_minor_on.append(           J['subplot_settings'][i]['datasets']['grid']['minor']['on']                             )    
    grid_minor_linewidth.append(    J['subplot_settings'][i]['datasets']['grid']['minor']['linewidth']                      )

    # TODO: "if":s that select what 'plot_type_settings' to get from JSON (line, marker, errorbar, ...)
    line_color.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['color']             )
    line_style.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['style']             )
    line_width.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['width']             )

    marker_type.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['type']            )
    marker_size.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['size']            )
    marker_thickness.append(        J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['thickness']       )
    marker_facecolor.append(        J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['facecolor']       )

    errorbar_on.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['on']            )
    errorbar_x_col.append(          J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['x_col']         )
    errorbar_y_col.append(          J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['y_col']         )
    errorbar_size.append(           J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['size']          )
    errorbar_linewidth.append(      J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['linewidth']     )
    errorbar_capthickness.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['capthickness']  )
    errorbar_constant_on.append(    J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['on']    )
    errorbar_constant_x_pm.append(  J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['x_pm']  )
    errorbar_constant_y_pm.append(  J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['y_pm']  )



print("DONE: get_JSON_data.py")