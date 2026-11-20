# Write a program that draws the graph of the function 
# f(x)=x2-3. 

import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100, 101):
    x = x + [n]

# create y values
for n in x:
    y = y + [n**2 - 3]

# print chart
plt.plot(x, y)
plt.show()