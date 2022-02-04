## PLOT SCIENTIFIC DATA: MAIN PLOTTER                      ##
#----------------------------------------------------------##
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 18:15
#     Updated: 2022-02-04, 
#       About: Plot data in figures with matplotlib.
#              Functions are used to make figure look nice. 
#              Plot-settings as JSON. Export figure as PDF.
##---------------------------------------------------------##


## IMPORT LIBRARIES ##

import matplotlib as mpl            # to plot
from matplotlib import font_manager # to get CMU Serif
import matplotlib.pyplot as plt     # to plot
import matplotlib.ticker as tkr     # for comma in x- and y-axis

import CSV_handler 
import JSON_handler



## FUNCTIONS ##


def save_figure_as_pdf(filePath):
  plt.savefig(filePath + '.pdf')
  print("DONE: Exported PDF:" + filePath + ".pdf")

def set_CMU_serif_font(fontString, fontDirectory):
  # CMU Serif:  https://fontlibrary.org/en/font/cmu-serif
  font_dirs = fontDirectory
  font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
  for font_file in font_files:
      font_manager.fontManager.addfont(font_file)
  plt.rcParams['font.family'] = fontString

# main plotting function
def plot_errorbar(csv_data, xError, yError, num_datasets):
  cm = 1/2.54  # centimeters in inches
  fig, ax = plt.subplots(figsize = (c['figure_width']*cm, c['figure_height']*cm))
  for i in range(0, num_datasets):
    xCol_index = c['dataset'][i]['x_column'] - 1 #from human number to cpu index
    yCol_index = c['dataset'][i]['y_column'] - 1
    xData = csv_data[csv_header[xCol_index]]
    yData = csv_data[csv_header[yCol_index]]

    ax.errorbar(xData, yData, xError, yError,
      capsize         = c['dataset'][i]['errorbar_size'],
      capthick        = c['dataset'][i]['errorbar_capthickness'],
      elinewidth      = c['dataset'][i]['errorbar_linewidth'],
      marker          = c['dataset'][i]['marker_type'],
      markersize      = c['dataset'][i]['marker_size'],
      markeredgewidth = c['dataset'][i]['marker_thickness'],
      markerfacecolor = c['dataset'][i]['marker_facecolor'],
      linestyle       = c['dataset'][i]['line_style'],
      linewidth       = c['dataset'][i]['line_width'],
      color           = c['dataset'][i]['line_color'], 
      label           = c['dataset'][i]['datalabel'])
     
  ax.set_xlabel(c['label_xAxis'], fontsize=c['fontSize_axis'])
  ax.set_ylabel(c['label_yAxis'], fontsize=c['fontSize_axis'])
  ax.tick_params(labelsize=c['fontSize_axis'])
  #ax.set_xticklabels(xTickLabels, fontsize=xTickSize)
  #ax.set_yticklabels(yTickLabels, fontsize=yTickSize)
  ax.grid(c['grid'])

  if c['legend_on']:
    plt.legend(fontsize=c['fontSize_legend'], framealpha=c['legend_alpha'], loc=c['legend_position'])

  if c['invert_xAxis']: ax.invert_xaxis()
  if c['invert_xAxis']: ax.invert_yaxis()

  ax.set( xlim=(c['xlim_min'], c['xlim_max']) )
  ax.set( ylim=(c['ylim_min'], c['ylim_max']) )

  #plt.rc('axes', unicode_minus=False) #gets rid of error: "Glyph 8722 missing from current font" #works but is ugly!
  # https://github.com/matplotlib/matplotlib/issues/17007
  # https://github.com/matplotlib/matplotlib/pull/18397

  def set_axis_to_comma_with_precision(xAxis_precision, yAxis_precision):
    xFormatString = '{:.' + str(xAxis_precision) + 'f}'
    yFormatString = '{:.' + str(yAxis_precision) + 'f}'
    ax.get_xaxis().set_major_formatter( tkr.FuncFormatter(lambda x, pos: xFormatString.format(x).replace('.', ',')) )
    ax.get_yaxis().set_major_formatter( tkr.FuncFormatter(lambda x, pos: yFormatString.format(x).replace('.', ',')) )
    
  set_axis_to_comma_with_precision(c['floatPrecision_xAxis'], c['floatPrecision_yAxis'])
   # Modified from: https://stackoverflow.com/questions/8271564/matplotlib-comma-separated-number-format-for-axis
  plt.tight_layout() #pad=0

  #plt.tight_layout(pad=1.08, h_pad=None)

def plot_image(image):
  cm = 1/2.54 #cm per inch
  fig, ax = plt.subplots(figsize=(c['figure_width']*cm, c['figure_height']*cm*0.3), squeeze=True)
  # TODO: magic number in figure_height should be 0.15 when figure height is 14 //2022-02-03, 16:00
  plt.imshow(image, interpolation=None, origin='lower', aspect='auto')
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  #plt.tight_layout(pad=1.08, h_pad=None)




## MAIN ##
CSV_readFilePath = "test.csv"
CSV_data = CSV_handler.read_CSV(CSV_readFilePath)
print(CSV_data)




### EOF ###




## SOURCES
  # https://matplotlib.org/stable/tutorials/introductory/usage.html
# for curve-fitting
# https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509



### EOF ###