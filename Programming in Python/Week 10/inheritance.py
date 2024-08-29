#! Inheritance 
#! Inheritance is a way of creating a new class for using details of an existing class without modifying it.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

#! Person is the parent/super class and Student and Employee are the child/sub classes

class Student(Person): # Student class inherits properties from Person class
    def __init__(self, name, age, marks):
        super().__init__(name, age) # super() is used to call the constructor of the parent class
        self.marks = marks

    def display(self):
        super().display()
        print("Marks:", self.marks)
        print('--------------')

s0 = Student('Varun', 21, 99)
s0.display() #! Output: Marks: 99

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        super().display()
        print("Salary:", self.salary)

s1 = Employee('Varun', 21, 1000000)
s1.display() #! Output: Salary: 1000000

class MyClass:
    def __init__(self, value):
        self.__private_attribute = value  # Private attribute

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()  # Can be called within the class

# Create an object of MyClass
obj = MyClass(10)

# Accessing private attribute (this will raise an AttributeError)
print(obj.__private_attribute)

# Accessing private method (this will raise an AttributeError)
obj.__private_method()