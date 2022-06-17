##====================================================##
##     Project: PLOT DATA
##        File: get_JSON_data.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-17, 11:54
##     Updated: 2022-06-17, 11:56
##       About: Reads and stores standard settings if
##              not overwritten by user data in JSON
##====================================================##


import JSON_handler as JSON


JSON_readFilePath = "JSON/"+ readJSONFilePathStringTEMP + ".json" #make it such that you can ask for what file it is or smht//2022-02-18
config = read_JSON(JSON_readFilePath)
c = config




#### FROM OLD: ####


#--------------------#
# GET DATA FROM JSON #
#--------------------#

fig_height      = c['figure_height']
fig_width       = c['figure_width']
#fontFamily      = c['font_family'] # #2022-04-07, keeping it in case i want to implement this in the future for other fonts
#fontDirectory   = c['font_directory'] # #2022-04-07
LaTeX_and_CMU   = c['LaTeX_and_CMU']
defaultFontSize = c['fontSize_axis']
xTickSize       = c['fontSize_tick']
yTickSize       = c['fontSize_tick']
legendFontSize  = c['fontSize_legend']
num_subplots    = c['num_subplots']
subplots_x      = c['num_subplots_x']
subplots_y      = c['num_subplots_y']
max_yDatasets   = c['max_yDatasets']



#---------------#
# ASSIGN VALUES #
#---------------#

for i in range(0, num_subplots):
    datasets_per_subplot[i]   = c['subplots'][i]['num_yDatasets']
    xLabel[i]                 = c['subplots'][i]['xLabel']
    yLabel[i]                 = c['subplots'][i]['yLabel']
    xScale[i]                 = c['subplots'][i]['xScale']
    yScale[i]                 = c['subplots'][i]['yScale']
    xlim_min[i]               = c['subplots'][i]['xlim_min']
    xlim_max[i]               = c['subplots'][i]['xlim_max']
    ylim_min[i]               = c['subplots'][i]['ylim_min']
    ylim_max[i]               = c['subplots'][i]['ylim_max']
    floatPrec_xAxis[i]        = c['subplots'][i]['floatPrec_xAxis']
    floatPrec_yAxis[i]        = c['subplots'][i]['floatPrec_yAxis']
    legendOn[i]               = c['subplots'][i]['legend_on']
    legendLocation[i]         = c['subplots'][i]['legend_location']
    legendAlpha[i]            = c['subplots'][i]['legend_alpha']
    gridMajorOn[i]            = c['subplots'][i]['grid_on']
    gridMinorOn[i]            = c['subplots'][i]['grid_minor_on']

    for k in range(0, c['subplots'][i]['num_yDatasets']):
        subplot_xCol[i][k]    = c['subplots'][i]['xDataCol'][k][str(k+1)] - 1
        subplot_yCol[i][k]    = c['subplots'][i]['yDataCol'][k][str(k+1)] - 1
        plot_type[i][k]       = c['subplots'][i]['yDataset'][k]['plot_type']
        dataLabel[i][k]       = c['subplots'][i]['yDataset'][k]['datalabel']
        lineColor[i][k]       = c['subplots'][i]['yDataset'][k]['line_color']
        lineStyle[i][k]       = c['subplots'][i]['yDataset'][k]['line_style']
        lineWidth[i][k]       = c['subplots'][i]['yDataset'][k]['line_width']
        markerType[i][k]      = c['subplots'][i]['yDataset'][k]['marker_type']
        markerSize[i][k]      = c['subplots'][i]['yDataset'][k]['marker_size']
        markerThickness[i][k] = c['subplots'][i]['yDataset'][k]['marker_thickness']
        markerFacecolor[i][k] = c['subplots'][i]['yDataset'][k]['marker_facecolor']
        
        if plot_type[i][k] == "errorbar":
            errorbarSize[i][k]          = c['subplots'][i]['yDataset'][k]['errorbar_size']
            errorbarLinewidth[i][k]     = c['subplots'][i]['yDataset'][k]['errorbar_linewidth']
            errorbarCapthickness[i][k]  = c['subplots'][i]['yDataset'][k]['errorbar_capthickness']
            if c['subplots'][i]['yDataset'][k]['constant_errorbar']:
                xError[i][k]            = c['subplots'][i]['yDataset'][k]['constant_xError']
                yError[i][k]            = c['subplots'][i]['yDataset'][k]['constant_yError']
            else:
                errorbar_xError_col     = c['subplots'][i]['yDataset'][k]['errorbar_xError_col']
                errorbar_yError_col     = c['subplots'][i]['yDataset'][k]['errorbar_yError_col']
                if errorbar_xError_col is not False:
                    xError[i][k] = data[header[errorbar_xError_col]]
                else:
                    xError[i][k] = 0 # can i make this more effective, coding-wise?

                if errorbar_yError_col is not False:
                    yError[i][k] = data[header[errorbar_yError_col]]
                else:
                    yError[i][k] = 0 # can i make this more effective, coding-wise?
