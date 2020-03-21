n = int(input('Enter the number of elements in the array'))
arr= []
i = 0
while i<n:
    arr.append(int(input("Enter next element in the array")))
    i = i+1
#Above - to move i along in the array for elements

max = arr[0]
for i in range(len(arr)):
  if(arr[i] > max):
     max = arr[i]
# Above - Finds max number
print(max)
