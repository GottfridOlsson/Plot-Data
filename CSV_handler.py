## PLOT SCIENTIFIC DATA: CSV HANDLER                       ##
#----------------------------------------------------------##
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 18:38
#     Updated: 2022-02-06, 20:47
#       About: Imports CSV- and prints data to a CSV-file.
#              Has functions for moving, splitting, removing,
#              and altering data in CSV-file.
##---------------------------------------------------------##

## LIBRARIES ##

import pandas as pd
#import csv


## CONSTANTS ##

CSV_DELIMITER = ','

## FUNCTIONS ##

def read_CSV(readFilePath):
    #print("In progress: Reading CSV" + CSV_filePath)
    CSV =  pd.read_csv(readFilePath, sep=CSV_DELIMITER)
    print("DONE: Reading CSV: " + readFilePath)
    return CSV

# i'm not sure how to do this nicely. yet. //2022-02-04, 19:12
def write_CSV(CSV_data, writeFilePath):
    #print("In progress: Exporting CSV")
    #headers = get_header(CSV_data)
    #CSV_data.to_csv(writeFilePath)
    #with open(writeFilePath, 'w', newline='') as csvfile:
    #    CSV = csv.writer(csvfile, delimiter = CSV_DELIMITER)
    #    CSV.writerows(CSV_data)
    #print("Done: Writing CSV: " + writeFilePath)
    raise Exception("This function is not yet coded. Sorry. //2022-02-04")

def get_header(CSV_data):
    return CSV_data.columns.values


## MAIN ##

#CSV_readFilePath = "CSV/testdata1.csv"
#CSV_writeFilePath = "test2.csv"


#CSV_data = read_CSV(CSV_readFilePath)
#print(CSV_data)
#CSV_header = get_header(CSV_data)
#print(CSV_header)

