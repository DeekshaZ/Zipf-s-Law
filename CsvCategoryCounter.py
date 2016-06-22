__author__ = 'Deeksha'
import csv
import json

fileName = "Data/Road Safety - Vehicles by Make and Model 2012 v2.csv"
storeName = "Vehicles Accidents.txt"
categoriesDictionary = {}

with open(fileName,'r') as csvFile:
    reader = csv.reader(csvFile)
    stop = 1
    for row in reader:
        if stop == 1:
            stop = 0
        else:
            key = row[22].strip() + " " + row[23].strip()
            if key != '':
                if key not in categoriesDictionary.keys():
                    categoriesDictionary[key] = 0
                categoriesDictionary[key] += 1

array = []
for key in categoriesDictionary.keys():
    array.append( (key,categoriesDictionary[key]))

perfectArray = sorted(array,key=lambda tup: tup[1],reverse=True)

results = open("Data/Results - " + storeName,"w")
for perfectStuff in json.dumps(perfectArray, sort_keys=True, indent=4, separators=(',', ': ')):
    results.write(perfectStuff)
results.close()
print("FINISHED!!")
