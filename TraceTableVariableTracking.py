arr = [4,1,6]
swapsMade = False
print("Starting of the program before the loop arr = ",arr,"swapsMade = ",swapsMade)
while swapsMade == False:
    swapsMade = True
    i = 0
    print("Inside outer while swapsMade = ",swapsMade,"i = ",i)
    while i<2:
        if arr[i+1]<arr[i]:
            t = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = t
            swapsMade = False
            print("printing inside inner while and if condition(when ever it becomes true the if contion) : t=",t,"swapsMade=",swapsMade,"arr=",arr)
        i = i+1
        print("printing inside while loop outside of if condition i=",i)

    
        




