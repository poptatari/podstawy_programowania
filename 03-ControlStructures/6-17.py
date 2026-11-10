###
# Write a program that allows you to convert 
# time in 24-hour format to 12-hour format. The time 
# in 24-hour format (hh:mm) is read from the keyboard.
#

time = input("Enter time (24-hour format): ")

hours, minutes = time.split(":")
hours = int(hours)

if hours == 0:
    hours = 12
    period = "am"
elif hours < 12:
    period = "am"
elif hours == 12:
    period = "pm"
else:
    hours -= 12
    period = "pm"

print(f"Time in 12-hour format: {hours}:{minutes}{period}")