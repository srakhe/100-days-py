number = int(input("Which number do you want to check? "))
type = ''
if number % 2 == 0:
    type = 'even'
else:
    type = 'odd'
print(f'This is an {type} number')
