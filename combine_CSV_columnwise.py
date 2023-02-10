import CSV_handler

# name of output file
output_string = "TIF320_A3_RDF_Na-O_our_different_simulation_timeintervals_and_their.csv"

#names of csv files to get columns from and print to output file
raw_paths = [
    "TIF320_A3_RDF_Na-O_our_simulation_different_simulation_timeintervals.csv",
    "TIF320_A3_RDF_Na-O_our_their.csv"
]


unformatted_CSV = "raw_CSV\\"
formatted_paths = [unformatted_CSV + raw_paths[i] for i in range(len(raw_paths))]

formatted_CSV_folder = "CSV\\"
output_path = formatted_CSV_folder + output_string

CSV_handler.combine_CSV_files_to_one(output_path, formatted_paths)
print(f"Combined {len(raw_paths)} CSV files to one at path: {output_path}")