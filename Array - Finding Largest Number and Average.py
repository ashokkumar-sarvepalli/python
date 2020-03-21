n = int(input("Enter number of elements in array"))
arr = []
i = 0
while i<n:
    arr.append(int(input("Enter next element in array")))
    i = i+1
total = 0
max = arr[0]
min = arr[0]
for i in range(len(arr)):
    total = total + arr[i]
    if(arr[i] > max):
        max = arr[i]
    if(arr[i] < min):
        min = arr[i]
print("The largest number in the array is: ",max)
print("The lowest number in the array is: ",min)
print("The sum of the array is: ",total)
avr = total/len(arr)
print ("The mean of this array is: ",avr)
