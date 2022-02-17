## PLOT SCIENTIFIC DATA: MAIN PLOTTER                      ##
#----------------------------------------------------------##
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 18:15
#     Updated: 2022-02-06, 20:53
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
def plot_plot(ax, xData, yData, dataLabel, lineColor, lineStyle, lineWidth, markerType, markerSize, markerThickness, markerFaceColor):
    out = ax.plot(xData, yData, label=dataLabel, color=lineColor, linestyle=lineStyle, linewidth=lineWidth, \
        marker=markerType, markersize=markerSize, markeredgewidth=markerThickness, markerfacecolor=markerFaceColor, )
    print("DONE: Plotted data")
    return out

def set_labels(ax, xLabel, yLabel): #TODO:#, majorTickLabel, minorTickLabel, legendLabel):
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    print("DONE: Set xLabel and yLabel")
    #ax.set_major


def set_font_size(defaultTextSize, xTickSize, yTickSize, legendFontSize): #TODO: major tick, minor tick 
    plt.rc('font',       size=defaultTextSize) #controls default text size
    #plt.rc('axes',  titlesize=10) #fontsize of the title
    plt.rc('axes',  labelsize=defaultTextSize) #fontsize of the x and y labels
    plt.rc('xtick', labelsize=xTickSize) #fontsize of the x tick labels
    plt.rc('ytick', labelsize=yTickSize) #fontsize of the y tick labels
    plt.rc('legend', fontsize=legendFontSize) #fontsize of the legend
    print("DONE: Set font size")


def set_legend(legendOn, alpha, location): #specify what "picture" to show in legend for each legendLabel
      if legendOn:
            plt.legend(framealpha=alpha, loc=location)
      print("DONE: Set legend")

def set_grid(gridOn): #subdivisions
      axs.grid(gridOn)
      print("DONE: Set grid")

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

def set_commaDecimal_with_precision(ax, xAxis_precision, yAxis_precision):
    # Modified from: https://stackoverflow.com/questions/8271564/matplotlib-comma-separated-number-format-for-axis
    xFormatString = '{:.' + str(xAxis_precision) + 'f}'
    yFormatString = '{:.' + str(yAxis_precision) + 'f}'
    ax.get_xaxis().set_major_formatter( tkr.FuncFormatter(lambda x, pos: xFormatString.format(x).replace('.', ',')) )
    ax.get_yaxis().set_major_formatter( tkr.FuncFormatter(lambda x, pos: yFormatString.format(x).replace('.', ',')) )
    print("DONE: Set comma as decimalseparator with precision: X: "+str(xAxis_precision)+", Y: "+str(yAxis_precision))

def export_figure_as_pdf(filePath):
    plt.savefig(filePath + '.pdf')
    print("DONE: Exported PDF: " + filePath + ".pdf")


## MAIN ##

#temp
CSV_readFilePath = "CSV/20220202_1439_calibration_He_1_broad.csv"
data = CSV_handler.read_CSV(CSV_readFilePath)
header = CSV_handler.get_header(data)

JSON_readFilePath = "JSON/CONFIG.json"
config = JSON_handler.read_JSON(JSON_readFilePath)
c = config


# SET DATA FROM JSON #
xLabel          = c['label_xAxis']
yLabel          = c['label_yAxis']
fig_height      = c['figure_height']
fig_width       = c['figure_width']
fontPath        = c['font_path']
fontString      = c['font']
defaultFontSize = c['fontSize_axis']
xTickSize       = c['fontSize_tick']
yTickSize       = c['fontSize_tick']
legendFontSize  = c['fontSize_legend']
gridOn          = c['grid_on']
legendOn        = c['legend_on']
legendAlpha     = c['legend_alpha']
legendLocation  = c['legend_position']
num_subplots_x  = c['num_subplots_x']
num_subplots_y  = c['num_subplots_y']

num_subplots = num_subplots_x*num_subplots_y

# INITIALIZE #

num_datasets    = c['num_datasets']
xCol_index      = [0]*num_datasets
yCol_index      = [0]*num_datasets
xData           = [0]*num_datasets
yData           = [0]*num_datasets
lineWidth       = [0]*num_datasets
markerSize      = [0]*num_datasets
markerThickness = [0]*num_datasets
floatPrecision_yAxis = [0]*num_subplots #unsure //2022-02-17
floatPrecision_xAxis = [0]*num_subplots #unsure //2022-02-17
markerFaceColor = [""]*num_datasets
lineStyle       = [""]*num_datasets
lineColor       = [""]*num_datasets
dataLabel       = [""]*num_datasets
markerType      = [""]*num_datasets


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
    markerFaceColor[i] = c['datasets'][i]['marker_facecolor']




filePathSaveFig = "PDF/testing2" #adhoc



#actual main

print(datetime.datetime.now())
# FIRST 'plt.rc' 
set_CMU_serif_font(fontString, fontPath)
set_font_size(defaultFontSize, xTickSize, yTickSize, legendFontSize)

#INTIALIZE 'fig, ax'
fig, axs = plt.subplots(num_subplots_y, num_subplots_x, figsize=(cm2inch(fig_width), cm2inch(fig_height))) #initialize fig, ax
if num_subplots > 1: 
    for k in range(0,num_subplots):
        #function that chooses which plot to plot (errorbar, plot, colormap,...)
        for i in thingThatDecidesWhichDatasetsGoesIntoWhichSubplots: #ex. datasets_subplot[k]
            plot_plot(axs[k], xData[i], yData[i], dataLabel[i], lineColor[i], lineStyle[i], lineWidth[i], \
            markerType[i], markerSize[i], markerThickness[i], markerFaceColor[i])
else:
    for i in range(0, num_datasets):
        plot_plot(axs, xData[i], yData[i], dataLabel[i], lineColor[i], lineStyle[i], lineWidth[i], \
            markerType[i], markerSize[i], markerThickness[i], markerFaceColor[i])
    set_labels(axs, xLabel, yLabel)
    set_commaDecimal_with_precision(axs, 1, 2)
    set_legend(legendOn, legendAlpha, legendLocation)
set_grid(gridOn)
export_figure_as_pdf(filePathSaveFig)

plt.show()
print() #for new line




### EOF ###




## SOURCES
  # https://matplotlib.org/stable/tutorials/introductory/usage.html
# for curve-fitting
# https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509



### EOF ###