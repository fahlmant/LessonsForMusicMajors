
.. Programming in Python Made Easy slides file, created by
   hieroglyph-quickstart on Mon Apr 20 20:28:08 2015.


Programming in Python Made Easy
===============================

Python Basics

.. toctree::
   :maxdepth: 2


What are We Learning?
---------------------

* Python 3
* Basic Programming
* Increasing skills in Logic and Problem Solving


But Why?
--------

* Programming is used in every field
* Understanding fundementals helps understand complexity
* Logic Skills!
* Learning is a good thing!


Boring Terminology
------------------

* Variables
* Operators
* Arrays
* Functions
* If/else
* For loops


So What is Python?
------------------

Python is a scripting language, and is very simple, which makes it a good learning tool.

Let's look at some examples!


Hello, World!
-------------

The simplest program. Put the following code in a file, then run with python:

.. code-block:: python

        print ("Hello, World!")


Yassss!
-------

You just made your first program!

Variables
---------

A variable is something that is changable in the code.

.. code-block:: python

        x = 7
        name = "Bob"

These are variables defined in code, which can be overwritten later in the code.

You can also get input and set the variable with that:

.. code-block:: python

    name = input("Enter your name: ")

Function
--------

A function is a bit of code that you can run over and over.

.. code-block:: python
    
    def hello():
        print("Hello, World!")

Now if we write 'hello()' later in our code, it will execute whatever is in the function block.

Indentation
-----------

In most languages, indentation is not enforced, but in practice, everyone uses it.

In python, tabs matter. The function we had in the previous slide wouldn't work if it looked like this:

.. code-block:: python
    
    def hello():
    print("Hello, World!")

If you have multiple lines you want to run in one function, they both need to be indented:

.. code-block:: python
    
    def hello():
        print("Hello, World!")
        print("Hello " + name)


Homework
--------

Write a Python program that takes the amount of coupons won as input and outputs
how many candy bars and gumballs you can get. 10 coupons for a candy bar and 3 coupons for a gumball. You prefer candy bars to gumballs, so you buy as many candy bars as you can first. Output how many candy bars and gumballs you get.








