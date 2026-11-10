###
# EAN-13 (European Article Number) is a barcode 
# for marking goods. The first 3 digits (590) usually 
# indicate goods manufactured in Poland. Write a 
# program that checks whether the EAN-13 number 
# entered from the keyboard consists of exactly 
# 13 characters (digits). Print a message if the 
# number is correct. Additionally, only when the 
# article number is correct, print a message when 
# the product was manufactured in Poland.
#

article_number = input('Enter EAN-13 article number: ')

if len(article_number) == 13 and article_number.isdigit():
    print('Article number is correct')
    if article_number[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')

