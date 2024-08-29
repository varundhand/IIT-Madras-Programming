#! Class is blueprint or template for creating objects.
# It defines a set of attributes (data) and methods (functions) that the objects created from the class will have. 

#! Object is an instance of a class.
# It is a concrete entity based on a class, and made up of attributes and methods defined in the class.

# class Student:
#     roll_no = None
#     name = None

# s0 = Student() # Creating an object of the class Student, Student is the 'constructor' of the class
# s0.roll_no = 1
# s0.name = 'Varun'

# print(s0.roll_no, s0.name)

#! self is the first parameter in every single method of a class.
#! it is a reference to the object itself.
class Student:
    global_roll = 10 # this is a class variable and is shared by all the objects of the class

    def __init__(self,roll_no,name,marks): # this is the constructor of the class and is used to set the initial state of the object
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(self.roll_no, self.name)

    def pass_or_fail(self):
        if self.marks > 40:
            print('Pass')
        else:
            print('Fail')

s0 = Student(1, 'Varun', 99)
# s0.display()   #! Output: 1 Varun
# s0.pass_or_fail() #! Output: Pass

# print(Student.global_roll) #! Output: 10

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is driving.")

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", "Red")

# Accessing attributes and methods
# print(my_car.make)  #! Output: Toyota
# print(my_car.model)  #! Output: Camry
# print(my_car.color)  #! Output: Red

# my_car.drive()  #! Output: The Red Toyota Camry is driving.

