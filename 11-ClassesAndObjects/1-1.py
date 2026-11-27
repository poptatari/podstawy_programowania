# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.major = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.major = "English"
    student2.name = "Olivia"
    student2.age = 21
    student2.major = "Physics"
    student3.name = "Elle"
    student3.age = 22
    student3.major = "Law"
    
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, major: {student1.major}')
    print(f'{student2.name}, {student2.age} years old, major: {student2.major}')
    print(f'{student3.name}, {student3.age} years old, major: {student3.major}')

if __name__ == "__main__":
    main()