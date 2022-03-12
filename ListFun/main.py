import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3
list_ints = [100, 1, 10, 20]
# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list

print(list_ints[0])
print(list_ints[-4])

# types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))
# lists are mutable (they can be changed)
list_numbers[0] = "hello"
print(list_numbers)

# use len() to find out how many elements are in a list
print(len(list_numbers))
list_numbers.append("another element")
# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list
print(list_numbers[len(list_numbers) - 1])

# we can declare an empty list!
empty_list = []
print(len(empty_list))

# we can have lists of lists (2D or ND)
nested_list = [[0, 1], [2], [3], [4, 5], []]
print(len(nested_list))
print(len(nested_list[0]))

# looping through list items
candies = ["twix", "reeses", "oreos", "snickers"]
print(candies)

for candy in candies:
    print(candy)

i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

i = 0
for i in range(len(candies)):
    print(i, candies[i])

# common list operators
# list concatenation... adding 2 lists together
print(candies)
candies += ["m&ms", "starburst"]
print(candies)
# list repetition... repeating elements in a list
bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)
# list slicing
print(candies[1:3]) # : is the slice operator. start index is inclusive
# end index is exclusive
# if you ever need a copy of a list, you can simply use the : with no start or end indices
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)

# list methods 
candies.remove("reeses")
print(candies)
# extend()
candies.extend(["skittles", "reeses"])
print(candies)
# pop()
# is like remove(), but is a position-based removal
first_candy = candies.pop(0)
print(first_candy, candies)

# create a string from a list of strings
word_list = ["t", "wi", "x"]
word_str = "*".join(word_list)
print(word_str)
# list()
# to convert a string to a list
word_list2 = list(word_str)
print(word_list2)

# CSV type (comma separated value)
# a,b,c
word_list3 = word_str.split("*")
print(word_list3)

# (more on) STRINGS
word = "starburst"
print(word)
# 0-based indexing
print(word[0], word[-1], word[1:4])
# string are immutable (they can't be changed)
# word[0] = "S" # crashes !!
# string concatenation + 
word = word + "!!"
print(word)
# string repetition *
print(word * 5)
# string comparison < <= > >= == !=
print("starburst" < "apple")
print("apple" < "starburst")
print("starburst" < "Starburst")
print("a" <= "a")
print("a" == "a")
print("abc" < "ab")
print("abc" < "ABC")
# strings are compared character by character from left to right
# based on ASCII values (integers that represent characters)
print("abc" == "ABC".lower())
list_words = ["twix", "starburst", word, "Starburst", "reeses", "snickers"]
print(sorted(list_words))
# A ASCII 65
# a ASCII 97
# string methods
# lower(), upper(), join(), split(), strip(), find()
# strip() removes leading and trailing whitespace characters
word = "   \n  \t\t\t \n    \t\t  starburst\t\t\n\n   \n\t\n  "
print(word)
print(repr(word))
print(word.strip())
print(repr(word.strip()))
# find()
word = word.strip()
# find the starting index of a substring
print(word.find("tar"))
print(word.find("hello"))
index = word.find("b")
if index != -1:
    print("b was found at:", index, word[index])