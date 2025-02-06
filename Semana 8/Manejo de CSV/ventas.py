import csv


def read_csv_file(file_path):
  with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(row)

path_file = "./Test.csv"
read_csv_file(path_file)