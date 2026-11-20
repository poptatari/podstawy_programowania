# Define a function time_string(hours, minutes, time_format) that, 
# given the number of hours (0..23) and the number of minutes (0..59), 
# returns a string specifying the time in the given format 
# ('24' for 24-hour time and '12' for 12-hour time).

def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}" # format the time as HH:MM
    elif time_format == '12':
        period = "AM" if hours < 12 else "PM"
        hour_12 = hours % 12 or 12
        return f"{hour_12}:{minutes:02d} {period}"

print(time_string(1, 30, '24'))