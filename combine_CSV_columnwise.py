import CSV_handler


# name of output file (TO CHANGE)
output_string = "TIF326_Tensile_test.csv"

#names of csv files to get columns from and print to output file (TO CHANGE)
raw_paths = [
    "TIF326_Group2-160C-2h_tensile-test.csv",
    "TIF326_Tensile_reference_material.csv"
]


unformatted_CSV = "raw_CSV\\"
formatted_paths = [unformatted_CSV + raw_paths[i] for i in range(len(raw_paths))]

formatted_CSV_folder = "CSV\\"
output_path = formatted_CSV_folder + output_string

CSV_handler.combine_CSV_files_to_one(output_path, formatted_paths)
print(f"Combined {len(raw_paths)} CSV files to one at path: {output_path}")