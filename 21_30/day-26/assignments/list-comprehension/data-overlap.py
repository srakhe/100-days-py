with open('file1.txt') as file:
    data1 = file.readlines()

with open('file2.txt') as file:
    data2 = file.readlines()

common_list = [int(num) for num in data1 if num in data2]
print('Common list: ', common_list)
