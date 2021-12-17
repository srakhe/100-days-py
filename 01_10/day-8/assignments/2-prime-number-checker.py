def prime_checker(number):
    not_prime = False
    for i in range(2, number):
        if number % i == 0:
            not_prime = True
            break
    if not_prime:
        print('It\'s not a prime number')
    else:
        print('It\'s a prime number')


n = int(input("Check this number: "))
prime_checker(number=n)
