print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print('You can ride the roller coaster!')
    age = int(input("What is your age in years? "))
    if age > 18:
        price = 12
    elif 18 >= age >= 12:
        price = 7
    else:
        price = 5
    print(f'The cost of the ride for you will be: ${price}')
else:
    print('Sorry! You cannot ride the roller coaster')
