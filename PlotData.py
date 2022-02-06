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

from time import time
import matplotlib as mpl            # to plot
from matplotlib import font_manager # to get CMU Serif
import matplotlib.pyplot as plt     # to plot
import matplotlib.ticker as tkr     # for comma in x- and y-axis
import datetime                     # (perhaps unnecessary) to know when script last ran

import CSV_handler 
import JSON_handler

## CONSTANTS ##
CM2INCH1 = 1/2.54                   # centimeters per inch, for figsize

## FUNCTIONS ##

# markeredgewidth, markerfacecolor
def plot_plot(ax, xData, yData, dataLabel, color, marker, markerSize, markerThickness, markerFaceColor, lineStyle, lineWidth):
    out = ax.plot(xData, yData, label=dataLabel, color=color, marker=marker, markersize=markerSize, \
      markeredgewidth=markerThickness, markerfacecolor=markerFaceColor, linestyle=lineStyle, linewidth=lineWidth)
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


def set_plot_estethics():
      ax.set
      return 1
      
def set_legend(legendOn, alpha, location): #specify what "picture" to show in legend for each legendLabel
      if legendOn:
            plt.legend(framealpha=alpha, loc=location)
      print("DONE: Set legend")

def set_grid(gridOn): #subdivisions
      ax.grid(gridOn)
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


xCol_index = 1
yCol_index = 2
xData = data[header[xCol_index]]
yData = data[header[yCol_index]]
xLabel = header[xCol_index]
yLabel = header[yCol_index]

fig_height = 14
fig_width = 22


fontPath = "C:\Windows\Fonts"
fontString = "CMU Serif"
defaultFontSize = 18
xTickSize = 16
yTickSize = xTickSize
legendFontSize = 16

gridOn = True
legendOn = True
dataLabel = "Measurements 2022-02-06"
legendAlpha = 0.9
legendLocation = 'best'

color = "#f1311d" #hex
marker = ''
markerSize = 6
markerThickness = 2.5
markerFaceColor = 'None'
lineStyle = '-'
lineWidth = 2.5

filePathSaveFig = "PDF/testing"



#actual main

print(datetime.datetime.now())
# FIRST 'plt.rc' 
set_CMU_serif_font(fontString, fontPath)
set_font_size(defaultFontSize, xTickSize, yTickSize, legendFontSize)

#INTIALIZE 'fig, ax'
fig, ax = plt.subplots(figsize=(fig_width*CM2INCH1, fig_height*CM2INCH1)) #initialize fig, ax
plot_plot(ax, xData, yData, dataLabel,color, marker, markerSize, markerThickness, markerFaceColor, lineStyle, lineWidth)
set_labels(ax, xLabel, yLabel)
set_commaDecimal_with_precision(ax, 1, 2)
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