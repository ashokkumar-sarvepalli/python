column0 = []
column1 = []
column2 = []

def printColumns():
    len0 = len(column0)-1
    len1 = len(column1)-1
    len2 = len(column2)-1

     
    while len0>=0:
        print(column0[len0])
        len0=len0-1

    print("-------Column0-------")
    
    while len1>=0:
        print(column1[len1])
        len1=len1-1

    print("-------Column1-------")
   
    while len2>=0:
        print(column2[len2])
        len2=len2-1

    print("-------Column2-------")
    
   # print(column0)
    #print(column1)
    #print(column2)

print("Enter the alphabets in column 0")
inp = "yes"
while inp =="yes" or inp =="YES" :
    x = input("Enter the character")
    column0.append(x)
    inp = input("Enter 'yes' for more characters or any key to stop")


print("Printing the input")
printColumns()

while len(column0) > 0:
    column2.append(column0.pop())

print("Printing the intermediate step")
printColumns()

while len(column2) > 0:
    column1.append(column2.pop())


print("Printing the final step")
printColumns()

    
