def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def readDogDataCsvFileInto2dList(year):
    
    allLines = readFile("dog-licenses-"+str(year)+".csv")
    lines = []
    for line in allLines.splitlines():
        lines.append(line.split(","))

    return lines

def convert2dListToTable(data):
    table = []
    #appending the first row to retain
    table.append(data[0])

    for dt in data[1:]:
        dictionary = {"LicenseType":dt[0],"Breed":dt[1],"Color":dt[2],"DogName":dt[3],"OwnerZip":dt[4],"ExpYear":dt[5],"ValidDate":dt[6]}
        table.append(dictionary)

    return table
        

def cleanData(table):
    #2. Ignore table[0]
    for dt in table[1:]:
        for key in dt:
            # 1. Ignore all characters in the raw data that are neither alphanumeric nor whitespace. Hint: str.isalnum and str.isspace may be helpful here.

            valuesWithOutAlphanumericOrWhiteSpaces = ""

            for ch in dt[key]:
                if ch.isalnum() or ch.isspace() or ch=='/':
                    valuesWithOutAlphanumericOrWhiteSpaces = valuesWithOutAlphanumericOrWhiteSpaces + ch

            dt[key] = valuesWithOutAlphanumericOrWhiteSpaces

            # 3.Convert LicenseType to only be one of: 'Male', 'Female', or 'Unknown'           
            if key.lower() == "licensetype":
                if "female" in dt[key].lower():
                    dt[key] = "Female"
                elif "male" in dt[key].lower():
                    dt[key] = "Male"
                else:
                    dt[key] = "Unknown"
            # 4.Make the Breed be so-called Title Case, where the first letter of each word is uppercase, and all others are lowercase. You may find str.title to be especially useful here. :-)
            if key.lower() == "breed":
                dt[key] = dt[key].title()

            # 5. Make the Color a list of lowercase colors. So if the raw color is 'WHITE', the Color becomes ['white'], and if the raw color is 'WHITE/BROWN', the Color becomes ['white', 'brown'].
            if key.lower() == "color":
                colors = []
                for color in dt[key].split('/'):
                    #print("color",color)
                    colors.append(color.lower())

                dt[key] = colors

            # 6. The DogName should be Title Case.
            if key.lower() == "dogname":
                dt[key] = dt[key].title()

            # 7. The ExpYear should be an int (not a string)
            if key.lower() == "expyear":
                dt[key] = int(dt[key])


            # 8. The ValidDate should only be the year, as an int. So for example, you would convert '2017-11-27T10:42:11' to just 2017.
            if key.lower() == "validdate":
                dt[key] = int(dt[key][0:4])


def getCleanedTable(year):
    data = readDogDataCsvFileInto2dList(year)
    table = convert2dListToTable(data)
    cleanData(table)
    return table

def getValueSets(year):
    dogdictionary = dict()
    table = getCleanedTable(year)
    for dt in table[1:]:
        for key in dt:
            if dogdictionary.get(key,0) == 0:
                dogdictionary[key] = set()

            if type(dt[key]) is list:
                    for each in dt[key]:
                        dogdictionary[key].add(each)
            else:
                dogdictionary[key].add(dt[key])
                

    return dogdictionary
            

def getValueCounts(year):
    dogdictionary = dict()
    table = getCleanedTable(year)
    for dt in table[1:]:
        for key in dt:
            if dogdictionary.get(key,0) == 0:
                dogdictionary[key] = dict()

            if type(dt[key]) is list:
                    for each in dt[key]:
                        innerdictionary = dogdictionary[key]
                        count = 1 + innerdictionary.get(each, 0)
                        innerdictionary[each] = count
            else:
                value = dt[key]
                innerdictionary = dogdictionary[key]
                count = 1 + innerdictionary.get(value, 0)
                innerdictionary[value] = count

                    
                

    return dogdictionary


def getMostPopularValues(year):
    dogdictionary = getValueCounts(year)
    resultdictionary = dict()

    for keys in dogdictionary:
        max = -1
        content = set()
        value = ""
        for innerkeys in dogdictionary[keys]:
            if dogdictionary[keys][innerkeys]>=max:
                if dogdictionary[keys][innerkeys]>max:
                    max = dogdictionary[keys][innerkeys]
                    value = innerkeys
                    content.clear()
                content.add(innerkeys)

        if len(content) > 1:
            resultdictionary[keys] = content
        else:
            resultdictionary[keys] = value


    return resultdictionary
                
                
