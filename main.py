# Warmup Program
# Create a class Called Person, which takes name, address, age.
# Create a method which can display this information when done person.display_info()

class Person:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age

    def display_info(self):
        print(f"Name:{self.name}, address:{self.address}, age:{self.age}")

person=Person("Roshani","Mahendranagar",21)
person.display_info()
      

        
