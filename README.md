# Plot-Data
Updated: 2022-04-07, 09:57
Plots data from CSV-file.
Settings specified in JSON-file.
### UNDER CONSTRUCTION ###


TODO FUF050:
    - log scale y- and x-axis

TODO:
-1. errorbar color (?)
0. 'log_yscale' in JSON (y and x) 
1. Program different plot types (and introduce changes to JSON as necessary):
    Most "urgent"/resonable:  plot, **scatter**, bar, contour(f), quiver, hist, **errorbar**, pie, (https://matplotlib.org/devdocs/plot_types/index.html) 
2. Program exceptions/raise errors for wrongly configured JSON-files.
3. Program GUI (to choose and possible 'lock': CSV, JSON and output filename and path, to easily change and save JSON and run PlotData.py again to see new plot (or update plot every X seconds or have a refresh button)). Perhaps being able to change things for different yDatasets per subplot and then click save to save the settings to a new JSON file (Optimal: allt är GUI, läsa in CSV och pilla runt allt annat, sen spara konfig till JSON).
4. Small fixes: fix ratio between textsize and figure_width, and also line_width and figure_width.


Note:
-JSON must be configured with UTF-8 encoding. Most notably for Swedish words is that 'å', 'ä', and'ö' must be encoded with "\u00e5", "\u00e4", and "\u00f6", respectively.
 -Headers in CSV must be unique (no duplicate headernames)
 -xDataCols given in JSON must be paired with corresponding yDataCols per subplot (that is to say that you need N number of xDataCols [ {"1": x}, {"2" : y}, ..., {"N" : w} ] if you have N number of yDataCols [ {"1": x}, {"2" : y}, ..., {"N" : w} ])
 - 
### UNDER CONSTRUCTION ###