def someMoreDataAnalysis():
    resultdictionary = getMostPopularValues('2018-abridged')
    print(resultdictionary["OwnerZip"])
    return '''
Q1: What is the most popular zip code in the full 2018 data?
A1: 42

Q2: What is the most popular dog name in the full 2018 data?
A2: 42

Q3: What is the second-most-popular dog name in the full 2018 data?
A3: 42

Q4: What is the third-most-popular dog name in the full 2018 data?
A4: 42
'''        
    
    
        
            
#test data.......    

def testReadDogDataCsvFileInto2dList():
    print('Testing readDogDataCsvFileInto2dList()...', end='')
    data = readDogDataCsvFileInto2dList('2018-abridged')
    assert(data[0] == ['LicenseType','Breed','Color','DogName','OwnerZip',
                       'ExpYear','ValidDate'])
    assert(len(data) == 101)
    assert(data[-1] == ['Dog Senior Citizen or Disability Neutered Male',
                        'YORKSHIRE TERRIER', 'BLACK/BROWN', 'JACK', '15238',
                        '2018', '2017-11-29T09:47:37'])
    print('Passed!')


def testConvert2dListToTable():
    print('Testing convert2dListToTable()...', end='')
    data = readDogDataCsvFileInto2dList('2018-abridged')
    table = convert2dListToTable(data)
    assert(len(data) == len(table))
    assert(data[18] == ['Dog Individual Spayed Female', 'COCKER SPANIEL', 
                        'BLONDE', 'JUILET', '15214', '2018', 
                        '2017-11-27T10:42:11'])
    assert(table[18] == {'LicenseType': 'Dog Individual Spayed Female',
                         'Breed': 'COCKER SPANIEL',
                         'Color': 'BLONDE',
                         'DogName': 'JUILET', 
                         'OwnerZip': '15214', 
                         'ExpYear': '2018', 
                         'ValidDate': '2017-11-27T10:42:11'
                        })
    print('Passed!')


def testCleanData():
    print('Testing cleanData()...', end='')
    data = readDogDataCsvFileInto2dList('2018-abridged')
    table = convert2dListToTable(data)
    print("before", table[2]['Color'])
    cleanData(table) # note this works destructively!
    print(table[18])
    assert(table[18] == {'LicenseType': 'Female',
                         'Breed': 'Cocker Spaniel',
                         'Color': ['blonde'],
                         'DogName': 'Juilet', 
                         'OwnerZip': '15214', 
                         'ExpYear': 2018, 
                         'ValidDate': 2017
                        })
    # Note that the raw data for row 2 has the Color BLACK/BROWN
    print(table[2]['Color'])
    assert(table[2]['Color'] == ['black', 'brown'])
    # Note that the raw data for row 26 has the DogName "CHRISTINA ""TINA"""
    assert(table[26]['DogName'] == 'Christina Tina')
    print('Passed!')


def testGetCleanedTable():
    print('Testing getCleanedTable()...', end='')
    table = getCleanedTable('2018-abridged')
    assert(len(table) == 101)
    assert(table[18] == {'LicenseType': 'Female',
                         'Breed': 'Cocker Spaniel',
                         'Color': ['blonde'],
                         'DogName': 'Juilet', 
                         'OwnerZip': '15214', 
                         'ExpYear': 2018, 
                         'ValidDate': 2017
                        })
    print('Passed!')

