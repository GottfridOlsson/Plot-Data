##====================================================##
##     Project: PLOT DATA
##        File: get_JSON_data.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17
##     Updated: 2022-12-12
##       About: Reads and stores user data from JSON.
##====================================================##

import JSON_handler as JSON
import easygui
import os

#JSON_readFilePath = "JSON/"+ "CONFIG" + ".json" #keeping this line for myself when I'm working with figures //2022-07-05
JSON_default_path = "JSON/"
JSON_readFilePath = easygui.fileopenbox(title="Please choose your JSON-file", default=JSON_default_path)
J = JSON.read(JSON_readFilePath)

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
STANDARD_VALUES_JSON_PATH = CURRENT_PATH + "//" + 'STANDARD_VALUES.json'



#--------------------#
# GET DATA FROM JSON #
#--------------------#

filepath_csv            = J['filepath']['csv']
filepath_pdf            = J['filepath']['pdf']
try: filepath_standard_values_json = J['filepath']['standard_values']
except: filepath_standard_values_json = STANDARD_VALUES_JSON_PATH
S = JSON.READ(filepath_standard_values_json)

figure_title            = J['figure_title']
figure_height           = J['figure_size']['height_cm'] # [cm]
figure_width            = J['figure_size']['width_cm']  # [cm]

font_size_axis          = J['font_size']['axis']   # [pt]
font_size_tick          = J['font_size']['tick']   # [pt]
font_size_legend        = J['font_size']['legend'] # [pt]

subplot_setup_rows      = J['subplot_setup']['rows']
subplot_setup_columns   = J['subplot_setup']['columns']
subplot_setup_subplots  = J['subplot_setup']['total_subplots'] #TODO?: raise error if "total != rows*columns"

## subplot_setup_share_x and _y implemented 2022-11-24. It seems to be working! :D
try: subplot_setup_share_x = J['subplot_setup']['share_x']
except:
    print(f"Optiomal setting missing: subplot_setup_share_x. Taking value from {filepath_standard_values_json} instead")
    subplot_setup_share_x = S['subplot_setup']['share_x']

try: subplot_setup_share_y = J['subplot_setup']['share_y']
except:
    print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
    subplot_setup_share_x = S['subplot_setup']['share_x']

try:    LaTeX_and_CMU = J['LaTeX_and_CMU'] # bool
except: LaTeX_and_CMU = S['LaTeX_and_CMU']

try:    point_or_decimal_comma  = J['point_or_decimal_comma'] # string, "." or ","
except: point_or_decimal_comma  = S['point_or_decimal_comma'] # string, "." or ","



## DECLARE VARIABLE NAMES ##

subplots = range(subplot_setup_subplots)

subplot_num            = [i for i in subplots]
plot_type              = []

dataset_label          = []
dataset_CSV_column_x   = []
dataset_CSV_column_y   = []

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
errorbar_CSV_column_x  = []
errorbar_CSV_column_y  = []
errorbar_size          = []
errorbar_linewidth     = []
errorbar_capthickness  = []
errorbar_color         = []
errorbar_alpha         = []

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

###### TODO: do this for standard JSON-values ##//2022-07-05: is it worth it? why just not copy and paste and change the values you need to change? I can create a JSON-template to copy forall plot_types
###### TODO: figure out how to "check" if a value in JSON exists (if not, don't overwrite standard values; if exists, do write over)
 

## PER SUBPLOT ##

