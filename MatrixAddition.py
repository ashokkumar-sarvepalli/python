rows2019 = int(input("Please enter number of events in year 2019"))
columns2019 = int(input("Please enter number of contributos in year 2019"))
total = [[0],[0],[0]]

year2019 = []
for i in range(rows2019):
    arr = []
    print("Enter the numbers for row:",i+1)
    for j in range(columns2019):
        arr.append(int(input()))
    year2019.append(arr)


rows2020 = int(input("Please enter number of events in year 2020"))
columns2020 = int(input("Please enter number of contir in year 2020"))

if(rows2019==rows2020 and columns2019==columns2020):

    year2020 = []
    for i in range(rows2020):
        arr = []
        print("Enter the numbers for row:",i+1)
        for j in range(columns2020):
            arr.append(int(input()))
        year2020.append(arr)


    for i in range(rows2019):
        for j in range(columns2019):
            total[i][j] = year2019[i][j] + year2020[i][j]

    print(total)
        
    