def testGetValueSets():
    print('Testing getValueSets()...', end='')
    valueSets = getValueSets('2018-abridged')
    print(valueSets)
    assert(valueSets == {
        'LicenseType': {
            'Unknown', 'Female', 'Male'
            },
        'Breed': {
            'Cockapoo', 'Bichon Frise', 'Boxer Mix', 'Poodle Mix',
            'Am Pitt Bull Mix', 'Brittany Spaniel', 'Beagle', 'Shepherd Mix',
            'Maltese Mix', 'Terrier Mix', 'Morkie', 'Aus Shepherd', 'Tag',
            'Am Pit Bull Terrier', 'Mixed', 'Tree Walk Coonhound',
            'Great Dane', 'Golden Retriever', 'Beagle Mix', 'Shih Tzu',
            'Akita', 'Ger Shepherd', 'Cane Corso', 'Weimaraner',
            'Goldendoodle', 'Poodle Standard', 'Belg Malinois',
            'Ger Shepherd Mix', 'Sib Husky', 'Estrela Mtn Dog', 'Chihuahua',
            'Maltese', 'Doberman Pinscher', 'Rat Terrier',
            'Labrador Retriever', 'Min Pinscher', 'Doberman Mix',
            'Yorkshire Terrier', 'Greyhound', 'Dachshund Mix', 'Keeshond',
            'Shetland Sheepdog', 'Lab Mix', 'Scottish Terrier',
            'Cocker Spaniel', 'Portugese Water Dog', 'Lhasa Apso Mix',
            'Yorkshire Terr Mix', 'Havanese'
            },
        'Color': {
            'grey', '', 'yellow', 'tan', 'brown', 'buff', 'red', 'cream',
            'gold', 'orange', 'brindle', 'blonde', 'spotted', 'multi',
            'black', 'white'},
        'DogName': {
            'Rosie ', 'Tucker', 'Rusty', 'Isis', 'Juilet', 'Gus', 'Romeo',
            'Doggie', 'Taffy', 'Karma', 'Bumble', 'Sable', 'Jessie', 'Lola',
            'Luna', 'Happy', 'Jake', 'Neena', 'Baloo', 'Buddy', 'Maeby Axford',
            'Eich', 'Honey Puck', 'Toby', 'Stella', 'Abe', 'Valkyrie', 'Carly',
            'Chickie', 'Aslan Mcgregor', 'Princess', 'Duke',
            'Rufus Gerald Wallace', 'Emily', 'Nahbi', 'Norman Mitchell',
            'Cissie Bear', 'Hunter', 'Molly Magee', 'Bailey', 'Howie',
            'Zoe Vitsas', 'Bruno', 'Dakota', 'Charley', 'Sisco', 'Molly',
            'Zeta', 'Jack', 'Shadoe', 'Annie', 'Charlie', 'Willie', 'Cobalt',
            'Bear', 'Roxy', 'Saint', 'Lilly', 'Oakley', 'Clover', 'Joe',
            'Christina Tina', 'Chloe', 'Murphy', 'Cooper', 'Tacoda',
            'Mimi Pearl Foster', 'Ellie', 'Tonks', 'Rosie', 'Teddy', 'King',
            'Leroi', 'Dude', 'Arrow', 'Titan', 'Luce', 'Bandit', 'Bojangles',
            'Baley', 'Missy', 'Jackson', 'Sydney', 'Maggie', 'Curious George',
            'Snowball', 'Winnie', 'Madeleine', 'Izzy'
            },
        'OwnerZip': {
            '15120', '15221', '15126', '15131', '15068', '15133', '15218',
            '15129', '15136', '15209', '15147', '15057', '15104', '15108',
            '15227', '15116', '15237', '15018', '15137', '15101', '15236',
            '15017', '15205', '15202', '15148', '15102', '15090', '15234',
            '15220', '15146', '15139', '15228', '15044', '15239', '15042',
            '15135', '15238', '15025', '15214', '15045', '15122', '15106',
            '15241', '15235', '15229'
            },
        'ExpYear': {
            2018
            },
        'ValidDate': {
            2017
            }
        })
    print('Passed!')


