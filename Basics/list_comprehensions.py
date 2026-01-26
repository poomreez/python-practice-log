# List Comprehensions
# [expression for variable in iterable if condition]

nums = [-1, 2, -4, 1, -5, -2, 5, 6]
pos_nums = [num for num in nums if num >= 0]
neg_nums = [num for num in nums if num < 0]
even_nums = [num for num in nums if num % 2 == 0]
odd_nums = [num for num in nums if not num % 2 == 0]

print(even_nums, odd_nums)