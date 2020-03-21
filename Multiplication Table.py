num = int(input("Please input a number that you would like to see the multiples of "))
end = int(input("Please input what multiple you would like to go up to "))
for i in range(1,end+1):
    multiple = num * i
    print(num," x ",i," = ",multiple)
