#----------------------------------------------------------##
#        Name: PLOT DATA
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 18:15
#     Updated: 2022-04-06, 22:06
#       About: Plot data from CSV in figure with matplotlib.
#              Plot-settings in JSON. Export figure as PDF.
##---------------------------------------------------------##

#------------------#
#    LIBRARIES     #
#------------------#

import json                             # to save/write to JSON
import pandas as pd                     # for CSV
import matplotlib                 
import matplotlib.pyplot as plt         # to plot
from matplotlib import font_manager     # to get fonts not 'default' in matplotlib


##---------------##
##   FUNCTIONS   ##
##---------------##

## CSV_handler ##
CSV_DELIMITER = ','

def read_CSV(readFilePath):
    #print("In progress: Reading CSV" + CSV_filePath)
    CSV =  pd.read_csv(readFilePath, sep=CSV_DELIMITER)
    print("DONE: Reading CSV: " + readFilePath)
    return CSV

def get_CSV_header(CSV_data):
    return CSV_data.columns.values

## JSON_handler ##
def read_JSON(readFilePath):
    with open(readFilePath, 'r') as jsonfile:
        JSON = json.load(jsonfile)
    print("DONE: Reading JSON: " + readFilePath)
    return JSON

def write_JSON(writeFilePath, JSON_data):
    with open(writeFilePath, 'w', encoding='utf-8') as jsonfile:
    #jsonfile.write(JSON) #commented out //2022-02-20
        json.dump(JSON_data, jsonfile, ensure_ascii=False) #changed from "dumps()" to "dump()" and added encoding 'utf-8' and ensure_ascii=False //2022-02-20
    print("DONE: Writing JSON: " + writeFilePath)


## PLOTDATA ##
def cm2inch(cm):
    return cm/2.54

def set_labels(ax, xLabel, yLabel, axNum): #TODO:#, majorTickLabel, minorTickLabel, legendLabel):
    ax.set_xlabel(str(xLabel))
    ax.set_ylabel(str(yLabel))
    print("DONE: Set x- and y-label axs: " + str(axNum))
    #ax.set_major

def set_font(fontFamily, fontDirectory): # CMU Serif:  https://fontlibrary.org/en/font/cmu-serif
    font_files = font_manager.findSystemFonts(fontpaths=fontDirectory) #e.g. "C:\Windows\Fonts"
    for font_file in font_files:
        font_manager.fontManager.addfont(font_file) #commented //2022-02-20, uncommented //2022-02-22
    matplotlib.rcParams['font.family'] = fontFamily
    print("DONE: Set font to: " + fontFamily)

def set_font_size(defaultTextSize, xTickSize, yTickSize, legendFontSize): #TODO: major tick, minor tick 
    plt.rc('font',   size=defaultTextSize)
    plt.rc('axes',   titlesize=10)
    plt.rc('axes',   labelsize=defaultTextSize) 
    plt.rc('xtick',  labelsize=xTickSize)
    plt.rc('ytick',  labelsize=yTickSize)
    plt.rc('legend', fontsize=legendFontSize)
    print("DONE: Set font size")

def set_legend(ax, legendOn, alpha, location, axNum):
      if legendOn:
            ax.legend(framealpha=alpha, loc=location)
      print("DONE: Set legend on axs: " + str(axNum))

def set_grid(ax, gridOn, axNum): #TODO: subdivisions?
      ax.grid(gridOn)
      print("DONE: Set grid on axs: " + str(axNum))

def get_ax_size(ax):
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi
    return width, height

def set_limits(ax, xmin, xmax, ymin, ymax, axNum):
    if not xmin: xmin = None
    if not xmax: xmax = None
    if not ymin: ymin = None
    if not ymax: ymax = None
    
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    print("DONE: Set limits to x=(" + str(xmin) + ", " + str(xmax)+ ") and y=(" + str(ymin) + ", " + str(ymax)+ ") on axs: " + str(axNum))

