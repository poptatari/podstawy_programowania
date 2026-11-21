# The clothing.csv contains a list of clothing in stock. 
# Write a program that prints those products whose price 
# is less than 60 and whose stock is less than 40.

import csv

with open('clothing.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row['Price'])
        stock = int(row['Stock_Quantity'])

        if price < 60 and stock < 40:
            print(
                f"{row['Product_ID']}. {row['Product_Name']} "
                f"({row['Size']}, {row['Color']}) - "
                f"Price: {price}, Stock: {stock}"
            )