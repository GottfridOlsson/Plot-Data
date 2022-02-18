## PLOT SCIENTIFIC DATA: MAIN PLOTTER                      ##
#----------------------------------------------------------##
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 18:15
#     Updated: 2022-02-17, 21:38
#       About: Plot data in figures with matplotlib.
#              Functions are used to make figure look nice. 
#              Plot-settings as JSON. Export figure as PDF.
##---------------------------------------------------------##

## IMPORT LIBRARIES ##

from platform import java_ver
from time import time
import matplotlib as mpl            # to plot
from matplotlib import font_manager # to get CMU Serif
import matplotlib.pyplot as plt     # to plot
import matplotlib.ticker as tkr     # for comma in x- and y-axis
import datetime                     # (perhaps unnecessary) to know when script last ran

import CSV_handler 
import JSON_handler


## FUNCTIONS ##
def cm2inch(cm):
    return cm/2.54

# markeredgewidth, markerfacecolor
def plot_plot(ax, xData, yData, dataLabel, lineColor, lineStyle, lineWidth, markerType, markerSize, markerThickness, markerFaceColor, axNum):
    out = ax.plot(xData, yData, label=dataLabel, color=lineColor, linestyle=lineStyle, linewidth=lineWidth, \
        marker=markerType, markersize=markerSize, markeredgewidth=markerThickness, markerfacecolor=markerFaceColor)
    print("DONE: Plotted data on axs: " + str(axNum))
    return out

def set_labels(ax, xLabel, yLabel, axNum): #TODO:#, majorTickLabel, minorTickLabel, legendLabel):
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    print("DONE: Set xLabel and yLabel on axs: " + str(axNum))
    #ax.set_major


def set_font_size(defaultTextSize, xTickSize, yTickSize, legendFontSize): #TODO: major tick, minor tick 
    plt.rc('font',       size=defaultTextSize) #controls default text size
    #plt.rc('axes',  titlesize=10) #fontsize of the title
    plt.rc('axes',  labelsize=defaultTextSize) #fontsize of the x and y labels
    plt.rc('xtick', labelsize=xTickSize) #fontsize of the x tick labels
    plt.rc('ytick', labelsize=yTickSize) #fontsize of the y tick labels
    plt.rc('legend', fontsize=legendFontSize) #fontsize of the legend
    print("DONE: Set font size")


def set_legend(ax, legendOn, alpha, location, axNum):
      if legendOn:
            ax.legend(framealpha=alpha, loc=location)
      print("DONE: Set legend on axs: " + str(axNum))

def set_grid(ax, gridOn, axNum): #TODO: subdivisions?
      ax.grid(gridOn)
      print("DONE: Set grid on axs: " + str(axNum))

# Unsure whether or not this actually does anything... //2022-02-06
#def set_ax_size(fig, ax_left, ax_bottom, ax_width, ax_height):
#      plt.Axes(fig, [ax_left, ax_bottom, ax_width, ax_height])
#      print("DONE: Set axis size")


def get_ax_size(ax):
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi
    return width, height

def set_CMU_serif_font(fontString, fontDirectory):
    # CMU Serif:  https://fontlibrary.org/en/font/cmu-serif
    font_dirs = fontDirectory
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)
    plt.rcParams['font.family'] = fontString
    print("DONE: Set font to: " + fontString)

def set_commaDecimal_with_precision(ax, xAxis_precision, yAxis_precision, axNum):
    # Modified from: https://stackoverflow.com/questions/8271564/matplotlib-comma-separated-number-format-for-axis
    xFormatString = '{:.' + str(xAxis_precision) + 'f}'
    yFormatString = '{:.' + str(yAxis_precision) + 'f}'
    ax.get_xaxis().set_major_formatter( tkr.FuncFormatter(lambda x, pos: xFormatString.format(x).replace('.', ',')) )
    ax.get_yaxis().set_major_formatter( tkr.FuncFormatter(lambda x, pos: yFormatString.format(x).replace('.', ',')) )
    print("DONE: Set comma as decimalseparator on with precision: X: "+str(xAxis_precision)+", Y: "+str(yAxis_precision) + " on axs: "+str(axNum))

def export_figure_as_pdf(filePath):
    plt.savefig(filePath)
    print("DONE: Exported PDF: " + filePath)


## MAIN ##

#temp
# OBS! must fill in JSON_readFilePath as of now #tofix!
readJSONFilePathStringTEMP = "20220218_0838_He_broadAndGauss2"
#"20220218_0938_fluorescens_mean"
                        #"20220218_0925_absorption_I2_measurement2"
                        #"20220202_1717_fluorescens_I2_measurement2"
JSON_readFilePath = "JSON/"+ readJSONFilePathStringTEMP + ".json" #make it such that you can ask for what file it is or smht//2022-02-18
config = JSON_handler.read_JSON(JSON_readFilePath)
c = config

filename_csv = c['filename_csv']
CSV_readFilePath = "CSV/"+str(filename_csv) + ".csv"  #"CSV/20220202_1439_calibration_He_1_broad.csv"
data = CSV_handler.read_CSV(CSV_readFilePath)
header = CSV_handler.get_header(data)

filePathSaveFig = "PDF/" + str(c['filename_pdf']) + ".pdf" #adhoc


# SET DATA FROM JSON #
xLabel          = c['label_xAxis']
yLabel          = c['label_yAxis']
fig_height      = c['figure_height']
fig_width       = c['figure_width']
fontPath        = c['font_path']
fontString      = c['font_string']
defaultFontSize = c['fontSize_axis']
xTickSize       = c['fontSize_tick']
yTickSize       = c['fontSize_tick']
legendFontSize  = c['fontSize_legend']
gridOn          = c['grid_on']
legendOn        = c['legend_on']
legendAlpha     = c['legend_alpha']
legendLocation  = c['legend_position']
subplots_x      = c['num_subplots_x']
subplots_y      = c['num_subplots_y']
num_subplots    = c['num_subplots']