def set_commaDecimal_with_precision(ax, xAxis_precision, yAxis_precision, axNum):
    # Modified from: https://stackoverflow.com/questions/8271564/matplotlib-comma-separated-number-format-for-axis
    xFormatString = '{:.' + str(xAxis_precision) + 'f}'
    yFormatString = '{:.' + str(yAxis_precision) + 'f}'
    ax.get_xaxis().set_major_formatter( matplotlib.ticker.FuncFormatter(lambda x, pos: xFormatString.format(x).replace('.', ',')) )
    ax.get_yaxis().set_major_formatter( matplotlib.ticker.FuncFormatter(lambda x, pos: yFormatString.format(x).replace('.', ',')) )
    print("DONE: Set comma as decimalseparator on with precision: X: "+str(xAxis_precision)+", Y: "+str(yAxis_precision) + " on axs: "+str(axNum))



def set_scientific_ticklabel(ax):
    formatter = matplotlib.ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    ax.xaxis.set_major_formatter( formatter )
    ax.yaxis.set_major_formatter( formatter )
    #ax.ticklabel_format(style='sci', axis='y', useMathText=True)
    ##### NGT är väldigt fel, fattar inte vad... //2022-03-31, 22:25




def align_labels(fig):
    fig.align_labels() #lol vilken funktion (def), //2022-02-20
    
def export_figure_as_pdf(filePath):
    plt.savefig(filePath)
    print("DONE: Exported PDF: " + filePath)


def plot_plot(ax, xData, yData, dataLabel, lineColor, lineStyle, lineWidth, markerType, markerSize, markerThickness, markerFaceColor, axNum):
    out = ax.plot(xData, yData, label=dataLabel, color=lineColor, linestyle=lineStyle, linewidth=lineWidth, \
        marker=markerType, markersize=markerSize, markeredgewidth=markerThickness, markerfacecolor=markerFaceColor)
    print("DONE: Plotted data with 'plot' on axs: " + str(axNum))
    return out

def plot_errorbar(ax, xData, yData, xError, yError, errorbarSize, errorbarLinewidth, errorbarThickness, dataLabel, lineColor, lineStyle, lineWidth, markerType, markerSize, markerThickness, markerFaceColor, axNum):
    out = ax.errorbar(xData, yData, label=dataLabel, color=lineColor, linestyle=lineStyle, linewidth=lineWidth, \
        marker=markerType, markersize=markerSize, markeredgewidth=markerThickness, markerfacecolor=markerFaceColor, \
            xerr=xError, yerr=yError, elinewidth=errorbarLinewidth, capsize=errorbarSize, capthick=errorbarThickness)
    print("DONE: Plotted data with 'errorbar' on axs: " + str(axNum))
    return out


##----------##
##   MAIN   ##
##----------##

#temp # OBS! must fill in JSON_readFilePath as of now #tofix!
readJSONFilePathStringTEMP = "20220406_2122_testdataKandidat" #"20220222_1014_fluorescenceNormalisedPeak628nmAndSimulation" # "20220221_1934_HeBroadAndGauss2" #"20220223_1558_absorbanceMeanAndSimulation" #  #"20220221_2000_absorption_I2_measurement2" #"20220221_1942_fluorescens_mean"

JSON_readFilePath = "JSON/"+ readJSONFilePathStringTEMP + ".json" #make it such that you can ask for what file it is or smht//2022-02-18
config = read_JSON(JSON_readFilePath)
c = config

filename_csv = c['filename_csv']
CSV_readFilePath = "CSV/"+str(filename_csv) + ".csv"
data = read_CSV(CSV_readFilePath)
header = get_CSV_header(data)

filePathSaveFig = "PDF/" + str(c['filename_pdf']) + ".pdf" #adhoc


#--------------------#
# GET DATA FROM JSON #
#--------------------#

fig_height      = c['figure_height']
fig_width       = c['figure_width']
fontFamily      = c['font_family']
fontDirectory   = c['font_directory']
defaultFontSize = c['fontSize_axis']
xTickSize       = c['fontSize_tick']
yTickSize       = c['fontSize_tick']
legendFontSize  = c['fontSize_legend']
num_subplots    = c['num_subplots']
subplots_x      = c['num_subplots_x']
subplots_y      = c['num_subplots_y']
max_yDatasets   = c['max_yDatasets']


