##====================================================##
##     Project: PLOT DATA
##        File: get_JSON_data.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17
##     Updated: 2022-12-28
##       About: Reads and stores user data from JSON.
##====================================================##

import JSON_handler as JSON
import easygui
import os


print("===== PLOT DATA: Read JSON (start) =====")

#JSON_readFilePath = "JSON/"+ "CONFIG" + ".json" #keeping this line for myself when I'm working with figures //2022-07-05
JSON_default_path = "JSON/"
JSON_readFilePath = easygui.fileopenbox(title="Please choose your JSON-file", default=JSON_default_path)
J = JSON.read(JSON_readFilePath)

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
STANDARD_VALUES_JSON_PATH = CURRENT_PATH + "\\JSON\\" + 'STANDARD_VALUES_ERRORBAR.json'



#--------------------#
# GET DATA FROM JSON #
#--------------------#

filepath_csv                    = J['filepath']['csv']
filepath_pdf                    = J['filepath']['pdf']

try: filepath_standard_values_json = CURRENT_PATH + "\\" + J['filepath']['standard_values']
except: filepath_standard_values_json = STANDARD_VALUES_JSON_PATH
S = JSON.read(filepath_standard_values_json)

try:    figure_title            = J['figure_title']
except: figure_title            = S['figure_title']

try: figure_height              = J['figure_size']['height_cm'] # [cm]
except: figure_height           = S['figure_size']['height_cm'] # [cm]

try: figure_width               = J['figure_size']['width_cm']  # [cm]
except: figure_width            = S['figure_size']['width_cm'] # [cm]


try: font_size_axis             = J['font_size']['axis'] # [pt]
except: font_size_axis          = S['font_size']['axis'] # [pt]

try: font_size_tick             = J['font_size']['tick'] # [pt]
except: font_size_tick          = S['font_size']['tick'] # [pt]

try: font_size_legend           = J['font_size']['legend'] # [pt]
except: font_size_legend        = S['font_size']['legend'] # [pt]


try: subplot_setup_rows         = J['subplot_setup']['rows']
except: subplot_setup_rows      = S['subplot_setup']['rows']


try: subplot_setup_columns      = J['subplot_setup']['columns']
except: subplot_setup_columns   = S['subplot_setup']['columns']

try: subplot_setup_subplots     = J['subplot_setup']['total_subplots'] #TODO?: raise error if "total != rows*columns"
except: subplot_setup_subplots  = S['subplot_setup']['total_subplots']


## subplot_setup_share_x and _y implemented 2022-11-24. It seems to be working! :D
try: subplot_setup_share_x      = J['subplot_setup']['share_x']
except:
    print(f"Optional setting missing: subplot_setup_share_x. Taking value from {filepath_standard_values_json} instead")
    subplot_setup_share_x       = S['subplot_setup']['share_x']

try: subplot_setup_share_y      = J['subplot_setup']['share_y']
except:
    print(f"Optional setting missing: subplot_setup_share_y. Taking value from {filepath_standard_values_json} instead")
    subplot_setup_share_y       = S['subplot_setup']['share_y']

