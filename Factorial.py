#factorial subroutine starts
def factorial(num):
    total = 1
    for i in range(1,num+1):
    # num+1 since last one is not automatically inclusive in python
        total = total *i
    return total

#factorial subroutine ends

#starting of the main program

num = int(input("Enter a number you want the factorial for"))
print("The factorial is ",factorial(num))