#------------#
# INITIALIZE #
#------------#

floatPrec_yAxis = [0]*num_subplots 
floatPrec_xAxis = [0]*num_subplots
subplot_xData   = [0]*num_subplots
subplot_yData   = [0]*num_subplots
subplot_xCol    = [ [ None for i in range(max_yDatasets) ] for i in range(num_subplots)]
subplot_yCol    = [ [ None for i in range(max_yDatasets) ] for i in range(num_subplots)]
dataLabel       = [ [   "" for i in range(max_yDatasets) ] for i in range(num_subplots)] 
lineColor       = [ [   "" for i in range(max_yDatasets) ] for i in range(num_subplots)]
lineStyle       = [ [ None for i in range(max_yDatasets) ] for i in range(num_subplots)]
lineWidth       = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
markerSize      = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
markerThickness = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
markerType      = [ [ None for i in range(max_yDatasets) ] for i in range(num_subplots)]
markerFacecolor = [ [ None for i in range(max_yDatasets) ] for i in range(num_subplots)]
plot_type       = [ [   "" for i in range(max_yDatasets) ] for i in range(num_subplots)]
xError          = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
yError          = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
errorbarSize    = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
errorbarLinewidth    = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
errorbarCapthickness = [ [    0 for i in range(max_yDatasets) ] for i in range(num_subplots)]
legendOn        = [ False for i in range(num_subplots) ]
legendAlpha     = [ False for i in range(num_subplots) ]
legendLocation  = [ False for i in range(num_subplots) ]
gridOn          = [ False for i in range(num_subplots) ]
xLabel          = [""]*num_subplots
yLabel          = [""]*num_subplots
xlim_min        = [""]*num_subplots
xlim_max        = [""]*num_subplots
ylim_min        = [""]*num_subplots
ylim_max        = [""]*num_subplots
datasets_per_subplot = [0]*num_subplots



#---------------#
# ASSIGN VALUES #
#---------------#

for i in range(0, num_subplots):
    datasets_per_subplot[i]   = c['subplots'][i]['num_yDatasets']
    xLabel[i]                 = c['subplots'][i]['xLabel']
    yLabel[i]                 = c['subplots'][i]['yLabel']
    xlim_min[i]               = c['subplots'][i]['xlim_min']
    xlim_max[i]               = c['subplots'][i]['xlim_max']
    ylim_min[i]               = c['subplots'][i]['ylim_min']
    ylim_max[i]               = c['subplots'][i]['ylim_max']
    floatPrec_xAxis[i]        = c['subplots'][i]['floatPrec_xAxis']
    floatPrec_yAxis[i]        = c['subplots'][i]['floatPrec_yAxis']
    legendOn[i]               = c['subplots'][i]['legend_on']
    legendLocation[i]         = c['subplots'][i]['legend_location']
    legendAlpha[i]            = c['subplots'][i]['legend_alpha']
    gridOn[i]                 = c['subplots'][i]['grid_on']

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
                xError[i][k]  = c['subplots'][i]['yDataset'][k]['constant_xError']
                yError[i][k]  = c['subplots'][i]['yDataset'][k]['constant_yError']
            
 #print(xError, yError)
 #quit()
        
##---------------##
##  ACTUAL MAIN  ##
##---------------##

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif", 
    "font.serif" : ["Computer Modern Roman"]
})

set_font(fontFamily, fontDirectory)
set_font_size(defaultFontSize, xTickSize, yTickSize, legendFontSize)

fig, axs = plt.subplots(subplots_y, subplots_x, figsize=(cm2inch(fig_width), cm2inch(fig_height)))

