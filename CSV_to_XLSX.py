import pandas as panda

print("Enter the directory of csv file: ")
path = input()
print("Enter name of csv file: ")
name_of_file = input()
raw_string = r"{}".format(path)
path = f"{raw_string}\\{name_of_file}.csv"
# Read the CSV File
open_file = panda.read_csv(r"{}".format(path))
path = f"{raw_string}\\{name_of_file}.xlsx"
# Convert the CSV File to XLSX in the same path
open_file.to_excel(r"{}".format(path))
