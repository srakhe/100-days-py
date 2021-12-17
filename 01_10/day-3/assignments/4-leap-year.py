year = int(input("Which year do you want to check? "))
leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        leap = True
if leap:
    print('It is a leap year!')
else:
    print('It is not a leap year!')
