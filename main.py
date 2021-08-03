import csv

data = []

with open("dataset_2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
planet_data = data[1:]

for data_point in proper_name:
    data_point[2] = data_point[2].lower()


proper_name.sort(key=lambda proper_name: proper_name[2])


with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(prope_name)