def testGetValueCounts():
    print('Testing getValueCounts()...', end='')
    valueCounts = getValueCounts('2018-abridged')
    print(valueCounts)
    assert(valueCounts == {
        'LicenseType': {
            'Male': 47, 'Female': 52, 'Unknown': 1
            },
        'Breed': {
            'Cockapoo': 2, 'Ger Shepherd': 4, 'Belg Malinois': 1, 'Mixed': 9, 
            'Am Pit Bull Terrier': 1, 'Scottish Terrier': 1, 
            'Yorkshire Terrier': 4, 'Dachshund Mix': 2, 'Shetland Sheepdog': 2,
            'Labrador Retriever': 5, 'Bichon Frise': 2, 'Lhasa Apso Mix': 1,
            'Am Pitt Bull Mix': 4, 'Brittany Spaniel': 2, 'Terrier Mix': 4,
            'Cocker Spaniel': 3, 'Maltese': 5, 'Lab Mix': 5, 'Havanese': 1,
            'Akita': 1, 'Beagle Mix': 2, 'Doberman Mix': 1, 'Shih Tzu': 2,
            'Ger Shepherd Mix': 1, 'Doberman Pinscher': 1, 'Greyhound': 1,
            'Chihuahua': 1, 'Beagle': 3, 'Morkie': 1, 'Aus Shepherd': 1,
            'Poodle Standard': 1, 'Tree Walk Coonhound': 1, 'Great Dane': 1,
            'Estrela Mtn Dog': 1, 'Boxer Mix': 1, 'Portugese Water Dog': 1,
            'Golden Retriever': 6, 'Maltese Mix': 1, 'Weimaraner': 1,
            'Shepherd Mix': 1, 'Cane Corso': 1, 'Sib Husky': 2,
            'Poodle Mix': 1, 'Rat Terrier': 1, 'Keeshond': 1,
            'Yorkshire Terr Mix': 1, 'Min Pinscher': 1, 'Goldendoodle': 1,
            'Tag': 3
            },
        'Color': {
            'brown': 40, 'black': 42, 'brindle': 3, 'white': 36, 'tan': 7,
            'yellow': 1, 'spotted': 3, 'blonde': 3, 'multi': 3, 'orange': 1, 
            'cream': 2, 'red': 1, 'grey': 3, '': 1, 'gold': 3, 'buff': 1
            },
        'DogName': {
            'Charley': 1, 'Tacoda': 1, 'Eich': 1, 'Arrow': 1, 'Oakley': 1,
            'Bailey': 1, 'Mimi Pearl Foster': 1, 'Leroi': 1, 'Zoe Vitsas': 1,
            'Taffy': 1, 'Dude': 1, 'Chickie': 1, 'King': 1, 'Emily': 1,
            'Ellie': 3, 'Rusty': 1, 'Annie': 1, 'Juilet': 1, 'Romeo': 1,
            'Lola': 3, 'Abe': 1, 'Maggie': 2, 'Buddy': 1, 'Princess': 1,
            'Christina Tina': 1, 'Howie': 1, 'Happy': 1, 'Lilly': 1,
            'Shadoe': 1, 'Sable': 1, 'Nahbi': 1, 'Valkyrie': 1, 'Doggie': 1,
            'Curious George': 1, 'Willie': 1, 'Snowball': 2, 'Honey Puck': 1,
            'Roxy': 1, 'Bumble': 1, 'Bojangles': 1, 'Stella': 1,
            'Norman Mitchell': 1, 'Winnie': 1, 'Molly Magee': 1,
            'Madeleine': 1, 'Bandit': 1, 'Karma': 1, 'Dakota': 1,
            'Clover': 1, 'Titan': 1, 'Luna': 1, 'Maeby Axford': 2,
            'Saint': 1, 'Luce': 1, 'Baloo': 1, 'Rufus Gerald Wallace': 1,
            'Baley': 1, 'Joe': 1, 'Jackson': 1, 'Teddy': 1,
            'Aslan Mcgregor': 1, 'Charlie': 2, 'Murphy': 1, 'Bear': 1,
            'Cooper': 2, 'Rosie ': 1, 'Hunter': 1, 'Zeta': 1, 'Duke': 1,
            'Bruno': 1, 'Molly': 1, 'Tucker': 1, 'Chloe': 1, 'Gus': 1,
            'Rosie': 1, 'Sydney': 1, 'Sisco': 1, 'Izzy': 1, 'Cissie Bear': 1,
            'Neena': 1, 'Toby': 1, 'Jessie': 1, 'Cobalt': 1, 'Isis': 1,
            'Tonks': 1, 'Carly': 1, 'Jake': 1, 'Missy': 3, 'Jack': 1
            },
        'OwnerZip': {
            '15236': 1, '15238': 6, '15104': 1, '15139': 4, '15129': 1,
            '15090': 1, '15101': 2, '15228': 3, '15235': 5, '15108': 5,
            '15120': 2, '15239': 7, '15214': 2, '15218': 4, '15237': 1,
            '15018': 2, '15025': 4, '15017': 1, '15137': 1, '15045': 2, 
            '15131': 1, '15136': 5, '15205': 4, '15122': 1, '15234': 1, 
            '15057': 1, '15241': 3, '15147': 1, '15135': 2, '15044': 3,
            '15126': 1, '15229': 2, '15221': 2, '15102': 1, '15202': 2, 
            '15227': 1, '15148': 1, '15133': 2, '15209': 2, '15146': 1, 
            '15116': 3, '15106': 2, '15042': 1, '15068': 1, '15220': 1
            },
        'ExpYear': {
            2018: 100
            },
        'ValidDate': {
            2017: 100
            }
        })
    print('Passed!')


def testGetMostPopularValues():
    print('Testing getMostPopularValues()...', end='')
    print(getMostPopularValues('2018-abridged'))
    assert(getMostPopularValues('2018-abridged') == {
        'LicenseType': 'Female',
        'Breed': 'Mixed',
        'Color': 'black',
        'DogName': {'Ellie', 'Lola', 'Missy'},
        'OwnerZip': '15239',
        'ExpYear': 2018,
        'ValidDate': 2017
        })
    print('Passed!')


def testSomeMoreDataAnalysis():
    someMoreDataAnalysis()
    print('Skipping testing for someMoreDataAnalysis().  :-)')

testReadDogDataCsvFileInto2dList()
testConvert2dListToTable()
testCleanData()
testGetCleanedTable()
testGetValueSets()
testGetValueCounts()
testGetMostPopularValues()
testSomeMoreDataAnalysis()

    



