rows = int(input("enter number of cubes"))
columns = 3
cubeDimensions= []
# cubeDimensions = [[10,20,40],[54,35,60],[30,40,50]]
# print(cubeDimensions) // [[10,20,40],[54,35,60],[30,40,50]]
# print(cubeDimensions[0]) // [10,20,40]
# print(cubeDimensions[0][0]) // 10
# print(cubeDimensions[2][1]) // 40
for i in range(rows):
    arr =[]
    print("enter dimensions of cube ",i+1)
    for j in range(columns):
        arr.append(int(input()))
    cubeDimensions.append(arr)


increasePositions = []


for i in range(rows):
    arr =[]
    print("enter the increase in position of cube ",i+1)
    for j in range(columns):
        arr.append(int(input()))
    increasePositions.append(arr)


print(cubeDimensions)
print(increasePositions)

newCubeDimensions = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(rows):
    for j in range(columns):
        newCubeDimensions[i][j] = cubeDimensions[i][j] + increasePositions[i][j]
        
print(newCubeDimensions)

