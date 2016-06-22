__author__ = 'Deeksha'

import csv
import json

choice = int(input("Press 1 for City Population in the US\nPress 2 for country population in the world\n"))
if(choice == 1 or choice == 2) :
    if(choice == 1) :
        csvCategoryPosition = 5
        csvCountPosition = 18
        fileName = 'Data/cityPopulation.csv'
        storeName = 'City Population.txt'
    elif(choice == 2):
        csvCategoryPosition = 2
        csvCountPosition = 14
        fileName = 'Data/worldPopulation.csv'
        storeName = 'World Population.txt'
    arrayOfEntries = []
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        stop = 1
        if choice == 1 :
            for row in reader:
                if(row[0] != '40' and row[0] != '50' and row[2] == '0' and ("balance" not in row[5])):
                    if stop == 1:
                        stop = 0
                    elif not int(row[csvCountPosition]) == 0:
                        arrayOfEntries.append((row[csvCategoryPosition],int(row[csvCountPosition]) ))
        else :
            for row in reader:
                if stop == 1:
                    stop = 0
                elif not int(row[csvCountPosition]) == 0:
                    arrayOfEntries.append((row[csvCategoryPosition],int(row[csvCountPosition]) ))

    setOfEntries = set()
    for entry in arrayOfEntries:
        setOfEntries.add(entry)

    filteredArray = []
    for entry in setOfEntries:
        filteredArray.append(entry)

    PerfectArray = sorted(filteredArray, key=lambda tup: tup[1],reverse=True)


    results = open("Data/Results - " + storeName,"w")
    for perfectStuff in json.dumps(PerfectArray, sort_keys=True, indent=4, separators=(',', ': ')):
        results.write(perfectStuff)
    results.close()
    print("FINISHED!!")
else :
    print("Wrong selection")
