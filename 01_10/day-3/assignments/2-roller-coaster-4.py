print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
cost = 0
if height > 120:
    print('You can ride the roller coaster!')
    age = int(input("What is your age in years? "))
    if age > 18 and not (45 <= age <= 55):
        cost += 12
    if age > 18 and (45 <= age <= 55):
        cost += 0
    elif 18 >= age >= 12:
        cost += 7
    else:
        cost += 5
    photo = input('Do you want a photo?')
    if photo.lower() == 'yes':
        cost += 3
    print(f'Your total bill is ${cost}')
else:
    print('Sorry! You cannot ride the roller coaster')
