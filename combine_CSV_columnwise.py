import CSV_handler


# name of output file (TO CHANGE)
output_string = "TIF320_A4_T1_Au-Pt-Rh_energy_vs_lattice-parameter_fit_step0.01.csv"

#names of csv files to get columns from and print to output file (TO CHANGE)
raw_paths = [
    "TIF320_A4_T1_Au_energy_vs_lattice_parameter_step0.01_fit.csv",
    "TIF320_A4_T1_Pt_energy_vs_lattice_parameter_step0.01_fit.csv",
    "TIF320_A4_T1_Rh_energy_vs_lattice_parameter_step0.01_fit.csv"
]


unformatted_CSV = "raw_CSV\\"
formatted_paths = [unformatted_CSV + raw_paths[i] for i in range(len(raw_paths))]

formatted_CSV_folder = "CSV\\"
output_path = formatted_CSV_folder + output_string

CSV_handler.combine_CSV_files_to_one(output_path, formatted_paths)
print(f"Combined {len(raw_paths)} CSV files to one at path: {output_path}")