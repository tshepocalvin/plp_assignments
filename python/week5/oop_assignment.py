"""
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
"""

# A class representing a Forex trading pair and an Indice
# with methods to buy and sell the pair.

class Forex_Pair:
    def __init__(self, symbol, base_curr, quote_curr):
        self.symbol = symbol
        self.__base_curr = base_curr #This only applies for forex pairs
        self.__quote_curr = quote_curr #This only applies for forex pairs
        
    def BuyPair(self):
        lotsize = input("Enter a lotsize (E.g 0.20): ")
        print(f"Bought {lotsize} of {self.symbol}")
    
    def SellPair(self):
        lotsize = input("Enter a lotsize (E.g 0.20): ")
        print(f"Sold 0.5 of {self.symbol}")
        

# A class representing an Indice that inherits from Forex_Pair.
# This class does not have base_curr and quote_curr attributes.

class Indice(Forex_Pair):
    pass #Won't have base_curr & quote_curr because stocks do not have them
    

# Creating instances of Forex_Pair and Indice
EURUSD = Forex_Pair("EUR/USD", "EURO", "US Dollar")
USDJPY = Forex_Pair("USD/JPY", "US Dollar", "Japanese Yen")
Nasdaq = Indice("Nasdaq", "N/A", "N/A")

# Using the methods of the Indice classe to prove inheritance

print(f"Trading pair: {Nasdaq.symbol}")
Nasdaq.BuyPair()


"""
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()).
 However, make each class define move() differently
(for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

"""

class Animal:
    pass
    
class Cat(Animal):
    def Sound(self):
        return "Meow!"
    
class Dog(Animal):
    def Sound(self):
        return "Woof!"

animals = [Cat(), Dog()]

for animal in animals:
    print(animal.Sound())
