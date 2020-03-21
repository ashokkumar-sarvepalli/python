width = int(input("Input Width"))
for i in range (1, width+1):    
    for k in range(1,width-i+1):
        print(' ',end='')
    for j in range (1,i+1): 
        print(j,end='')
    for l in range(i-1,0,-1):
        print(l,end='')


    print("\n",end='')
