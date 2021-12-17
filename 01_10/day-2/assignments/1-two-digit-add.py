two_digit_number = input("Type a two digit number: ")
if len(two_digit_number) == 2:
    d1 = int(two_digit_number[0])
    d2 = int(two_digit_number[1])
    print(d1 + d2)
else:
    print('It is not a 2 digit number')
