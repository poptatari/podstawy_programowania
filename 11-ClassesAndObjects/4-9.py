# This program defines a class `C` that stores an employee's 
# first name, last name, age, and years of seniority. 
# It generates a compact identifier combining the employee's 
# surname, first initial, and seniority—formatted in uppercase 
# if the employee is 18 or older, and lowercase if they are under 18.

class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        text = f"{self.surname}{self.name[0]}{self.seniority}"
        if self.age >= 18:
            return text.upper()
        return text.lower()


# Sample test cases
emp1 = C("Anna", "May", 17, 7)
emp2 = C("George", "Brown", 21, 4)

print(emp1)
print(emp2)