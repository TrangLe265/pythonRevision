class Person:
    def __init__(self, name):
        self.name=name

    def hello(self):
        print(f"Hello, my name is {self.name}!")
    
p = Person('Matti')
print(p.hello())

"""
Restaurant
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:
For example:

Test	Result
restaurant = Restaurant('Kotipizza', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
Kotipizza
pizza
Kotipizza serves wonderful pizza.
Kotipizza is open. Come on in
"""

class Restaurant: 
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type= cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")


"""
User
Make a class called `User`. Create the following attributes: first_name and last_name, email, and location. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.

"""

class User:
    def __init__(self,first_name,last_name,user_name, email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name=user_name
        self.email = email
        self.location = location
    
    def describe_user(self):
        print(f"Name:{self.first_name} {self.last_name} \nUsername: {self.user_name} \nEmail: {self.email} \nLocation: {self.location}")

    def greet_user(self):
        print(f"Welcome back {self.user_name}")
