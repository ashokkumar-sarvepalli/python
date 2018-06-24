n=int(input('enter the number'))
first=0
second=1
print(first)
print(second)
for i in range(3,n+1):
    third=first+second
    print(third)
    first=second
    second=third
