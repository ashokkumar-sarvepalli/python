n = int(input('Enter the number of elements in the array'))
#below is the array declaration
arr = []
i=0
# below loop gets the input and fills the array
while i<n :
    arr.append(int(input('Enter the next element in the array')))
    i=i+1

#below logic is swaps the first half of the array to the second half
mid = int(len(arr)/2)
i=0
while i<mid :
    temp = arr[i]
    arr[i] = arr[i+mid]
    arr[i+mid] = temp
    i=i+1

    
# print the output

print(arr)
    

     
