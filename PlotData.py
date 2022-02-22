## PLOT SCIENTIFIC DATA: PLOTTER                           ##
#----------------------------------------------------------##
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 18:15
#     Updated: 2022-02-22, 11:17
#       About: Plot data in figures with matplotlib.
#              Functions are used to make figure look nice. 
#              Plot-settings as JSON. Export figure as PDF.
##---------------------------------------------------------##

#------------------#
# IMPORT LIBRARIES #
#------------------#

import matplotlib                 
import matplotlib.pyplot as plt     

import CSV_handler 
import JSON_handler



##---------------##
##   FUNCTIONS   ##
##---------------##

def cm2inch(cm):
    return cm/2.54

def plot_plot(ax, xData, yData, dataLabel, lineColor, lineStyle, lineWidth, markerType, markerSize, markerThickness, markerFaceColor, axNum):
    out = ax.plot(xData, yData, label=dataLabel, color=lineColor, linestyle=lineStyle, linewidth=lineWidth, \
        marker=markerType, markersize=markerSize, markeredgewidth=markerThickness, markerfacecolor=markerFaceColor)
    print("DONE: Plotted data on axs: " + str(axNum))
    return out

def set_labels(ax, xLabel, yLabel, axNum): #TODO:#, majorTickLabel, minorTickLabel, legendLabel):
    ax.set_xlabel(str(xLabel))
    ax.set_ylabel(str(yLabel))
    print("DONE: Set x- and y-label axs: " + str(axNum))
    #ax.set_major

def set_font(fontFamily): #, fontDirectory): //2022-02-20
    # CMU Serif:  https://fontlibrary.org/en/font/cmu-serif
     #font_files = font_manager.findSystemFonts(fontpaths=fontDirectory) #e.g. "C:\Windows\Fonts"
     #for font_file in font_files:
     #    font_manager.fontManager.addfont(font_file) #commented //2022-02-20
     #needs:  from matplotlib import font_manager # to get CMU Serif //don't use this part of the function anymore //2022-02-20
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

def align_labels(fig):
    fig.align_labels() #lol vilken funktion (def), //2022-02-20
    
def export_figure_as_pdf(filePath):
    plt.savefig(filePath)
    print("DONE: Exported PDF: " + filePath)



##----------##
##   MAIN   ##
##----------##

#temp # OBS! must fill in JSON_readFilePath as of now #tofix!
readJSONFilePathStringTEMP = "20220222_1014_fluorescenceNormalisedPeak628nmAndSimulation" #"20220221_2000_absorption_I2_measurement2" #"20220221_1942_fluorescens_mean" #"20220221_1934_HeBroadAndGauss2" #

JSON_readFilePath = "JSON/"+ readJSONFilePathStringTEMP + ".json" #make it such that you can ask for what file it is or smht//2022-02-18
config = JSON_handler.read_JSON(JSON_readFilePath)
c = config

filename_csv = c['filename_csv']
CSV_readFilePath = "CSV/"+str(filename_csv) + ".csv"
data = CSV_handler.read_CSV(CSV_readFilePath)
header = CSV_handler.get_header(data)

filePathSaveFig = "PDF/" + str(c['filename_pdf']) + ".pdf" #adhoc


#--------------------#
# GET DATA FROM JSON #
#--------------------#

fig_height      = c['figure_height']
fig_width       = c['figure_width']
fontFamily      = c['font_family']
defaultFontSize = c['fontSize_axis']
xTickSize       = c['fontSize_tick']
yTickSize       = c['fontSize_tick']
legendFontSize  = c['fontSize_legend']
num_subplots    = c['num_subplots']
subplots_x      = c['num_subplots_x']
subplots_y      = c['num_subplots_y']

#TOFIX:
#TOFIX: do smth like this to fix the initialize/allocation of matrixes for things below //2022-02-22
 # max_yDatasets_per_subplot = c['max_yDatasets_per_subplot']


#------------#
# INITIALIZE #
#------------#

