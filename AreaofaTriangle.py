import math #need square root
def area(sideA,sideB,sideC):
    perimeter = (sideA+sideB+sideC)/2
    area = math.sqrt(perimeter*(perimeter-sideA)*(perimeter-sideB)*(perimeter-sideC))
    # * needed since compiler will not understand
    return area


sideA= int(input("Input side A: "))
sideB= int(input("Input side B: "))
sideC= int(input("Input side C: "))
result = area(sideA,sideB,sideC) #increases efficency- no need to calll it 2x for same thing
print("The area is(integer): ",int(result))
print("The area is: ",result)
