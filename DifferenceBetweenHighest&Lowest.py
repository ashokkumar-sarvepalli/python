n = int(input("Enter number of elements in the array"))
arr = []
i = 0
while i<n:
    arr.append(int(input("Enter next element in the array")))
    i = i+1

max = arr[0]
min = arr[0]
for i in range(len(arr)):
    if (arr[i]>max):
        max = arr[i]
    if (arr[i]<min):
        min = arr[i]
    
diff = max - min
print("The difference is",diff)
# '+' is Java ',' is Python
