max = -999999999
min =  999999999
ans = 'Y'
while ans == 'Y' or ans =='y':
    num = int(input("Enter the number"))
    if(num>max):
        max = num
    if(num<min):
        min = num

    ans = input("Press 'Y' to coninue or any key to stop")
    
print("The maximum element entered by you in the above list ",max)
print("The minimum element entered by you in the above list ",min)
