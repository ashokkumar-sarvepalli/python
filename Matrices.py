rows = int(input("Enter number of rows- SQUARE MATRIX"))
columns = rows
matrix = []

# 10 20 30
# 21 45 67
# 12 34 90

#after 1st ieration of the loop
# arr = [10,20,30]
#matrix =[[10,20,30]]

# after 2nd itertion of the loop
# arr = [21,45,67]
#matrix = [[10,20,30],[21,45,67]]


# after 3rd itertion of the loop
# arr = [12,34,90]
#matrix = [[10,20,30],[21,45,67],[12,34,90]]

#below code for getting input - the flow is represented above in each iteration
for i in range(rows):
    arr =[]
    print("Enter the numbers for row :",i+1)
    for j in range(columns):
        arr.append(int(input()))
    matrix.append(arr)


# logic for right diagonal sum, upper trianglem, lower triangle sum
rightDiagonalSum = 0
upperTriangleSum = 0
lowerTriangleSum = 0
leftDiagonalSum = 0
for i in range(rows):
    for j in range(columns):
        if(i + j == rows - 1):
            rightDiagonalSum = rightDiagonalSum + matrix[i][j]
        if(i == j):
            leftDiagonalSum = leftDiagonalSum + matrix[i][j]
            
        if (i>j):
            upperTriangleSum = upperTriangleSum + matrix[i][j]
            
        elif (i<j):
            lowerTriangleSum = lowerTriangleSum + matrix[i][j]
            
print("The sum of the right diagonal is :",rightDiagonalSum)
print("The sum of the left diagonal is: ",leftDiagonalSum)
print("The upper Triangle Sum is :" ,upperTriangleSum)
print("The lower Triangle Sum is : ",lowerTriangleSum)        

            

    

    
