student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
sum = 0
num = 0
for height in student_heights:
    sum += height
    num += 1
avg = sum // num
print(avg)
