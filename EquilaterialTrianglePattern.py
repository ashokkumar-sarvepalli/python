width = int(input("Input Width"))
for i in range (1, width+1):
    val = 'a'
    
    for k in range(1,width-i+1):
        print(' ',end='')
    for j in range (1,(2*i)): 
        print(val,end='')
        intval = ord(val)
        intval = intval+1
        val = chr(intval)
        
        


    print("\n",end='')
