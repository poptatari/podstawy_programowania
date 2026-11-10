###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = float(input('Radius: '))
pi = 3.14
# calculate area 
area = pi * radius ** 2
# calculate circumference 
circumference = 2 * pi * radius
# print results
print(f'Area: {area:.2f}, circumference: {circumference:.2f}')