if num_subplots > 1: 
    for i in range(0, num_subplots):
        ## HEREGOES: function that chooses which plot to plot (errorbar, plot, colormap,...) foreach subplot
        for k in range(0, datasets_per_subplot[i]):
            if plot_type[i][k] == "plot":
                if subplot_yCol[i][k] is not None:
                    print("Plotting 'plot': x: "+ header[subplot_xCol[i][k]]+", and y: "+ header[subplot_yCol[i][k]])
                    plot_plot(axs[i], data[header[subplot_xCol[i][k]]], data[header[subplot_yCol[i][k]]], dataLabel[i][k],\
                        lineColor[i][k],  lineStyle[i][k],  lineWidth[i][k], \
                        markerType[i][k], markerSize[i][k], markerThickness[i][k], markerFacecolor[i][k], k)
            elif plot_type[i][k] == "errorbar":
                if subplot_yCol[i][k] is not None:
                    print("Plotting 'errorbar': x: "+ header[subplot_xCol[i][k]]+", and y: "+ header[subplot_yCol[i][k]])
                    plot_errorbar(axs[i], data[header[subplot_xCol[i][k]]], data[header[subplot_yCol[i][k]]], xError[i][k], yError[i][k], errorbarSize[i][k], errorbarLinewidth[i][k], errorbarCapthickness[i][k], dataLabel[i][k],\
                        lineColor[i][k],  lineStyle[i][k],  lineWidth[i][k], \
                        markerType[i][k], markerSize[i][k], markerThickness[i][k], markerFacecolor[i][k], k)
            else:
                print("ERROR: keyword 'plot_type' = " + str(plot_type[i][k]) + " is not yet implemented. Sorry :/")            
        set_limits(axs[i], xlim_min[i], xlim_max[i], ylim_min[i], ylim_max[i], i)
        set_legend(axs[i], legendOn[i], legendAlpha[i], legendLocation[i], i)
        set_labels(axs[i], xLabel[i], yLabel[i], i) 
        set_grid(axs[i], gridOn[i], i)
        #set_scientific_ticklabel(axs[i])
        set_commaDecimal_with_precision(axs[i], floatPrec_xAxis[i], floatPrec_yAxis[i], i)
        
        
        ###### skräp sTART
        #matplotlib.ticker.ScalarFormatter(useOffset=True, useMathText=True)
        #axs[i].ticklabel_formatter(axis='x', style='scientific', scilimits=(0,0))
        #axs[i].yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter(useMathText=True))
        
        #axs[i].xaxis.set_major_formatter(ticker.ScalarFormatter.set_useMathText(True))
        # ...set_useMathText(True)

        #ticker.ScalarFormatter.set_scientific(True, True)
        ###### skräp Slut



if num_subplots <= 1:
    i = 0 #to avoid magic numbers
    for k in range(0, datasets_per_subplot[i]):
        if plot_type[i][k] == "plot":
            plot_plot(axs, data[header[subplot_xCol[i][k]]], data[header[subplot_yCol[i][k]]], dataLabel[i][k],\
                lineColor[i][k],  lineStyle[i][k],  lineWidth[i][k], \
                markerType[i][k], markerSize[i][k], markerThickness[i][k], markerFacecolor[i][k], k)
        elif plot_type[i][k] == "errorbar":
                plot_errorbar(axs, data[header[subplot_xCol[i][k]]], data[header[subplot_yCol[i][k]]], xError[i][k], yError[i][k], errorbarSize[i][k], errorbarLinewidth[i][k], errorbarCapthickness[i][k], dataLabel[i][k],\
                    lineColor[i][k],  lineStyle[i][k],  lineWidth[i][k], \
                    markerType[i][k], markerSize[i][k], markerThickness[i][k], markerFacecolor[i][k], k)
        else:
            print("ERROR: keyword 'plot_type' = " + str(plot_type[i][k]) + " is not yet implemented. Sorry :/")
    set_limits(axs, xlim_min[i], xlim_max[i], ylim_min[i], ylim_max[i], i)
    set_legend(axs, legendOn[i], legendAlpha[i], legendLocation[i], i)
    set_labels(axs, xLabel[i], yLabel[i], i) 
    set_grid(  axs, gridOn[i], i)
    set_commaDecimal_with_precision(axs, floatPrec_xAxis[i], floatPrec_yAxis[i], i)

#print(data)

align_labels(fig)
plt.tight_layout() #I think this works. Mostly bcs I use figure_width as the baseline for all measurements //2022-02-21; looks like it works! //2022-02-22 
export_figure_as_pdf(filePathSaveFig)
plt.show()
print() #for new line


###-----###
### EOF ###
###-----###