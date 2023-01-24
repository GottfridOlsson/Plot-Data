##=============================================##
##     Project: PLOT DATA
##        File: CSV_handler.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-02-04
##     Updated: 2023-01-24
##       About: Imports data from a CSV-file.
##              Has functions for reading data
##              and getting the headers.
##              Also comvbining CSV files.
##=============================================##


## LIBRARIES ##

import pandas as pd


## CONSTANTS ##

CSV_DELIMITER = ','


## FUNCTIONS ##

def read(read_file_path, print_message=True):
    #print("In progress: Reading CSV" + CSV_filePath)
    CSV =  pd.read_csv(read_file_path, sep=CSV_DELIMITER)
    if print_message:
        print("DONE: Reading CSV: " + read_file_path)
    return CSV

# i'm not sure how to do this nicely. yet. //2022-02-04, 19:12
def write_DataFrame_to_CSV(DataFrame, write_file_path):
    print("In progress: Exporting DataFrame to CSV")
    DataFrame.to_csv(write_file_path, sep=CSV_DELIMITER, encoding='utf-8', index=False)
    print("Done: Writing DataFrame to CSV: " + write_file_path)

def combine_list_of_lists_and_header_to_DataFrame(list_of_lists, header):
    dataframe = pd.DataFrame(list_of_lists).transpose()
    dataframe.columns = header
    return dataframe

def get_header(CSV_data):
    return CSV_data.columns.values


def combine_CSV_files_to_one(output_path, paths):
    """Takes several CSV files and appends them columnwise to a new CSV file

    INPUT:
        output_path: path to where the outputted csv should go
        
        paths: paths to CSV files in array: [csv_path_1, csv_path_2, ..., csv_path_n]

    Code modified from: https://stackoverflow.com/questions/19945296/combining-csv-files-column-wise
    """

    headers = []
    columns = []

    for path in paths:

        CSV_i = read(path, print_message=False)
        headers_i = get_header(CSV_i)

        for header in headers_i:
            headers.append(header)
            columns.append(CSV_i[header])
    
    dataframe = combine_list_of_lists_and_header_to_DataFrame(columns, headers)
    write_DataFrame_to_CSV(dataframe, output_path)
    
    print(f"Successfully appended {len(paths)} CSV files to output path: '{output_path}'")
    





# EOF #