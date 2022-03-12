import math # by convention, you put all of your import statements at the top
import random

# this is a one line comment
# a comment is "code" that Python ignores
# we use comments to document our code

"""
this is a multi
line comment
AKA block comment
"""
print("hello world")

# VARIABLES 
# a variable stores a value
x = 5 # read this as "x is assigned 5" or "x stores 5"
# NOT "x equals 5"
# == is the equality
print(x)
# a variable has a data type
# the data type define the range of values
# example: int data type
# int is short for integer
# an int variable can store whole numbers
print(type(x))
# let's overwrite x with a new value
x = 5.7
print(x)
print(type(x))
# example: float data type
# float is short for floating point number
# a float variable can store decimal numbers (numbers with a fractional part)
x = "hello"
# example: str data type
# str is short for string
# a string variable can store a sequence of characters
print(x)
print(type(x))
x = "5"
print(x)
print(type(x))

# OPERATORS
# PEMDAS: parens, exponents, multiplication, division, addition, subtraction
# ()
# ** is the exponentiation 
print(2 ** 3) # 2 * 2 * 2 
# a py file is also known as a module
# we can use standard modules that are included with python
# let's use the math module to see another way to compute an exponent
print(math.pow(2, 3))
# * is multiplication
print(4 * 5)
# / is floating point division (the "normal" division)
print(5 / 2)
# // is integer division (the whole number result of floating point division)
print(5 // 2)
# % is modulus (the remainder from integer division)
print(5 % 2)

# IO (input output)
print("a", "b", "c")
print("a", "b", "c", sep="")
print("a", "b", "c", 1, 2, 3, x, "z", sep="***")
print("a", "b", "c", end="")
print("x", "y", "z")

print(math.pi)
# we can round pi to 2 decimal places
# a few ways to do this
# 1. Pythonic way
print("{:.2f}".format(math.pi))
# 2. C style
print("%.2f" %(math.pi))
# 3. use the built-in round() function
print(round(math.pi, 2))

# GETTING INPUT FROM THE USER
# print("Please enter your favorite number: ")
# favorite_number = input()
# print("Your favorite number is:", favorite_number)
# print("Your favorite number doubled is:", 2 * favorite_number)
# # string repetition
# print(3 * "hello")
# print(type(favorite_number))
# # let's say we really do want favorite_number to be a numeric type (e.g. float or int)
# # this is called type conversion (e.g. str -> int)
# favorite_number_int = int(favorite_number)
# print(favorite_number_int)
# print(type(favorite_number_int))
# print("Your favorite number doubled is:", 2 * favorite_number_int)

# CONDITIONALS (AKA if statements)
# if some condition (boolean condition) is ture, then
# execute some code
# if boolean condition:
#   body

x = 6
if x == 6:
    print("x is 6")
    # in Python, indentation (1 tab or 4 spaces) is used
    # to group code statements into a block
    # like { }
    print("hello!!")

# let's say we want to create a guess my number game
num_guesses = 3
num_to_guess = 4
# players_guess = int(input("Please enter a number between 1 and 10 inclusive: "))

# # we can use an else keyword by attached it to a preceding if statement
# # else bodies only execute when the condition on the associated if statement is false
# # if players_guess == num_to_guess:
# #     print("Congrats, you guessed the number!!")
# # else: # !(players_guess == num_to_guess) -> players_guess != num_to guess (e.g. players_guess == num_to_guess is false)
# #     print("Unfortunately, you guessed incorrectly; however, I will give you a hint")
# #     if players_guess > num_to_guess:
# #         print("Your guess was too high")
# #     else: # !(players_guess > num_to_guess) -> players_guess <= num_to_guess
# #         print("Your guess was too low")

# # && in Python, this is and keyword
# # ||, this or keyword
# # !, this not keyword

# # multiple-alternative if statements
# # we also have an elif (else if)
# # use elif when you want to test multiple conditions in order
# # the first condition that evaluates to true, will have its body execute
# # then at the end of that body the code will exit the entire mulitple alternative
# # if structure
# if players_guess == num_to_guess:
#     print("Congrats, you guessed the number!!")
# elif players_guess > num_to_guess: # players_guess != num_to_guess
#     print("Your guess was too high")
# else: # !(players_guess > num_to_guess) -> players_guess <= num_to_guess
#     print("Your guess was too low")

# # else is a "catch all"
# # else will always execute if none of the previous conditions are true

# num_guesses -= 1
# if players_guess != num_to_guess:
#     if num_guesses > 0:
#         print("You get to try again")

# # the above nested if can collapse into a compound condition
# if players_guess != num_to_guess and num_guesses > 0:
#     print("You get to try again")

# LOOPS
# use a loop to repeat statements
# we have for loops and while loops
# for loop structure
# for item in sequence:
#    body (statements you want to repeat)
#    you do something with item
# lots of sequences we can use with for loop!
# lists are sequences!!
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
# strings are sequences!!
for character in "hello":
    print(character)
# we can generate our own sequences using range()
# range(stop) e.g. range(5) : [0, stop) e.g. [0, 5)
for i in range(9): #[0, 9)
    print(i, end=" ")
print()
# range(start, stop) e.g. range(1, 5) : [start, stop) e.g. [1, 5)
for i in range(4, 9): #[4, 9)
    print(i, end=" ")
print()
# range(start, stop, step) e.g. range(1, 5, 2) : [start, stop) incremening by step
# e.g. [1, 3]
for i in range(4, 9, 2): #[0, 9) incrementing by 2
    print(i, end=" ")
print()

# task 1: try to produce the same output as our last for loop (4 6 8 ) but reversed
# (8 6 4 )
for i in range(8, 3, -2):
    print(i, end=" ")
print()

# task 2: write a for loop to print out the first 20 even numbers
# all on line, seperated by a , 
# ex: 2, 4, 6, ...., 38, 40
for j in range(2, 40, 2):
    print(j, end=", ")
print(j + 2)

# while loop structure
# while condition is true:
#    body (statements to be repeated)
#    progress towards the condition being false
k = 2
while k < 40:
    print(k, end=", ")
    k += 2
print(k)

# you can get an early exit from a look using break keyword
# while True:
#     user_input = input("Enter a word (stop to exit): ")
#     if user_input == "stop":
#         break # early exit 
# print("here")

# you can nest loops (be sure to watch your indentation)

# FUNCTIONS
# a function is a named sequence of statements
# 1. definition # 2. call
# print(), input(), int(), type(), round(), ...
# now we are going define/write our own functions

# functions take inputs (arguments that are passed into the
# function when you call it and parameters that are variables
# defined in the function header that store these incoming arguments) 
# and produce outputs (AKA return values AKA return results)

# function structure
# def function_name(parameter list): # header
#     body 

# definition = function header + function body
# the body of a function does not execute until the function is called

# example 1: no parameters (no arguments in the call) and no return value
def say_hello():
    print("hello")

say_hello() # function call
for _ in range(5):
    say_hello() 

# example 2: one parameter (one argument in the call) and no return value
def say(message):
    print("message received:", message)

say("hi there") # "hi there" is the argument
say("goodbye") # "goodbye" is the argument
say("python is awesome!") # "python is awesome!" is the argument

# TASK: define/call a function that accepts the radius of a circle and
# prints out the area of that circle
# area = pi R^2
def compute_circle_area(radius): # radius is the parameter
    area = math.pi * radius ** 2
    print("area:", area)
compute_circle_area(5.0) # 5.0 is the argument

# example 3: one parameter and one return value
def compute_circle_area2(radius): # radius is the parameter
    area = math.pi * radius ** 2
    return area 
result = compute_circle_area2(5.0) # 5.0 is the argument
print("result:", result)
print("result rounded:", round(compute_circle_area2(5.0), 2))
print("area doubled:", compute_circle_area2(5.0) * 2)

# example 4: one parameter and two return values!!
def compute_circle_area_and_circumference(radius): # radius is the parameter
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference # creates a tuple (immutable list)
    # tuple has 2 elements

results = compute_circle_area_and_circumference(5.0)
print("results:", results)
print("results:", results[0], results[1])
result1, result2 = compute_circle_area_and_circumference(5.0) # tuple unpacking
print("result1:", result1, "result2:", result2)

def add(a, b):
    print(a + b)
add(2, 3)

# example 5: one parameter with a default argument (and no return value)
def print_even_numbers(stop=20):
    """A function that prints the first even numbers starting at 2
    and stopping at stop

    """
    for j in range(2, stop, 2):
        print(j, end=", ")
    print(j + 2)

print_even_numbers(40)
print_even_numbers()
print_even_numbers(stop=10) # keyword arguments

# demo of help()
# help(print)
# help(print_even_numbers)

# why use functions?
# 1. write once, call multiple times
# 2. minimize redundant code
# 3. helps with code organization

# RANDOM NUMBERS
# often we want a random numbers to simulate something
# or setup the initial state for an algorithm

# often we want the same random number sequence each time
# we run our program
# 1. debugging
# 2. producing reproducible results
random.seed(0) 

# lets say we want roll a 6-sided die
die_roll = random.randint(1, 6) # [1, 6]
print("die_roll:", die_roll)
die_roll = random.randint(1, 6) # [1, 6]
print("die_roll:", die_roll)
die_roll = random.randint(1, 6) # [1, 6]
print("die_roll:", die_roll)

die_roll = random.randrange(1, 7) # [1, 7)
print("die_roll:", die_roll)

# floating point numbers
print(random.random()) # [0, 1)
print(random.random())
print(random.uniform(2, 5)) # [2, 5)
for _ in range(5):
    print(random.gauss(100.0, 5.0))

# lists
my_list = ["a", "b", "c", "d", "e"]
random.shuffle(my_list) # inplace shuffle
print(my_list)
print(random.choice(my_list))
print(random.sample(my_list, 3))