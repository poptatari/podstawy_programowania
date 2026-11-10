###
# In one of the online stores, a 25% discount is charged 
# for each product purchased over two. Write a program that 
# calculates the amount to be paid. Read the number of 
# purchased products and the product price from the keyboard. 
#

number_of_products = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))

if number_of_products <= 2:
    amount = number_of_products * product_price
else:
    amount = 2 * product_price + 0.75 * product_price * (number_of_products - 2)

print(f'Amount to pay: {amount}') 