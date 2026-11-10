###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

total_inches = cm / 2.54
# calculate the number of feet
feet = total_inches // 12
inches = total_inches % 12

print(f'I am {cm}cm tall, i.e. {round(feet)} feet and {round(inches)} inches')