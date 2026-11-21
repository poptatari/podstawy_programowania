# A traffic camera records passing vehicles. The camera 
# saves their registration numbers in the file vehicle.txt.
# Write a program that calculates and prints how many 
# registered cars come from each province of Poland.

import csv

provinces = {}
vehicle_counts = {}

# Load letter-to-province mappings and initialize counts
with open('province.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip header row ('Letter,Name')
    for letter, name in reader:
        provinces[letter] = name
        vehicle_counts[name] = 0

# Read registration numbers and count vehicles per province
with open('vehicle.txt', mode='r', encoding='utf-8') as txt_file:
    for line in txt_file:
        plate = line.strip()
        if plate:
            first_letter = plate[0]
            if first_letter in provinces:
                province_name = provinces[first_letter]
                vehicle_counts[province_name] += 1

# Display the results
for province, count in vehicle_counts.items():
    print(f"{province}: {count}")