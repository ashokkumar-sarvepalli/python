students = int(input("Enter number of students"))
columns = 3
marks = []
for i in range(students):
    arr=[]
    print("Enter the Maths marks for student :",i+1);
    arr.append(int(input()))
    print("Entearr the Physics marks for student :",i+1);
    arr.append(int(input()))
    print("Enter the Chemistry marks for student :",i+1);
    arr.append(int(input()))
    marks.append(arr)

print(marks)


marks[0][0] + marks[0][1] + marks[0][2]

for i in range(students):
    sum =0
    for j in range(columns):
        sum = sum + marks[i][j]
    print("The total of the student :",i+1," is :",sum)

total=0
for i in range(students):
    for j in range(columns):
        total = total + marks[i][j]

print("The total marks is:",total)
        


marks[0][0] + marks[1][0] + marks[2][0]

for i in range(columns):
    sum = 0
    for j in range(students):
        sum = sum + marks[j][i]
    mean = sum/students
    print("The average of column ",i+1," is ",mean)

sum = 0
for i in range(students):
    for j in range(columns):
        if i == j:
            sum = sum + marks[i][j]

print("The left diagonal sum is ", sum)

sum =0
for i in range(students):
    sum = sum + marks[i][i]

print("The left diagonal sum [improvised version] is ", sum)



