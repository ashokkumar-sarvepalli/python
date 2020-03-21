num = int(input("Please input how many terms you want"))
if num <= 0:
    print("Error")
f1 =0
f2 =1
print(f1)
print(f2)

for i in range(2,num):
    f3 = f1 +f2
    print(f3)
    f1 =f2
    f2 =f3
