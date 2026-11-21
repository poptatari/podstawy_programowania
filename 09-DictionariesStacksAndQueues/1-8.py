price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# 1. Print products and prices before the discount
print("Prices before discount:")
for item, price in price_list.items():
    print(f"{item}: {price}")

# 2. Print total value before the discount
total_before = round(sum(price_list.values()), 2)
print(f"Total value before discount: {total_before}\n")

# 3. Modify the price list with a 10% discount
for item in price_list:
    price_list[item] = round(price_list[item] * 0.90, 2)

# 4. Print products and prices after the discount
print("Prices after 10% discount:")
for item, price in price_list.items():
    print(f"{item}: {price}")

# 5. Print total value after the discount
total_after = round(sum(price_list.values()), 2)
print(f"Total value after discount: {total_after}")