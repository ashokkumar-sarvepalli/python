#LowercaseOrNotQuestion
isMoreInput  = True
while isMoreInput == True :
    char = input("Please Enter a character")
    if len(char)>1:
        print("You Entered more than one character - please try again")
        continue

    if ord(char[0])>=97 and ord(char[0])<=122:
        #ord gives unicode of a character which is the ASCII value
        print("LOWER")
    else:
        print("NOT LOWER")
        
    option = input("Please enter 'YES' to input more or any key to stop")
    if option != "YES" and option != "yes":
        print("Thank you .. good bye")
        # RESET THE flag(isMoreInput) that is running this loop to false
        isMoreInput = False
