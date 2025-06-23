import csv
import os

file_path = os.path.join("C:\\Users\\rabin\\Desktop", "lab.csv")

data_to_write = [{"name": "Rabin", "age": 100}, {"name": "Rahul", "age": 25}]

with open(file_path, "w", newline="") as file_obj:
    header = ["age"]
    writer = csv.DictWriter(file_obj, fieldnames=header)
    writer.writeheader()
    writer.writerows(data_to_write)