floatPrec_yAxis = [0]*num_subplots 
floatPrec_xAxis = [0]*num_subplots
subplot_xData   = [0]*num_subplots
subplot_yData   = [0]*num_subplots 
subplot_xCol    = [ [ None for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
subplot_yCol    = [ [ None for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
    #TOFIX: subplot_yCol should, in the second range, NOT have num_subplots but rather " max(c['subplots'][i]['num_yDatasets']) " //2022-02-22
dataLabel       = [ [   "" for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?  
#TOFIX: dataLabel should, in the second range, NOT have num_subplots but rather " max(c['subplots'][i]['num_yDatasets']) " //2022-02-22
lineColor       = [ [   "" for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
lineStyle       = [ [ None for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
lineWidth       = [ [    0 for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
markerSize      = [ [    0 for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
markerThickness = [ [    0 for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
markerType      = [ [ None for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
markerFacecolor = [ [ None for i in range(5) ] for i in range(5)] #perhaps too big of an allocation?
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
    datasets_per_subplot[i] = c['subplots'][i]['num_yDatasets']
    xLabel[i]               = c['subplots'][i]['xLabel']
    yLabel[i]               = c['subplots'][i]['yLabel']
    xlim_min[i]             = c['subplots'][i]['xlim_min']
    xlim_max[i]             = c['subplots'][i]['xlim_max']
    ylim_min[i]             = c['subplots'][i]['ylim_min']
    ylim_max[i]             = c['subplots'][i]['ylim_max']
    floatPrec_xAxis[i]      = c['subplots'][i]['floatPrec_xAxis']
    floatPrec_yAxis[i]      = c['subplots'][i]['floatPrec_yAxis']
    legendOn[i]             = c['subplots'][i]['legend_on']
    legendLocation[i]       = c['subplots'][i]['legend_location']
    legendAlpha[i]          = c['subplots'][i]['legend_alpha']
    gridOn[i]               = c['subplots'][i]['grid_on']

    for k in range(0, c['subplots'][i]['num_yDatasets']):
        print(i,k)
        #print(c['subplots'][i]['yDataCol'][k][str(k+1)] - 1)
        print(len(dataLabel))
        subplot_xCol[i][k]    = c['subplots'][i]['xDataCol'][k][str(k+1)] - 1
        subplot_yCol[i][k]    = c['subplots'][i]['yDataCol'][k][str(k+1)] - 1
        dataLabel[i][k]       = c['subplots'][i]['yDataset'][k]['datalabel']
        lineColor[i][k]       = c['subplots'][i]['yDataset'][k]['line_color']
        lineStyle[i][k]       = c['subplots'][i]['yDataset'][k]['line_style']
        lineWidth[i][k]       = c['subplots'][i]['yDataset'][k]['line_width']
        markerType[i][k]      = c['subplots'][i]['yDataset'][k]['marker_type']
        markerSize[i][k]      = c['subplots'][i]['yDataset'][k]['marker_size']
        markerThickness[i][k] = c['subplots'][i]['yDataset'][k]['marker_thickness']
        markerFacecolor[i][k] = c['subplots'][i]['yDataset'][k]['marker_facecolor']
        

  



#error searching:

if False:
    print(subplot_xCol)
    print(subplot_yCol)
    print(data)
    print(xlim_min, xlim_max, ylim_min, ylim_max)
    

##---------------##
##  ACTUAL MAIN  ##
##---------------##

set_font(fontFamily)#, fontDirectory) #//2022-02-20
set_font_size(defaultFontSize, xTickSize, yTickSize, legendFontSize)

fig, axs = plt.subplots(subplots_y, subplots_x, figsize=(cm2inch(fig_width), cm2inch(fig_height)))

if num_subplots > 1: 
    for k in range(0, num_subplots):
        ## HEREGOES: function that chooses which plot to plot (errorbar, plot, colormap,...) foreach subplot
        for i in range(0, datasets_per_subplot[k]):
            print(subplot_yCol)
            if subplot_yCol[k][i] is not None:
                print("Plotting: x: "+ header[subplot_xCol[k][i]]+", and y: "+ header[subplot_yCol[k][i]])
                plot_plot(axs[k], data[header[subplot_xCol[k][i]]], data[header[subplot_yCol[k][i]]], dataLabel[k][i],\
                    lineColor[k][i],  lineStyle[k][i],  lineWidth[k][i], \
                    markerType[k][i], markerSize[k][i], markerThickness[k][i], markerFacecolor[k][i], k)
        set_limits(axs[k], xlim_min[k], xlim_max[k], ylim_min[k], ylim_max[k], k)
        set_legend(axs[k], legendOn[k], legendAlpha[k], legendLocation[k], k)
        set_labels(axs[k], xLabel[k], yLabel[k], k) 
        set_grid(axs[k], gridOn[k], k)
        set_commaDecimal_with_precision(axs[k], floatPrec_xAxis[k], floatPrec_yAxis[k], k)
        

if num_subplots <= 1:
    k = 0 #to avoid magic numbers
    for i in range(0, datasets_per_subplot[k]):
            plot_plot(axs, data[header[subplot_xCol[k][i]]], data[header[subplot_yCol[k][i]]], dataLabel[k][i],\
                lineColor[k][i],  lineStyle[k][i],  lineWidth[k][i], \
                markerType[k][i], markerSize[k][i], markerThickness[k][i], markerFacecolor[k][i], k)
    set_limits(axs, xlim_min[k], xlim_max[k], ylim_min[k], ylim_max[k], k)
    set_legend(axs, legendOn[k], legendAlpha[k], legendLocation[k], k)
    set_labels(axs, xLabel[k], yLabel[k], k) 
    set_grid(  axs, gridOn[k], k)
    set_commaDecimal_with_precision(axs, floatPrec_xAxis[k], floatPrec_yAxis[k], k)

#align_labels(fig)
plt.tight_layout() #I think this works. Mostly bcs I use figure_width as the baseline for all measurements //2022-02-21
export_figure_as_pdf(filePathSaveFig)

plt.show()
print() #for new line


###-----###
### EOF ###
###-----###