##=============================================##
##     Project: PLOT DATA
##        File: CSV_handler.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-02-04, 18:38
##     Updated: 2022-08-03, 14:42
##       About: Imports data from a CSV-file.
##              Has functions for reading data
##              and getting the headers.
##=============================================##


## LIBRARIES ##

import pandas as pd


## CONSTANTS ##

CSV_DELIMITER = ','


## FUNCTIONS ##

def read(read_file_path):
    #print("In progress: Reading CSV" + CSV_filePath)
    CSV =  pd.read_csv(read_file_path, sep=CSV_DELIMITER)
    print("DONE: Reading CSV: " + read_file_path)
    return CSV

# i'm not sure how to do this nicely. yet. //2022-02-04, 19:12
def write_DataFrame_to_CSV(DataFrame, write_file_path):
    print("In progress: Exporting DataFrame to CSV")
    DataFrame.to_csv(write_file_path, sep=CSV_DELIMITER, encoding='utf-8', index=False)
    print("Done: Writing DataFrame to CSV: " + write_file_path)
    #raise Exception("This function is not yet coded. Sorry. //2022-02-04")

def combine_list_of_lists_and_header_to_DataFrame(list_of_lists, header):
    dataframe = pd.DataFrame(list_of_lists).transpose()
    dataframe.columns = header
    return dataframe

def get_header(CSV_data):
    return CSV_data.columns.values


# EOF #