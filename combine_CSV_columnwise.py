import CSV_handler


# name of output file (TO CHANGE)
output_string = "TIF326_Tensile_test_LDPE_CM_MD_strain_percent_stress_MPa.csv"

#names of csv files to get columns from and print to output file (TO CHANGE)
raw_paths = [
    "TIF326_Tensile_testing_LDPE_CD_Data_CD_strain_percent_stress_MPa.csv",
    "TIF326_Tensile_testing_LDPE_MD_Data_MD_strain_percent_stress_MPa.csv"
]


unformatted_CSV = "raw_CSV\\"
formatted_paths = [unformatted_CSV + raw_paths[i] for i in range(len(raw_paths))]

formatted_CSV_folder = "CSV\\"
output_path = formatted_CSV_folder + output_string

CSV_handler.combine_CSV_files_to_one(output_path, formatted_paths)
print(f"Combined {len(raw_paths)} CSV files to one at path: {output_path}")