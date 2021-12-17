# Method 1 of making a new list out of data in another
# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_list = []
# for n in numbers:
#     add_n = n + 1
#     new_list.append(add_n)

# Method 2 list comprehension method
# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_list = [n + 1 for n in numbers]

# Sequences in python: list, string, range, tuple. They are called sequences because they have a particular order!

# new_list = [n * 2 for n in range(1, 6)]

# Conditional list comprehension

# Get names only of length 4 or less
names = ['alex', 'beth', 'carol', 'zach', 'tomato', 'aloo', 'potato']
new_list = [name for name in names if len(name) <= 4]

print(new_list)
