###
# Write a program that creates the following pattern. Sample result:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

i = 0

while i < 5:
    star = '* ' * i
    print(star)
    i += 1

while i > 0:
    star = '* ' * i
    print(star)
    i -= 1