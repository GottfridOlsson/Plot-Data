import CSV_handler

# name of output file
output_string = "A1_T4_comparison_hydrogen_wavefunction_T1_T4.csv"

#names of csv files to get columns from and print to output file
raw_paths = [
    "A1_Task1_hydrogen_wavefunction_4gaussians_as_basis_N=1000.csv", 
    "A1_Task4_helium_wavefunction_N=1000.csv", 
]


unformatted_CSV = "raw_CSV\\"
formatted_paths = [unformatted_CSV + raw_paths[i] for i in range(len(raw_paths))]

formatted_CSV_folder = "CSV\\"
output_path = formatted_CSV_folder + output_string

CSV_handler.combine_CSV_files_to_one(output_path, formatted_paths)