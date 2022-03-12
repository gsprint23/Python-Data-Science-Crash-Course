# assert expression, message
# if the assert evaluates to true, then execution continues
# if the assert evaluates to the false, then execution stops
assert 3 == 3 # evaluates to true
print("here")
assert 3 == 4, "testing if 3 equals 4" # evaluates to false
print("there")

# a unit test is a function that tests a "unit under test"
# for correctness
# unit: function, class, module, ...
# typically: a unit test is a function that tests another
# function for functional correctness
# recall: function takes inputs and produces outputs
# given a function under test we can write a unit test
# that asserts the function under test produces the
# correct outputs given certain inputs

# a unit test has one or more test cases
# start with a simple/common test case
# then move on to various test cases of
# different complexity and edge cases

# example: lets write a function that implements
# the euclidean distance formula
# need: euclidean_distance.py for the function under test
# test_euclidean_distance.py for the unit test
# if we write the unit test before the function under test
# then we are practicing test driven development (TDD)