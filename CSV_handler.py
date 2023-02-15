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
    




def print_arrays_to_CSV(path_to_CSV_file, *args, print_message=False):
    """Prints array(s) with corresponding header(s) to a file with comma separated values (CSV)

        Input:
            path_to_csv: the path to where the CSV file should be printed

            *args: array(s) and corresponding header(s) in this format:
                    header_1, array_1, header_2, array_2, ..., header_n, array_n

            print_message: displays a message "Sucessfully printed CSV file (...)" (default False)

        Output:
            A CSV file with utf-8 formatting at path_to_csv, with the array(s) as column(s) and corresponding header(s)

            Lines larger down than the length of array(s) are printed as ',' without an empty space [Plot-Data once complained when there was an empty space]
        
        Warnings:
            ValueError: if the length of args is not even

            ValueError: if the number of array(s) is not equal to the number of header(s)
    """

    if len(args) % 2 != 0:
        raise ValueError("WARNING: the number of arrays + headers is not even. This may cause errors in printing!")
    
    arrays, headers, lines_per_array = [], [], []

    for index, arg in enumerate(args):

        if index % 2 == 0:
            headers.append(arg)
        else:
            arrays.append(arg)
            lines_per_array.append(len(arg))
      

    if len(arrays) != len(headers):
        raise ValueError("WARNING: the number of arrays does not equal the number of headers!")


    with open(path_to_CSV_file, 'w', encoding="utf-8") as CSV_file:
        
        # Print header line
        for header_number, header in enumerate(headers):
            CSV_file.write(str(header))

            # print comma separator between values (CSV) or newline at end of line
            if header_number != len(headers) - 1:
                CSV_file.write(",")
            else:
                CSV_file.write("\n")

        # Print CSV data
        for line in range(max(lines_per_array)):

            for array_number, array in enumerate(arrays):
                # print value of array at line, or if outside length of aray print nothing
                try:
                    CSV_file.write(str(array[line]))
                except:
                    CSV_file.write(str("")) 
                
                # print comma separator between values (CSV) or newline at end of line
                if array_number != len(arrays) - 1:
                    CSV_file.write(",")
                else:
                    CSV_file.write("\n")
    

    if print_message:
        print(f"Successfully printed {len(arrays)} arrays to CSV file at path: '{path_to_CSV_file}'")

# EOF #