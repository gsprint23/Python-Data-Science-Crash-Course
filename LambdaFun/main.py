# A function is an object in Python, this means you can use a function like a reference
def mydouble(x):
    return 2 * x

print(mydouble(5))
myfunc = mydouble # myfunc is a reference to the same object that mydouble refers to
print(myfunc(10)) # myfunc is an alias 
print(type(mydouble), type(myfunc), mydouble == myfunc)


# A lambda function is a function that has no name
# (hence, an anonymous/nameless function) 
# that you can pass around in your code to be executed at a later time
# lambda x: x + 1

# examples!
def say(message):
    print("saying:", message)

# define another function that can execute any one string argument void function
# it is passed
def executeVoidFunction(f): # f is a reference to a function
    f("hello") # execute f passing in "hello"

# call executeVoidFunction(), passing in say function reference
executeVoidFunction(say)
# call executeVoidFunction(), passing in a lambda function
executeVoidFunction(lambda x: print("from lambda:", x))

# map, filter, and reduce 
nums = [3, 4, 5]
print("orig list:", nums)

# map a function to each element in a list
# nums2 = map(mydouble, nums)
nums2 = map(lambda x: 2 * x, nums)
print(list(nums2))

# filter elements in a list by some criteria
def odd(x):
    return x % 2 == 1
# nums3 = filter(odd, nums)
nums3 = filter(lambda x: x % 2 == 1, nums)
print(list(nums3))

# reduce elements in a list to a single value
from functools import reduce
def total(total_so_far, x):
    return total_so_far + x
# result = reduce(total, nums)
result = reduce(lambda total_so_far, x: total_so_far + x, nums)
print(result)

nums = [1, 2, 3, 4, 5]
sentence = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# Use a lambda function to create a new list of nums converted to floats
# Use a lambda function to create a new list of only the even integers in nums
# Use a lambda function to compute the product of the integers in nums
# Use a lambda function to create a list of only the words containing the letter “o”
# Use a lambda function to create a list of the words in all caps
# Use a lambda function to create a string containing only the first letters of each word
# Read the documentation for the built-in function sorted(key). Use a lambda function to 
# create a list of the words sorted from shortest word to longest word