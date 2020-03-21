def minimum(arr):
    min = arr[0]
    for i in range(len(arr)):
        if(arr[i] < min):
         min = arr[i]
    return(min)


def inputArray(arr):
    i = 0
    while i<n:
        arr.append(int(input("Enter next element in the array")))
        i = i+1



n = int(input('Enter the number of elements in the array'))
arr= []
inputArray(arr)
print("The minimum value of the Array is",minimum(arr))



