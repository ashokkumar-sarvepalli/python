num = int(input("Input a number"))
sum=0
zero = 0
ones = 0
while(num !=0):
    temp = num%10
    if temp == 0:
        zero = zero + 1
    elif temp == 1:
        ones = ones + 1
    sum = sum + temp
    num = num//10
# '/' = normal division, '//' is integer division
print(sum)
print(zero)
print(ones)