for i in subplots:
    # PLOT TYPE, DATA #

    try: plot_type.append(  J['subplot_settings'][i]['datasets']['plot_type']                       )
    except:
        print(f"Optiomal setting missing: plot_type. Taking value from {filepath_standard_values_json} instead")
        plot_type.append(   S['subplot_settings']['datasets']['plot_type'])

    try: dataset_label.append(       J['subplot_settings'][i]['datasets']['dataset_label']                   )  
    except:
        print(f"Optiomal setting missing: dataset_label. Taking value from {filepath_standard_values_json} instead")
        dataset_label.append(   S['subplot_settings']['datasets']['dataset_label'])

    dataset_CSV_column_x.append(    J['subplot_settings'][i]['datasets']['CSV_column_x']                    )
    dataset_CSV_column_y.append(    J['subplot_settings'][i]['datasets']['CSV_column_y']                    )


    #x-AXIS #
    try: axis_x_label.append(        J['subplot_settings'][i]['datasets']['axis']['x']['label']              )
    except:
        print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
        axis_x_label.append("x-axis")

    try: axis_x_limit_min.append(        J['subplot_settings'][i]['datasets']['axis']['x']['limit']['min']       )
    except:
        print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
        axis_x_limit_min.append(False)
    
    try: axis_x_limit_max.append(        J['subplot_settings'][i]['datasets']['axis']['x']['limit']['max']       )
    except:
        print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
        axis_x_limit_max.append(False)

    try: axis_x_scale.append(            J['subplot_settings'][i]['datasets']['axis']['x']['scale']              )
    except:
        print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
        axis_x_scale.append("linear") 
        
    try: axis_x_invert.append(           J['subplot_settings'][i]['datasets']['axis']['x']['invert']             )
    except:
        print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
        axis_x_invert.append(False) 

    try: axis_x_float_precision.append(  J['subplot_settings'][i]['datasets']['axis']['x']['float_precision']    )   
    except:
        print(f"Optiomal setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
        axis_x_float_precision.append(1) 



    # y-AXIS #
    try: axis_y_label.append(   J['subplot_settings'][i]['datasets']['axis']['y']['label']  )
    except:
        print(f"MISSING OPTIONAL SETTING: axis_y_label could not be read from get_JSON_data.py for subplot {i}. Setting it to 'x-axis' and continuing")
        axis_y_label.append("x-axis")

    try: axis_y_limit_min.append(        J['subplot_settings'][i]['datasets']['axis']['y']['limit']['min']       )
    except:
        print(f"MISSING OPTIONAL SETTING: axis_y_limit_min could not be read from get_JSON_data.py for subplot {i}. Setting it to 'False' and continuing")
        axis_y_limit_min.append(False)
    
    try: axis_y_limit_max.append(        J['subplot_settings'][i]['datasets']['axis']['y']['limit']['max']       )
    except:
        print(f"MISSING OPTIONAL SETTING: axis_y_limit_max could not be read from get_JSON_data.py for subplot {i}. Setting it to 'False' and continuing")
        axis_y_limit_max.append(False)

    try: axis_y_scale.append(            J['subplot_settings'][i]['datasets']['axis']['y']['scale']              )
    except:
        print(f"MISSING OPTIONAL SETTING: axis_y_scale could not be read from get_JSON_data.py for subplot {i}. Setting it to 'linear' and continuing")
        axis_y_scale.append("linear") 
        
    try: axis_y_invert.append(           J['subplot_settings'][i]['datasets']['axis']['y']['invert']             )
    except:
        print(f"MISSING OPTIONAL SETTING: axis_y_invert could not be read from get_JSON_data.py for subplot {i}. Setting it to 'False' and continuing")
        axis_y_invert.append(False) 

    try: axis_y_float_precision.append(  J['subplot_settings'][i]['datasets']['axis']['y']['float_precision']    )   
    except:
        print(f"MISSING OPTIONAL SETTING: axis_y_float_precision could not be read from get_JSON_data.py for subplot {i}. Setting it to '1' and continuing")
        axis_y_float_precision.append(1) 


    # LEGEND #
    try: legend_on.append(               J['subplot_settings'][i]['datasets']['legend']['on']                    )
    except:
        print(f"MISSING OPTIONAL SETTING: legend_on could not be read from get_JSON_data.py for subplot {i}. Setting it to 'False' and continuing")
        legend_on.append(False) 

    try: legend_alpha.append(            J['subplot_settings'][i]['datasets']['legend']['alpha']                 )
    except:
        print(f"MISSING OPTIONAL SETTING: legend_alpha could not be read from get_JSON_data.py for subplot {i}. Setting it to '1' and continuing")
        legend_alpha.append(1) 

    try: legend_location.append(         J['subplot_settings'][i]['datasets']['legend']['location']              )
    except:
        print(f"MISSING OPTIONAL SETTING: legend_location could not be read from get_JSON_data.py for subplot {i}. Setting it to 'best' and continuing")
        legend_location.append("best")    


    # GRID #
    try: grid_major_on.append(           J['subplot_settings'][i]['datasets']['grid']['major']['on']             )
    except:
        print(f"MISSING OPTIONAL SETTING: grid_major_on could not be read from get_JSON_data.py for subplot {i}. Setting it to 'False' and continuing")
        grid_major_on.append(False) 

    try: grid_major_linewidth.append(    J['subplot_settings'][i]['datasets']['grid']['major']['linewidth']      )
    except:
        print(f"MISSING OPTIONAL SETTING: grid_major_linewidth could not be read from get_JSON_data.py for subplot {i}. Setting it to '0.7' and continuing")
        grid_major_linewidth.append(0.7) 

    try: grid_minor_on.append(           J['subplot_settings'][i]['datasets']['grid']['minor']['on']             )
    except:
        print(f"MISSING OPTIONAL SETTING: grid_minor_on could not be read from get_JSON_data.py for subplot {i}. Setting it to 'False' and continuing")
        grid_minor_on.append(False) 

    try: grid_minor_linewidth.append(    J['subplot_settings'][i]['datasets']['grid']['minor']['linewidth']      )
    except:
        print(f"MISSING OPTIONAL SETTING: grid_minor_linewidth could not be read from get_JSON_data.py for subplot {i}. Setting it to '0.3' and continuing")
        grid_minor_linewidth.append(0.3) 




    bin_line_color = []
    bin_line_style = []
    bin_line_width = []

    bin_marker_type      = []
    bin_marker_size      = []
    bin_marker_thickness = []
    bin_marker_facecolor = []

    bin_errorbar_on            = []
    bin_errorbar_CSV_column_x  = []
    bin_errorbar_CSV_column_y  = []
    bin_errorbar_size          = []
    bin_errorbar_linewidth     = []
    bin_errorbar_capthickness  = []
    bin_errorbar_constant_on   = []
    bin_errorbar_constant_x_pm = []
    bin_errorbar_constant_y_pm = []
    bin_erorrbar_color         = []
    bin_errorbar_alpha         = []


    for k in range(len(plot_type[i])):
        # TODO: "if":s that select what 'plot_type_settings' to get from JSON (line, marker, errorbar, ...)
        bin_line_color.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['color'][k]                  )
        bin_line_style.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['style'][k]                  )
        bin_line_width.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['width'][k]                  )

        bin_marker_type.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['type'][k]                 )
        bin_marker_size.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['size'][k]                 )
        bin_marker_thickness.append(        J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['thickness'][k]            )
        bin_marker_facecolor.append(        J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['facecolor'][k]            )
        
        bin_errorbar_on.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['on'][k]                 )
        bin_errorbar_CSV_column_x.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['CSV_column_x'][k]       )
        bin_errorbar_CSV_column_y.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['CSV_column_y'][k]       )
        bin_errorbar_size.append(           J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['size'][k]               )
        bin_errorbar_linewidth.append(      J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['linewidth'][k]          )
        bin_errorbar_capthickness.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['capthickness'][k]       )
        bin_errorbar_constant_on.append(    J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['on'][k]     )
        bin_errorbar_constant_x_pm.append(  J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['x_pm'][k]   )
        bin_errorbar_constant_y_pm.append(  J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['y_pm'][k]   )
        
        # added 2022-12-09
        try:
            bin_erorrbar_color.append(      J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['errorbar_color'][k]     )
        except:
            print(f"MISSING OPTIONAL SETTING: errorbar_color could not be read from get_JSON_data.py for subplot {i} errorbar {k}. Setting it to line_color and continuing")
            bin_erorrbar_color.append(      J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['color'][k]                  )

        try:
            bin_errorbar_alpha.append (     J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['errorbar_alpha'][k]     )
        except:
            print(f"MISSING OPTIONAL SETTING: errorbar_alpha could not be read from get_JSON_data.py for subplot {i} errorbar {k}. Setting it to 1 and continuing")
            bin_errorbar_alpha.append (1)


    line_color.append(bin_line_color)
    line_style.append(bin_line_style)
    line_width.append(bin_line_width)

    marker_type.append(     bin_marker_type     )
    marker_size.append(     bin_marker_size     )
    marker_thickness.append(bin_marker_thickness)
    marker_facecolor.append(bin_marker_facecolor)
    
    errorbar_on.append(             bin_errorbar_on             )
    errorbar_CSV_column_x.append(   bin_errorbar_CSV_column_x   )
    errorbar_CSV_column_y.append(   bin_errorbar_CSV_column_y   )
    errorbar_size.append(           bin_errorbar_size           )
    errorbar_linewidth.append(      bin_errorbar_linewidth      )
    errorbar_capthickness.append(   bin_errorbar_capthickness   )
    errorbar_constant_on.append(    bin_errorbar_constant_on    )
    errorbar_constant_x_pm.append(  bin_errorbar_constant_x_pm  )
    errorbar_constant_y_pm.append(  bin_errorbar_constant_y_pm  )
    errorbar_color.append (         bin_erorrbar_color          )
    errorbar_alpha.append(          bin_errorbar_alpha          )

print(f"errorbar_color: {errorbar_color}")

commaDecimal = False
pointDecimal = True
if point_or_decimal_comma == ",":
            pointDecimal = False
            commaDecimal = True

print("DONE: get_JSON_data.py")