try:    LaTeX_and_CMU           = J['LaTeX_and_CMU'] # bool
except: LaTeX_and_CMU           = S['LaTeX_and_CMU']

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
        print(f"Optional setting missing: plot_type on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        plot_type.append(   S['subplot_settings']['plot_type'])

    try: dataset_label.append(       J['subplot_settings'][i]['datasets']['dataset_label']                   )  
    except:
        print(f"Optional setting missing: dataset_label on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        dataset_label.append(   S['subplot_settings']['dataset_label'])

    try: dataset_CSV_column_x.append(    J['subplot_settings'][i]['datasets']['CSV_column_x']                    )
    except:
        print(f"Optional setting missing: dataset_CSV_column_x on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        dataset_CSV_column_x.append(   S['subplot_settings']['CSV_column_x'])
    
    try: dataset_CSV_column_y.append(    J['subplot_settings'][i]['datasets']['CSV_column_y']                    )
    except:
        print(f"Optional setting missing: dataset_CSV_column_y on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        dataset_CSV_column_y.append(   S['subplot_settings']['dataset_CSV_column_y'])



    #x-AXIS #
    try: axis_x_label.append(        J['subplot_settings'][i]['datasets']['axis']['x']['label']              )
    except:
        print(f"Optional setting missing: axis_x_label on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_x_label.append(S['subplot_settings']['axis']['x']['label'])

    try: axis_x_limit_min.append(        J['subplot_settings'][i]['datasets']['axis']['x']['limit']['min']       )
    except:
        print(f"Optional setting missing: axis_x_limit_min on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_x_limit_min.append(S['subplot_settings']['axis']['x']['limit']['min'])
    
    try: axis_x_limit_max.append(        J['subplot_settings'][i]['datasets']['axis']['x']['limit']['max']       )
    except:
        print(f"Optional setting missing: axis_x_limit_max on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_x_limit_max.append(S['subplot_settings']['axis']['x']['limit']['max'])

    try: axis_x_scale.append(            J['subplot_settings'][i]['datasets']['axis']['x']['scale']              )
    except:
        print(f"Optional setting missing: axis_x_scale on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_x_scale.append(S['subplot_settings']['axis']['x']['scale']) 
        
    try: axis_x_invert.append(           J['subplot_settings'][i]['datasets']['axis']['x']['invert']             )
    except:
        print(f"Optional setting missing: axis_x_invert on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_x_invert.append(S['subplot_settings']['axis']['x']['invert']) 

    try: axis_x_float_precision.append(  J['subplot_settings'][i]['datasets']['axis']['x']['float_precision']    )   
    except:
        print(f"Optional setting missing: axis_x_float_precision on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_x_float_precision.append(S['subplot_settings']['axis']['x']['float_precision']) 



    # y-AXIS #
    try: axis_y_label.append(        J['subplot_settings'][i]['datasets']['axis']['y']['label']              )
    except:
        print(f"Optional setting missing: axis_y_label on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_y_label.append(S['subplot_settings']['axis']['y']['label'])

    try: axis_y_limit_min.append(        J['subplot_settings'][i]['datasets']['axis']['y']['limit']['min']       )
    except:
        print(f"Optional setting missing: axis_y_limit_min on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_y_limit_min.append(S['subplot_settings']['axis']['y']['limit']['min'])
    
    try: axis_y_limit_max.append(        J['subplot_settings'][i]['datasets']['axis']['y']['limit']['max']       )
    except:
        print(f"Optional setting missing: axis_y_limit_max on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_y_limit_max.append(S['subplot_settings']['axis']['y']['limit']['max'])

    try: axis_y_scale.append(            J['subplot_settings'][i]['datasets']['axis']['y']['scale']              )
    except:
        print(f"Optional setting missing: axis_y_scale on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_y_scale.append(S['subplot_settings']['axis']['y']['scale']) 
        
    try: axis_y_invert.append(           J['subplot_settings'][i]['datasets']['axis']['y']['invert']             )
    except:
        print(f"Optional setting missing: axis_y_invert on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_y_invert.append(S['subplot_settings']['axis']['y']['invert']) 

    try: axis_y_float_precision.append(  J['subplot_settings'][i]['datasets']['axis']['y']['float_precision']    )   
    except:
        print(f"Optional setting missing: axis_y_float_precision on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        axis_y_float_precision.append(S['subplot_settings']['axis']['y']['float_precision']) 



    # LEGEND #
    try: legend_on.append(               J['subplot_settings'][i]['datasets']['legend']['on']                    )
    except:
        print(f"Optional setting missing: legend_on on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        legend_on.append(S['subplot_settings']['legend']['on']) 

    try: legend_alpha.append(            J['subplot_settings'][i]['datasets']['legend']['alpha']                 )
    except:
        print(f"Optional setting missing: legend_alpha on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        legend_alpha.append(S['subplot_settings']['legend']['alpha']) 

    try: legend_location.append(         J['subplot_settings'][i]['datasets']['legend']['location']              )
    except:
        print(f"Optional setting missing: legend_location on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        legend_location.append(S['subplot_settings']['legend']['location'])    



    # GRID #
    try: grid_major_on.append(           J['subplot_settings'][i]['datasets']['grid']['major']['on']             )
    except:
        print(f"Optional setting missing: grid_major_on on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        grid_major_on.append(S['subplot_settings']['grid']['major']['on']) 

    try: grid_major_linewidth.append(    J['subplot_settings'][i]['datasets']['grid']['major']['linewidth']      )
    except:
        print(f"Optional setting missing: grid_major_linewidth on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        grid_major_linewidth.append(S['subplot_settings']['grid']['major']['linewidth']) 

    try: grid_minor_on.append(           J['subplot_settings'][i]['datasets']['grid']['minor']['on']             )
    except:
        print(f"Optional setting missing: grid_minor_on on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        grid_minor_on.append(S['subplot_settings']['grid']['minor']['on']) 

    try: grid_minor_linewidth.append(    J['subplot_settings'][i]['datasets']['grid']['minor']['linewidth']      )
    except:
        print(f"Optional setting missing: grid_minor_linewidth on subplot {i}. Taking value from {filepath_standard_values_json} instead")
        grid_minor_linewidth.append(S['subplot_settings']['grid']['minor']['linewidth']) 




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

        try: bin_line_color.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['color'][k]                  )
        except:
            print(f"Optional setting missing: line_color on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_line_color.append(S['subplot_settings']['plot_type_settings']['line']['color']) 

        try: bin_line_style.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['style'][k]                  )
        except:
            print(f"Optional setting missing: line_style on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_line_style.append(S['subplot_settings']['plot_type_settings']['line']['style']) 

        try: bin_line_width.append(              J['subplot_settings'][i]['datasets']['plot_type_settings']['line']['width'][k]                  )
        except:
            print(f"Optional setting missing: line_width on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_line_width.append(S['subplot_settings']['plot_type_settings']['line']['width']) 

        try: bin_marker_type.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['type'][k]                 )
        except:
            print(f"Optional setting missing: marker_type on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_marker_type.append(S['subplot_settings']['plot_type_settings']['marker']['type']) 

        try: bin_marker_size.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['size'][k]                 )
        except:
            print(f"Optional setting missing: marker_size on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_marker_size.append(S['subplot_settings']['plot_type_settings']['marker']['size']) 

        try: bin_marker_thickness.append(        J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['thickness'][k]            )
        except:
            print(f"Optional setting missing: marker_thickness on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_marker_thickness.append(S['subplot_settings']['plot_type_settings']['marker']['thickness']) 

        try: bin_marker_facecolor.append(        J['subplot_settings'][i]['datasets']['plot_type_settings']['marker']['facecolor'][k]            )
        except:
            print(f"Optional setting missing: marker_facecolor on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_marker_facecolor.append(S['subplot_settings']['plot_type_settings']['marker']['facecolor']) 




        try: bin_errorbar_on.append(             J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['on'][k]                 )
        except:
            print(f"Optional setting missing: errorbar_on on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_on.append(S['subplot_settings']['plot_type_settings']['errorbar']['on']) 

        try: bin_errorbar_CSV_column_x.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['CSV_column_x'][k]       )
        except:
            print(f"Optional setting missing: errorbar_CSV_column_x on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_CSV_column_x.append(S['subplot_settings']['plot_type_settings']['errorbar']['CSV_column_x']) 

        try: bin_errorbar_CSV_column_y.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['CSV_column_y'][k]       )
        except:
            print(f"Optional setting missing: errorbar_CSV_column_y on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_CSV_column_y.append(S['subplot_settings']['plot_type_settings']['errorbar']['CSV_column_y']) 

        try: bin_errorbar_size.append(           J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['size'][k]               )
        except:
            print(f"Optional setting missing: errorbar_size on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_size.append(S['subplot_settings']['plot_type_settings']['errorbar']['size']) 

        try: bin_errorbar_linewidth.append(      J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['linewidth'][k]          )
        except:
            print(f"Optional setting missing: errorbar_linewidth on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_linewidth.append(S['subplot_settings']['plot_type_settings']['errorbar']['linewidth']) 

        try: bin_errorbar_capthickness.append(   J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['capthickness'][k]       )
        except:
            print(f"Optional setting missing: errorbar_capthickness on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_capthickness.append(S['subplot_settings']['plot_type_settings']['errorbar']['capthickness']) 

        try: bin_errorbar_constant_on.append(    J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['on'][k]     )
        except:
            print(f"Optional setting missing: errorbar_constant_on on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_constant_on.append(S['subplot_settings']['plot_type_settings']['errorbar']['constant']['on']) 

        try: bin_errorbar_constant_x_pm.append(  J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['x_pm'][k]   )
        except:
            print(f"Optional setting missing: errorbar_constant_x_pm on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_constant_x_pm.append(S['subplot_settings']['plot_type_settings']['errorbar']['constant']['x_pm']) 

        try: bin_errorbar_constant_y_pm.append(  J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['constant']['y_pm'][k]   )
        except:
            print(f"Optional setting missing: errorbar_constant_y_pm on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_constant_y_pm.append(S['subplot_settings']['plot_type_settings']['errorbar']['constant']['y_pm']) 


        # added 2022-12-09
        try: bin_erorrbar_color.append(      J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['color'][k]     )
        except:
            print(f"Optional setting missing: erorrbar_color on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_erorrbar_color.append(S['subplot_settings']['plot_type_settings']['errorbar']['color'])

        try: bin_errorbar_alpha.append (     J['subplot_settings'][i]['datasets']['plot_type_settings']['errorbar']['alpha'][k]     )
        except:
            print(f"Optional setting missing: errorbar_alpha on subplot {i} axs {k}. Taking value from {filepath_standard_values_json} instead")
            bin_errorbar_alpha.append(S['subplot_settings']['plot_type_settings']['errorbar']['alpha'])


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


commaDecimal = False
pointDecimal = True
if point_or_decimal_comma == ",":
            pointDecimal = False
            commaDecimal = True



print("===== PLOT DATA: Read JSON (end) =====")