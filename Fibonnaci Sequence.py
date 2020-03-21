num = int(input("Please input how many terms you want"))
if num <= 0:
    print("Error")
arr = []
arr.append(0)
arr.append(1)
for i in range(2,num):
    arr.append(arr[i-1]+ arr[i-2])

print(arr)

