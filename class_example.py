class Shirt: # Is a good coding practice to capitalize the first letter.
    def __init__ (self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

# def __init__ is used by Python to create a specific short object.
# Self stores the attributes and make the attributes available, or it can be viewed as a dictionary that stores the attributes and the attribute values.  It's always the first
# input to the methods if we want to access the attributes.

# Methods:

    def change_price (self, new_price):
        self.price = new_price
      
    def discount (self, discount):
        return self.price*(1-discount)
      
# Instantiating and object: Creating a real object

Shirt('red', 'S', 'short sleeve', 15)
new_shirt = Shirt('red', 'S', 'short sleeve', 15)

# Using dot (.) syntax, we can access the attributes and methods:

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(0.2))

# Example: Instantiate three Shirt objects and store those objects in a list:

tshirt_collection = []
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve, 10)
                    
tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)
                  
for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)
                    
                    
