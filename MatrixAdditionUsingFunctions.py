def inputMatrix(arr,rows,columns):
    for i in range(1,rows+1):
        temp = []
        for j in range(1,columns+1):
            temp.append(int(input("Enter the next element")))
        arr.append(temp)


def matrixSum(array1,array2,rows,columns):
    array3 = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(array1[i][j] + array2[i][j])
        array3.append(temp)

    return array3


matrixA = []
matrixB = []

rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))

inputMatrix(matrixA,rows,columns)
print("Entered matrix is ",matrixA)
inputMatrix(matrixB,rows,columns)
print("Entered matrix is ",matrixB)

print("Sum of the two matrices is ",matrixSum(matrixA,matrixB,rows,columns))

    
