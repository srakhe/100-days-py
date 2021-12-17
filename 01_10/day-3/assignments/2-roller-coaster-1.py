print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
canRide = False
if height > 120:
    age = int(input("What is your age in years? "))
    if age > 18:
        canRide = True
    else:
        canRide = False
else:
    canRide = False
if canRide:
    print('You can ride the roller coaster!')
else:
    print('Sorry! You cannot ride the roller coaster')
