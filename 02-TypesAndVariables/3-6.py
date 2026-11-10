###
# A program that calculates the distance to the horizon
# from a height given in meters.
#
import math

height = float(input('Enter height in meters: '))
distance = 3.57 * math.sqrt(height)
print(f'Your distance to the horizon is {distance}km.')