rows = int(input("Please input the number of rows"))
columns = int(input("Please input the number of columns"))
matrix = []
sum = 0
for i in range(rows):
    arr=[]
    print("Enter numbers for row:",i+1)
    for j in range(columns):
        arr.append(int(input()))
    matrix.append(arr)
for k in range(rows):
    for l in range(columns):
        if (k==0 or k==rows-1):
            sum = sum + matrix[k][l]

        elif (l==0 or l==columns-1):
            sum = sum + matrix[k][l]

print (sum)
print (matrix)
