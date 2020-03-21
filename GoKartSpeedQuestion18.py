#GoKartQuestion18
speed = 0
brakingDistance = 1
isMoreInput = True
while isMoreInput == True :
    speed = int(input("Please input the speed in km/h(range 10-50)"))
    if speed<10 or speed>50:
        print("Drive properly and safely - See the range(10-50)")
        continue
    
    wet = str(input("Is the ground wet? yes or no"))
    brakingDistance = speed/5
    if wet == "yes" or wet == "YES" :
        brakingDistance = brakingDistance*1.5
        
    print("The braking distance in metres is",brakingDistance)


    option = input("Please enter 'YES' to input more or any key to stop")
    if option != "YES" and option != "yes":
        print("Thank you .. good bye")
        isMoreInput = False
    

