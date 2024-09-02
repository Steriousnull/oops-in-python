# Define a class named 'Person'
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name  # Attribute for storing the name
        self.age = age    # Attribute for storing the age

    # Method to display the person's information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Method to celebrate the person's birthday
    def celebrate_birthday(self):
        self.age += 1  # Increment the age by 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Create instances (objects) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing the attributes and methods of the objects
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25

# Celebrating a birthday
person1.celebrate_birthday()  # Output: Happy Birthday, Alice! You are now 31 years old.
person2.celebrate_birthday()  # Output: Happy Birthday, Bob! You are now 26 years old.
