###
# Let x and y denote the coordinates of a point 
# on the plane. Write a program that determines 
# in which quadrant of the coordinate system the point 
# P(x, y) is located or on which axis it is located, 
# or that it is located in the position (0,0) of the 
# coordinate system. 
#

x = 5
y = 2

if x == 0 and y == 0:
    location = 'located in the position (0,0)'
elif x == 0:
    location = 'on the y axis'
elif y == 0:
    location = 'on the x axis'
elif x > 0 and y > 0:
    location = 'in the first quadrant'
elif x < 0 and y > 0:
    location = 'in the second quadrant'
elif x < 0 and y < 0:
    location = 'in the third quadrant'
else:
    location = 'in the fourth quadrant'

print(f'Point P({x},{y}) is {location} of the coordinate system.')