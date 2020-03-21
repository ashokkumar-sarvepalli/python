arr1 = []
arr2 = []
def inputArray(arr,n):
    print("Enter the ",n,":for the array ")
    i = 0
    while i<n:
        arr.append(int(input("Enter next element in array.")))
        i = i+1
def addArray(arr1,arr2,n):
    arr3 = []
    for i in range(0,n):
        arr3.append(arr1[i] + arr2[i])
    return arr3
n = int(input("Please input the number of elements in the array"))
inputArray(arr1,n)
inputArray(arr2,n)
print("The sum of two arrays are ",addArray(arr1,arr2,n))





    
