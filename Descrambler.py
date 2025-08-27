import requests
import time
from dotenv import load_dotenv
import os

def factorial(num):
    newNum = 1
    for i in range(2, num + 1):
        newNum = newNum * i
    return newNum

def GetConfidence(word, desiredWord):
    
    confidence = (len(word)/len(desiredWord)) * 100 if len(word) <= len(desiredWord) else (len(desiredWord)/len(word)) * 100
    confidence = confidence/2
    charInSet = 0
    charsUsed = set(word)

    for letter in desiredWord:
        if letter in charsUsed:
            charInSet = charInSet + 1

    confidence = confidence + ((charInSet/len(desiredWord) * 100)/2)

    return confidence

def GetPossibleWords(baseWord, curLength):    
    startPos = len(baseWord) - curLength
    for i in range(startPos, len(baseWord)):
        baseWord = list(baseWord)
        tempLetter = baseWord[i]
        baseWord[i] = baseWord[startPos]
        baseWord[startPos] = tempLetter 
        baseWord = ''.join(baseWord)
        if curLength > 2:
            GetPossibleWords(baseWord, curLength - 1)
        else:
            CheckWord(baseWord)

def GetWordCombinations(baseWord, curLength):
    startPos = len(baseWord) - curLength
    for i in range(startPos, len(baseWord)):
        baseWord = list(baseWord)
        tempLetter = baseWord[i]
        baseWord[i] = baseWord[startPos]
        baseWord[startPos] = tempLetter 
        baseWord = ''.join(baseWord)
        if curLength > 2:
            GetWordCombinations(baseWord, curLength - 1)
        else:
            print(baseWord)

def CheckWord(word):
    url = os.environ.get("DictionaryUrl")

    querystring = {"term":word}

    headers = {
        "x-rapidapi-key": os.environ.get("DictionaryApi"),
        "x-rapidapi-host": os.environ.get("DictionaryHost")
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        PrintWord(response.json())

def PrintWord(wordsInfo):
    answer = "y"
    curWord = 0
    maxWord = len(wordsInfo["list"])
    
    for wordInfo in wordsInfo["list"]:
        cofindence = GetConfidence(wordInfo["word"], name)
        if desiredConfidence > cofindence:
            print(f"Word only had {cofindence} instead of {desiredConfidence} or above")
            continue

        if answer != 'y' and answer != "Y":
            break
        curWord = curWord + 1
        print(f"1.{wordInfo["word"]}: {wordInfo["definition"]}")
        print(f"Example sentence: {wordInfo["example"]}\n")
        time.sleep(3)
        if curWord < maxWord:
            print(f"You are on word {curWord} of {maxWord}.\n Press Y/y to see the next one, anything else to stop.")
            answer = input("Input here:")

load_dotenv()

name = input("Input a word you want to descramble: ")
answer = input("Do you want to descramble this word or get the possible combinations(Y/y for descramble and N/n for combinations): ")


print(f"Their are {factorial(len(name))} possible combinations of the word {name}.")

if answer == 'y' or answer == 'Y':
    #confidence is the length of the word found over the length of letters in the scrambled word
    desiredConfidence = int(input("What confidence do you want to have for the unscrambled words(choose between inclusive 1 and 100)?: "))
    print(f"The possible words that can be made from {name} are:")
    GetPossibleWords(name, len(name))
else:
    print(f"The combinations of words that can be made from {name} are:")
    GetWordCombinations(name, len(name))
    print(f"Here are {factorial(len(name))} combinations of the word {name}.")

print("Finished")