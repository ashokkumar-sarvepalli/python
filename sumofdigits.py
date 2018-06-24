n=int(input("enter the num"))
sum=0
while n>0:
    lastdigit=n%10
    n=n//10
    sum=sum+lastdigit
print("hello")
print(sum)
