##=============================================##
##     Project: PLOT DATA
##        File: functions.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-06-21, 17:50
##     Updated: 2022-06-21, 17:50
##       About: Helper functions for plotting.
##=============================================##

import matplotlib.pyplot
import matplotlib as plt


def cm_2_inch(cm):
    return cm/2.54


def set_LaTeX_and_CMU(LaTeX_and_CMU_on):
    if LaTeX_and_CMU_on:
        plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif", 
    "font.serif" : ["Computer Modern Roman"]
    })
    print("DONE: Set LaTeX and CMU to: " + str(LaTeX_and_CMU_on))


def set_font_size(axis, tick, legend):
    plt.rc('font',   size=axis)      #2022-06-21: not sure what the difference is, to test later on!
    plt.rc('axes',   titlesize=axis) #2022-06-21: not sure what the difference is, to test later on!
    plt.rc('axes',   labelsize=axis) #2022-06-21: not sure what the difference is, to test later on!
    plt.rc('xtick',  labelsize=tick)
    plt.rc('ytick',  labelsize=tick)
    plt.rc('legend', fontsize=legend)
    print("DONE: Set font sizes (axis, tick, legend): " + str(axis) + ", " + str(tick) + ", " + str(legend))


def set_axis_labels(ax, xLabel, yLabel, axNum):
    ax.set_xlabel(str(xLabel))
    ax.set_ylabel(str(yLabel))
    print("DONE: Set x- and y-label axs: " + str(axNum))


def set_legend(ax, legendOn, alpha, location, axNum):
      if legendOn:
            ax.legend(framealpha=alpha, loc=location)
      print("DONE: Set legend on axs: " + str(axNum))


def set_grid(ax, grid_major_on, grid_major_linewidth, grid_minor_on, grid_minor_linewidth, axNum): #TODO: subdivisions?
      if grid_major_on:
        ax.grid(grid_major_on, which='major', linewidth=grid_major_linewidth) 
      if grid_minor_on:
        ax.minorticks_on()
        ax.grid(grid_minor_on, which='minor', linewidth=grid_minor_linewidth)
      print("DONE: Set gridMajor = " + str(grid_major_on) +" and gridMinor = "+ str(grid_minor_on)+  " on axs: " + str(axNum))


def set_axis_scale(ax, xScale_string, yScale_string, axNum):
    ax.set_xscale(xScale_string)
    ax.set_yscale(yScale_string)
    print("DONE: Set x-axis scale to " + str(xScale_string) + " and y-axis scale to " + str(yScale_string) + " on axs: " + str(axNum))


def set_axis_limits(ax, xmin, xmax, ymin, ymax, axNum):
    if not xmin: xmin = None
    if not xmax: xmax = None
    if not ymin: ymin = None
    if not ymax: ymax = None
    
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    print("DONE: Set limits to x=(" + str(xmin) + ", " + str(xmax)+ ") and y=(" + str(ymin) + ", " + str(ymax)+ ") on axs: " + str(axNum))


def set_comma_decimal_with_precision(ax, xAxis_precision, yAxis_precision, axNum):
            # Modified from: https://stackoverflow.com/questions/8271564/matplotlib-comma-separated-number-format-for-axis
    xFormatString = '{:.' + str(xAxis_precision) + 'f}'
    yFormatString = '{:.' + str(yAxis_precision) + 'f}'
    ax.get_xaxis().set_major_formatter( plt.ticker.FuncFormatter(lambda x, pos: xFormatString.format(x).replace('.', ',')) )
    ax.get_yaxis().set_major_formatter( plt.ticker.FuncFormatter(lambda x, pos: yFormatString.format(x).replace('.', ',')) )
    print("DONE: Set comma as decimalseparator on with precision: X: "+str(xAxis_precision)+", Y: "+str(yAxis_precision) + " on axs: "+str(axNum))


def set_layout_tight(fig):
    fig.tight_layout()
    print("DONE: Set tight layout")


def align_labels(fig):
    fig.align_labels()
    print("DONE: Aligned labels")
    

def export_figure_as_pdf(filePath):
    matplotlib.pyplot.savefig(filePath, format='pdf', bbox_inches='tight')#, metadata={"Author" : "Gottfrid Olsson", "Title" : "", "Keywords" : "Created with PlotData by Gottfrid Olsson"}) ##this could be implemented in the future, 2022-06-21
    print("DONE: Exported PDF: " + filePath)
