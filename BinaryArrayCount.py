n = int(input("Enter number of elements in the array"))
arr = []
i=0
# below loop gets the input and fills the array
while i<n :
    arr.append(int(input('Enter the next element in the array')))
    i=i+1

countzero = 0
countone = 0

i=0
while i<n :
    if(arr[i]==0):
        countzero = countzero+1
    elif (arr[i]==1):
        countone = countone+1
    i=i+1

print("number of zeros",countzero)
print("number of ones",countone) 
