##====================================================##
##     Project: PLOT DATA
##        File: absolute_path.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-10-27, 09:52
##     Updated: 2022-10-27, 09:52
##       About: Get absolute path of current file to
##              avoid error.
##====================================================##


#---------------#
#    IMPORTS    #
#---------------#

import os

def get_current_absolute_path():
    return os.path.abspath(os.path.dirname(__file__))