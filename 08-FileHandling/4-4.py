# Write a program that displays the first five lines 
# from the it_company.csv file and then prints 'Press 
# Enter key...' in the next line and waits for the Enter 
# key to be pressed. The program repeats printing the next
# five lines from the file, waiting for the Enter key to 
# be pressed each time.

with open('it_company.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for i in range(0, len(lines), 5):
    # Print the next slice of up to 5 lines
    for line in lines[i:i + 5]:
        print(line, end="")
    
    # Wait for Enter if there are still more lines left to display
    if i + 5 < len(lines):
        input("Press Enter key...")