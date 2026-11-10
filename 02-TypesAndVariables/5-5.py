###
# A program that calculates the discounted
# produce price.
#

price = float(input('Enter price: '))
discount = float(input('Enter discount %: ')) / 100
new_price = price - price * discount

print(f'Price with discount {new_price:.2f}')
print(f'Reduction: {price - new_price:.2f}')