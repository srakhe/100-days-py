print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
t_count = name1.count('t') + name2.count('t')
r_count = name1.count('r') + name2.count('r')
u_count = name1.count('u') + name2.count('u')
e_count = name1.count('e') + name2.count('e')
sum_1 = t_count + r_count + u_count + e_count
l_count = name1.count('l') + name2.count('l')
o_count = name1.count('o') + name2.count('o')
v_count = name1.count('v') + name2.count('v')
e_count = name1.count('e') + name2.count('e')
sum_2 = l_count + o_count + v_count + e_count
score = int(str(sum_1) + str(sum_2))
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos')
elif 40 < score < 50:
    print(f'Your score is {score}, you are alright together')
else:
    print(f'Your score is {score}')
