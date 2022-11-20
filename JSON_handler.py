##======================================================##
##     Project: PLOT DATA
##        File: JSON_handler.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-02-04, 19:18
##     Updated: 2022-08-17, 11:29
##       About: Read and write to JSON-files using json.
##======================================================##


## LIBRARIES ##

import json


## FUNCTIONS ##

def read(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as json_file: # encoding='utf-8-sig' solved problem where functioning .json got error: "json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)" //2022-08-17
        JSON = json.load(json_file)
    print("DONE: Reading JSON: " + file_path)
    return JSON

def write(file_path, JSON_data):
  with open(file_path, 'w', encoding='utf-8') as json_file:
    #jsonfile.write(JSON) #commented out //2022-02-20
    json.dump(JSON_data, json_file, ensure_ascii=False) #changed from "dumps()" to "dump()" and added encoding 'utf-8' and ensure_ascii=False //2022-02-20
  print("DONE: Writing JSON: " + file_path)

# EOF #