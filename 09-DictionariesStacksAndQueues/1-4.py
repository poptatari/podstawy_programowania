person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

# Create a program that:

# Displays name
print(f'Name: {person["name"]}')

# Displays hobby
print(f'Hobby: {", ".join(person["hobby"])}')

# Displays the entire contents of the dictionary
print(person)

# Changes surname to 'Nowak'
person["surname"] = "Nowak"
print(f'Surname: {person["surname"]}')

# Changes person's marriage status
person["married"] = False
print(f'Married: {person["married"]}')

# Adds gender: 'male'
person["gender"] = "male"
print(f'Gender: {person["gender"]}')

# Adds a new hobby: 'bicycle'
person["hobby"].append("bicycle")
print(f'{person["hobby"]}')

# Adds work phone to existing phones: '313131444'
person["phone"]["work"] = "313131444"
print(person["phone"])

# Displays the entire contents of the dictionary (iterate over dictionary items)
for key, value in person.items():
    print(f'{key} : {value}')