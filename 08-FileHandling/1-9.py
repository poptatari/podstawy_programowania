with open('it_company.csv', 'r') as file:
    lines = file.read().splitlines()

count = 1
for line in lines[1:]:  # Skip header
    row = line.split(',')
    if row[2] == "Software Engineer":
        print(f"{count}. {row[1]} {row[0]} ({row[3]})")
        count += 1