n = int(input('Enter the number of elements in the array'))
#below is the array declaration
arr = []
i=0
# below loop gets the input and fills the array
while i<n :
    arr.append(int(input('Enter the next element in the array')))
    i=i+1

#
i=0
while i<n :
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    i = i+2

    
# print the output

print(arr)
    

     
