width = int(input("Input Width"))
for i in range (0, width):
    val = "1"
    for j in range (0,i+1):
        print(val,end='')
        intval = ord(val)
        intval = intval+1
        val = chr(intval)


    print("\n",end='')

 
