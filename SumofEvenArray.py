n = int(input("Enter number of elements in the array"))
arr = []
i=0
# below loop gets the input and fills the array
while i<n :
    arr.append(int(input('Enter the next element in the array')))
    i=i+1
        
even = 0
i = 0
for i in range(len(arr)):
    if arr[i]%2 == 0:
        even = even + arr[i]

print("The sum of the even elements entered is",even)
