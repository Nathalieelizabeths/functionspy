class Student:
    school="Akirachix"
    def __init__(self,firstname,lastname,age,country):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country

    def greet_student(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}"

    def show_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def year_of_birth(self):
        current_year=2023
        return current_year-self.age

    def show_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"

#how to create a class that can represent all students(instance variables)
#1) Update the Student Class to include these attributes - first_name, last_name, age, country
     #- Add these methods to the Student class
            # - show_full_name
            # - year_of_birth
             #- show_initials

#2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
#Car
#Fruit
#Account

    

