# importing reduce()
from functools import reduce
# list of numbers
numbers = [1, 2, 3, 4, 5]
# using reduce() to find sum of elements
sum = reduce(lambda x, y: x + y, numbers)
print("Sum of elements in", numbers, ":", sum)
