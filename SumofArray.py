n = int(input("Enter number of elements in the array"))
arr = []
i=0
# below loop gets the input and fills the array
while i<n :
    arr.append(int(input('Enter the next element in the array')))
    i=i+1
sum = 0
i = 0
for i in range(len(arr)):
    sum = sum + arr[i]

print("The sum of the elements entered is",sum)
