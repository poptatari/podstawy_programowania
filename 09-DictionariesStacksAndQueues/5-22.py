# Write a program that takes data from the keyboard 
# about a purchased product, then saves the product 
# data in the product.json file. 

import json

product = {}

# Read product data from keyboard
product["name"] = input("Enter product name: ")
product["price"] = round(float(input("Enter product price: ")), 2)
paid_input = input("Is the product paid? (yes/no): ").strip().lower()
product["paid"] = paid_input == "yes"

# Save product data to json file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)