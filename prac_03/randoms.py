import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
#Question 1
# generate a random integer
# the smallest number is 5, the largest number is 20

# Question2
# generate a random odd number between 3 and 10
# the smallest number is 3, the largest number is 9
# no, line 2 may only produce 3, 5, 7, 9, because the range is between 3(inclusive) and 10(exclusive),
#  and the step is 2

# Question3
# generate a random float number between 2.5 and 5.5 (both inclusive)
# the smallest number is 2.5, the largest number is 5.5

# Question 4
print(random.uniform(1, 100)) # produce a random float number
print(random.randint(1, 100)) #  produce a random integer number
