products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

# Write a program that prints:
# a list of products and the quantity
# the total number of products in the store

total = 0
for key, value in products.items():
    print(f'Product: {key}, quantity: {value}')
    total += value

print(f'Total number of products: {total}')