height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) // (float(height) ** 2)
category = ''
if bmi < 18.5:
    category = 'underweight'
elif 18.5 <= bmi < 25:
    category = 'normal weight'
elif 25 <= bmi < 30:
    category = 'slightly overweight'
elif 30 <= bmi < 35:
    category = 'obese'
else:
    category = 'clinically obese'
print(f'Your BMI is {bmi}, you are {category}')
