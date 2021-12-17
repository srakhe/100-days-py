import pandas

student_dict = {
    'students': ['Sam', 'Pam', 'Jack'],
    'scores': [80, 50, 60]
}

dataFrame = pandas.DataFrame(student_dict)
# print(dataFrame)

# Loop through the data frame

# Method 1 (not useful)
# for (key, value) in dataFrame.items():
#     print(value)

# Method 2
for (index, row) in dataFrame.iterrows():
    # print(row)
    if row.students == 'Sam':
        print('Sam\'s score: ', row.scores)
# Each row is a Series type
