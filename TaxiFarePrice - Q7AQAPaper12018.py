# distance <- 0 
#WHILE TRUE THEN
#    distance <- USERINPUT
#    if distance>0
#       EXIT LOOP
#    OUTPUT "Wrong INput to distance"
#noOfPassengers <- USERINPUT
# taxiFare <- (2*noOfPassengers) + (distance*1.5)
#OUTPUT taxiFare

distance = 0
while True:
    distance = int(input("Please input a distance in km"))
    if distance > 0:
        break
    print("Wrong Input for distance")
noOfPassengers = int(input("Please input number of passengers"))
taxiFare = (2*noOfPassengers) + (distance*1.5)
print("The final taxi fare is: £",taxiFare)

     
