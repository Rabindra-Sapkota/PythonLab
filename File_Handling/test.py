import csv

data = [{"Name": "Rabin", "Age": 21}, {"Name": "Rahul", "Age": 25}]

with open("test_csv_write.csv", "w", newline="") as file_obj:
    header = ["Age"]
    writer = csv.DictWriter(file_obj, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
