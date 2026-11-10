###
# Program analyses the price of a product in an online store.
#

current_price = 140.00
previous_price = 200.00

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

price_reduction = ((previous_price - current_price) / previous_price) * 100

if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction:.0f}%")