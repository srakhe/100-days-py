import random

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
new_dict = {key: value for key in keys for value in values}
print('Dict from list: ', new_dict)
new_dict1 = {key: value for (key, value) in new_dict.items()}
print('Dict from another dict: ', new_dict1)
new_dict2 = {key: value for (key, value) in new_dict.items() if not key == 'a'}
print('Dict from another dict: ', new_dict2)

names = ['alex', 'beth', 'carol', 'zach', 'tomato', 'aloo', 'potato']
new_dict3 = {name: random.randint(0, 100) for name in names}
print(new_dict3)

# Outputs:
# Dict from list:  {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5}
# Dict from another dict:  {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5}
# Dict from another dict:  {'b': 5, 'c': 5, 'd': 5, 'e': 5}
# {'alex': 17, 'beth': 89, 'carol': 53, 'zach': 57, 'tomato': 33, 'aloo': 10, 'potato': 33}
