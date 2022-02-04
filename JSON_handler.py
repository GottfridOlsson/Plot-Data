## PLOT SCIENTIFIC DATA: JSON HANDLER                      ##
#----------------------------------------------------------##
#      Author: GOTTFRID OLSSON 
#     Created: 2022-02-04, 19:18
#     Updated: 2022-02-04, 
#       About: Read and write to JSON-files.
##---------------------------------------------------------##


## IMPORT LIBRARIES ##

import json                         # to save/write to JSON





## FUNCTIONS ##

def read_JSON(readFilePath):
    with open(readFilePath, "r") as jsonfile:
        JSON = json.load(jsonfile)
    print("DONE: Reading JSON: " + readFilePath)
    return JSON

def write_JSON(writeFilePath, JSON_data):
  JSON = json.dumps(JSON_data)
  with open(writeFilePath, "w") as jsonfile:
    jsonfile.write(JSON)
  print("DONE: Writing JSON: " + writeFilePath)





## FUNCTIONS ##

JSON_readFilePath = "jtest.json"
JSON_writeFilePath = "jtest2.json"
JSON_data = read_JSON(JSON_readFilePath)
print(JSON_data['created'])
print(JSON_data['updated'])
print(JSON_data['filename'])
write_JSON(JSON_writeFilePath, JSON_data)

