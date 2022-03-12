import random 

# 1D List Practice Problem
# In ListFun, write code that generates 20 random numbers between 1 and 10 inclusive 
# and puts them in a 1D list. The program then does the following using the list:
random.seed(0)
numbers = []
for _ in range(20):
    rand_num = random.randrange(1, 11) # [1, 11)
    numbers.append(rand_num)
print(numbers)

# 1. Prints the numbers all one line, each number separated by a space
def pretty_print(nums):
    for num in nums:
        print(num, end=" ")
    print()
pretty_print(numbers)

# 2. Sorts the list using a list method
# numbers.sort() # inplace sort (modifies the list)
# pretty_print(numbers)
# solve this again using the built-in function sorted()
sorted_numbers = sorted(numbers)
print("sorted_numbers", end=": ")
pretty_print(sorted_numbers)
print("numbers", end=": ")
pretty_print(numbers)

# 3. Prints the largest and smallest number in the list
#     Hint: can you take advantage of the current ordering of your list?
print("min:", sorted_numbers[0], "max:", sorted_numbers[-1])
# solve this again using the built-in functions min() and max()
print("min:", min(numbers), "max:", max(numbers))

# 4. Determines the number of times a user-specified number is in the list
# user_num = int(input("Please enter a number in [1, 10]: "))
# count = 0
# for num in numbers: 
#     if num == user_num:
#         count += 1
# print("There are", count, "of", user_num, "in the list")
# # or solve it again using a list method
# print("There are", numbers.count(user_num), "of", user_num, "in the list")

# # 5. Removes all instances of a user-specified number in the list. 
# # If the number is not in the list print the message: "Sorry, your number is not here!"
# user_num = int(input("Please enter a number in [1, 10] to remove: "))
# if user_num in numbers:
#     while user_num in numbers:
#         numbers.remove(user_num)
# else: # user_num not in numbers
#     print("Sorry, your number is not here!")
# pretty_print(numbers)
# print(numbers.count(user_num))
# # Note: for practice with functions, try solving this problem using functions :)

# 2D List Practice Problem
# In ListFun, write code that generates 50 random numbers between 1 and 10 
# inclusive and puts them in a 2D list that is 10x5 (e.g. 10 rows and 5 columns). 
table = [] # 2D list (AKA nested list) where each element is a row (1D list of ints)
for _ in range(10):
    row = []
    for _ in range(5):
        rand_num = random.randrange(1, 11) # [1, 10] AKA [1, 10)
        row.append(rand_num)
    # we have built a row
    table.append(row)
print("table:", table)

# The program then does the following using the list:
# 1. Prints the numbers in a nice grid format (like a table)
def print_table(table):
    for row in table:
        for value in row:
            print(value, end="\t")
        print()
print_table(table)
# NOTE: take a look at the tabulate module for a nice package used for
# pretty printing tables

# 2. Prints the largest and smallest number in the list
# assume the first row's first element is both the smallest and the
# largest element in the table
smallest = largest = table[0][0] # assumes there is at least 1 row w/1 element
for row in table:
    if min(row) < smallest:
        # new smallest 
        smallest = min(row)
    if max(row) > largest:
        largest = max(row)
print("min:", smallest, "max:", largest)

# 3. Determines the number of times a user-specified number is in the list
user_num = int(input("Please enter a number in [1, 10]: "))
count = 0
for row in table:
    count += row.count(user_num)
print("There are", count, "of", user_num, "in the list")

# 4. Removes all instances of a user-specified number in the list. 
# If the number is not in the list print the message: "Sorry, your number is not here!"
user_num = int(input("Please enter a number in [1, 10] to remove: "))
found = False # assume we haven't found user_num in the table rows until 
# proven otherwise
for row in table:
    while user_num in row:
        found = True # we found it!!
        row.remove(user_num)

if found:
    print_table(table)
else: # not found
    print("Sorry, your number is not here!")

# Note: for practice with functions, try solving this problem using functions :)