students = [("Sally",["CompSci","Physics"]),("Robert",["Art","CompSci","Stats"]),("Charlotte",["CompSci","French","Economics"]),("Steve",["CompSci","French","Economics","CommLaw"]),("Carole",["Sociology","French","Law","Stats","Music"])]
counter = 0
uniquesub = set()
for (name,subjects) in students:
    print(name, "takes", len(subjects), "GCSEs")
    for s in subjects:
        uniquesub.add(s)
        if s == "CompSci":
            counter = counter + 1
print("The number of students taking Computer Science is", counter)
print("The number of unique subjects altogether is",len(uniquesub))