# INITIALIZE #

num_datasets    = c['num_datasets']

xCol_index      = [0]*num_datasets
yCol_index      = [0]*num_datasets
xData           = [0]*num_datasets
yData           = [0]*num_datasets
lineWidth       = [0]*num_datasets
markerSize      = [0]*num_datasets
markerThickness = [0]*num_datasets
floatPrec_yAxis = [0]*num_subplots 
floatPrec_xAxis = [0]*num_subplots 
subplot_xCol    = [0]*num_subplots
subplot_yCols   = [ [ None for i in range(num_subplots) ] for i in range(num_subplots)] #perhaps too big of an allocation; -5 for "fel" or "no real column"
subplot_xData   = [0]*num_subplots
subplot_yData   = [0]*num_subplots
gridsOn         = [ False for i in range(num_subplots) ]
xLabels         = [""]*num_subplots
yLabels         = [""]*num_subplots
markerFacecolor = [""]*num_datasets
lineStyle       = [""]*num_datasets
lineColor       = [""]*num_datasets
dataLabel       = [""]*num_datasets
markerType      = [""]*num_datasets

datasets_per_subplot = [0]*num_subplots


# ASSIGN VALUES #

for i in range(0, num_datasets):
    xCol_index[i]      = c['datasets'][i]['x_column'] - 1 #convert from human "1,2,3,..." to CPU index "0,1,2,..."
    yCol_index[i]      = c['datasets'][i]['y_column'] - 1
    xData[i]           = data[header[xCol_index[i]]]
    yData[i]           = data[header[yCol_index[i]]]
    dataLabel[i]       = c['datasets'][i]['datalabel']
    lineColor[i]       = c['datasets'][i]['line_color']
    lineStyle[i]       = c['datasets'][i]['line_style']
    lineWidth[i]       = c['datasets'][i]['line_width']
    markerType[i]      = c['datasets'][i]['marker_type']
    markerSize[i]      = c['datasets'][i]['marker_size']
    markerThickness[i] = c['datasets'][i]['marker_thickness']
    markerFacecolor[i] = c['datasets'][i]['marker_facecolor']

if num_subplots > 1: 
    for i in range(0, num_subplots):
        datasets_per_subplot[i] = c['subplots'][i]['num_subplot_yDatasets']
        xLabels[i]         = c['subplots'][i]['xLabel']
        yLabels[i]         = c['subplots'][i]['yLabel']
        floatPrec_xAxis[i] = c['subplots'][i]['floatPrec_xAxis']
        floatPrec_yAxis[i] = c['subplots'][i]['floatPrec_yAxis']
        gridsOn[i]         = c['subplots'][i]['gridOn']
        subplot_xCol[i]    = c['subplots'][i]['xDataCol'] - 1
        for k in range(0, c['subplots'][i]['num_subplot_yDatasets']):
            subplot_yCols[i][k] = c['subplots'][i]['yDataCol'][k][str(k+1)] - 1
    
  



## ACTUAL MAIN ##

print(datetime.datetime.now()) #helping text in terminal
# FIRST 'plt.rc' 
set_CMU_serif_font(fontString, fontPath)
set_font_size(defaultFontSize, xTickSize, yTickSize, legendFontSize)

#INTIALIZE 'fig, ax'
fig, axs = plt.subplots(subplots_y, subplots_x, figsize=(cm2inch(fig_width), cm2inch(fig_height))) #initialize fig, ax

if num_subplots > 1: 
    for k in range(0, num_subplots):
        ## HEREGOES: function that chooses which plot to plot (errorbar, plot, colormap,...) foreach subplot
        for i in range(0, datasets_per_subplot[k]):
            if subplot_yCols[k][i] is not None:
                print(data[header[subplot_xCol[i]]])
                print(data[header[subplot_yCols[k][i]]])
                plot_plot(axs[k], data[header[subplot_xCol[i]]], data[header[subplot_yCols[k][i]]], dataLabel[i],\
                     lineColor[i], lineStyle[i], lineWidth[i], markerType[i], markerSize[i], markerThickness[i], markerFacecolor[i], k)
        set_legend(axs[k], legendOn, legendAlpha, legendLocation, k)
        set_labels(axs[k], xLabels[k], yLabels[k], k)
        set_grid(axs[k], gridsOn[k], k)
        set_commaDecimal_with_precision(axs[k], floatPrec_xAxis[k], floatPrec_yAxis[k], k)
        

if num_subplots <= 1:
    for i in range(0, num_datasets):
        plot_plot(axs, xData[i], yData[i], dataLabel[i], lineColor[i], lineStyle[i], lineWidth[i], \
            markerType[i], markerSize[i], markerThickness[i], markerFacecolor[i], 1)
    set_labels(axs, xLabel, yLabel, 1)
    set_grid(axs, gridOn, 1)
    set_legend(axs, legendOn, legendAlpha, legendLocation, 1)
    set_commaDecimal_with_precision(axs, floatPrec_xAxis[0], floatPrec_yAxis[0], 1)

plt.tight_layout() #unsure if this works w.r.t. Overleaf and textsize... //2022-02-17
#plt.tight_layout(h_pad=1) #unsure if this works w.r.t. Overleaf and textsize... //2022-02-17
export_figure_as_pdf(filePathSaveFig)

plt.show()
print() #for new line




### EOF ###




## SOURCES
  # https://matplotlib.org/stable/tutorials/introductory/usage.html
# for curve-fitting
# https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509



### EOF ###