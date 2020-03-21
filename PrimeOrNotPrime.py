#defintion of user defined function (or subroutine starts)
def isPrime(num):
    if num <=1:
        return False
    for i in range(2,(int)(num/2)+1):
        if num%i == 0:
            return False
    return True
          
#definition of user defined function (or subroutine ends)
            

#main program starts here

ans = 'Y'
while ans == 'Y' or ans == 'y':
    num = int(input("Enter the number to find prime or not"))
    if isPrime(num):
        print("The entered number is prime")
    else :
        print("The entered number is not prime")


    ans = input("Press 'Y' to continue or press any key to stop...")

#main program ends here

