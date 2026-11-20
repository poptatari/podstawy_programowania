# Write a program that draws the function y = sin(x) 
# for an angle value in the range 0-360 degrees.

import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values (0 to 360 degrees)
for angle in range(0, 361):
    x.append(angle)

# create y values (convert degrees to radians first)
for angle in x:
    y.append(math.sin(math.radians(angle)))

# print chart
plt.plot(x, y)
plt.show()