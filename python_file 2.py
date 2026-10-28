# Question1
# Create a set containing five different fruits and print it.
fruits = {"apple", "mango", "banana", "orange", "grapes"}
print(fruits)


# Question2
# Given numbers = [2, 4, 2, 6, 4, 8, 8], convert the list into a set to remove duplicates.
numbers = [2, 4, 2, 6, 4, 8, 8]
numbers_set = set(numbers)
print(numbers_set)


# Question3
# Create a set of five numbers. Add 10 to the set and remove one existing number.
my_set = {1, 2, 3, 4, 5}
my_set.add(10)
my_set.remove(3)  # removing 3
print(my_set)


# Question4
# Ask the user for a number and check whether it exists in the set {10, 20, 30, 40, 50}.
check_set = {10, 20, 30, 40, 50}
user_num = int(input("Enter a number to check: "))

if user_num in check_set:
    print(f"{user_num} exists in the set")
else:
    print(f"{user_num} does not exist in the set")


# Question5
# Given values = {1, 2, 2, 3, 3, 3, 4}, predict the length of the set and explain why.
values = {1, 2, 2, 3, 3, 3, 4}
print(f"Length is {len(values)}")

# Explanation: A set automatically removes duplicate values, so
# {1, 2, 2, 3, 3, 3, 4} becomes {1, 2, 3, 4}, with length 4.


# Question6
# Practice the four important operations: union (|), intersection (&), difference (-),
# and symmetric difference (^).
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Find all unique elements in A and B.
# Using the same sets, find elements common to both sets.
# Find A - B and B - A. Explain why their results differ.
# Find elements that are in either A or B, but not in both.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# All unique elements in A and B (Union)
print(f"Union (A | B): {A | B}")

# Elements common to both sets (Intersection)
print(f"Intersection (A & B): {A & B}")

# A - B and B - A (Difference)
print(f"A - B: {A - B}")
print(f"B - A: {B - A}")

# Explanation: A - B gives elements only in A, while B - A gives elements
# only in B, so the results differ because set difference is not commutative.

# Elements that are in either A or B, but not in both (Symmetric Difference)
print(f"Symmetric Difference (A ^ B): {A ^ B}")
