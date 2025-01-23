


# Create a Function: Turn this logic into a function called suggest_destination(budget) that:

# Accepts budget as an argument.
# Returns the suggestion as a string.
from budgetFunction import bugetFunction 
from calculator import calculator  
from calculator import add    
from weather_advice import advice
from shopping_list import shoppinglist
from TemperatureConverter import celsius_to_fahrenheit
from TemperatureConverter import  fahrenheit_to_celsius
from inventory import inventory
from password import validate_password
print(bugetFunction(300) )
print(calculator(10,5))
print(add(10,5))
print (advice("rainy"))
print (shoppinglist("carrots"))
print (celsius_to_fahrenheit(16))
print(fahrenheit_to_celsius(67))
print(inventory("apples"))
print(validate_password("char168"))
#-----------------------------------------------------------------git--------------------------------------

# Instructions for Students:

# Refactor this code by creating a function for each arithmetic operation (e.g., add, subtract, etc.).
# Make a Calculator class that contains these functions as methods.
# Ensure that division checks for zero before attempting the operation.
# Move the arithmetic logic into a file named calculator.py.

####################################################################################################
# Instructions for Students:

# Create a function that takes weather as an argument and returns the appropriate advice.
# Optionally, create a class WeatherAssistant with a method for weather advice.
#Move the weather advice logic into a file named weather_advice.py.



# Instructions for Students:

# Refactor this code by creating functions to:
# Add an item to the shopping list.
# Remove an item from the shopping list.
# Print all items in the shopping list.
# Optionally, create a ShoppingList class that manages the list with the above methods.
#Move the shopping list logic into a file named shopping_list.py.


# Instructions for Students:

# Refactor this code by creating two functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Consider creating a TemperatureConverter class with these methods.







# Instructions for Students:

# Create functions for:
# Adding an item to the inventory.
# Removing an item from the inventory.
# Printing the inventory.
# Optionally, organize these into an Inventory class.


inventory = {}
inventory["apples"] = 10
inventory["bananas"] = 5
inventory["apples"] -= 3
if inventory["apples"] <= 0:
    del inventory["apples"]
print(inventory)







# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.

password = "Pass1234"
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            print("Strong password")
        else:
            print("Password needs an uppercase letter")
    else:
        print("Password needs a number")
else:
    print("Password is too short")
      