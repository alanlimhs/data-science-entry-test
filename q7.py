class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make, model, year): #initialize object attributes
        self.make = make #store the car's make inside variable
        self.model = model #store the car's model inside variable
        self.year = year #store the car's year inside variable

    def describe_car(self): #function to display car attributes
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

my_car = Car("Toyota", "Corolla", 2020) #define the attributes here
my_car.describe_car() #initialize function to print the attributes