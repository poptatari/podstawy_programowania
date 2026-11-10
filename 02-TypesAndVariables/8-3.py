###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# get user's input
celsius = float(input('Temperature in Celsius: '))
# convert to Kelvin
kelvin = celsius + 273.15
# convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

print(f'Kelvin: {kelvin}, Fahrenheit: {fahrenheit}')