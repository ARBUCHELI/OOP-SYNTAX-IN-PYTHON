# OOP-SYNTAX-IN-PYTHON

This example shows how to write a class in Python.

# Function vs Method
In the video above at 1:44, the dialogue mistakenly calls init a function rather than a method. Why is init not a function?

A function and a method look very similar. They both use the <code>def</code> keyword. They also have inputs and return outputs. The difference is that a method is inside of a class whereas a function is outside of a class.

# What is self?
If you instantiate two objects, how does Python differentiate between these two objects?

<pre><code>
shirt_one = Shirt('red', 'S', 'short-sleeve', 15)
short_two = Shirt('yellow', 'M', 'long-sleeve', 20)
</code></pre>

That's where <code>self</code> comes into play. If you call the<code>change_price</code> method on shirt_one, how does Python know to change the price of shirt_one and not of 
shirt_two?

<code>shirt_one.change_price(12)</code>

Behind the scenes, Python is calling the <code>change_price</code> method:

<pre><code>
   def change_price(self, new_price):

        self.price = new_price
</code></pre>

<code>Self</code> tells Python where to look in the computer's memory for the shirt_one object. And then Python changes the price of the shirt_one object. When you call the 
<code>change_price</code> method, <code>shirt_one.change_price(12)</code>, <code>self</code> is implicitly passed in.

The word <code>self</code> is just a convention. You could actually use any other name as long as you are consistent; however, you should always use <code>self</code> rather than some other word or else you might confuse people.

## Inspired in AWS Machine Learning Foundations Course.

# Adaptation as a repository: Andrés R. Bucheli.
