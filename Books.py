__author__ = 'Deeksha'

import string
import json

def hasLetters(word):
    for letter in word:
        if letter in string.ascii_letters:
            return True
    return False

def trimWord(word):
    while word[0] not in string.ascii_letters and len(word) != 0:
        word = word[1:]
    while word[-1] not in string.ascii_letters and len(word) != 0:
        word = word[:-1]
    return word


bookName = input("Input the book file name:  ")
bookName1 = "Data/"+bookName
bookFile = open(bookName1,"r")

wordsCount = {}
perfectArray = []

for line in bookFile:
    for word in line.replace("--"," ").split():
        lowerWord = word.lower()
        if hasLetters(lowerWord):
            perfectWord = trimWord(lowerWord)
            if perfectWord not in wordsCount.keys():
                wordsCount[perfectWord] = 0
            wordsCount[perfectWord] = wordsCount[perfectWord] + 1

for word in sorted(wordsCount,key = wordsCount.get,reverse=True):
    perfectArray.append( (word, wordsCount[word]) )

results = open("Data/Results - " + bookName,"w")
for perfectStuff in json.dumps(perfectArray, sort_keys=True, indent=4, separators=(',', ': ')):
    results.write(perfectStuff)
results.close()
print("FINISHED!!")




