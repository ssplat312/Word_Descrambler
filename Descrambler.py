import requests

def factorial(num):
    newNum = 1
    for i in range(2, num + 1):
        newNum = newNum * i
    return newNum

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

def CheckWord(name):
    url = f"{baseUrl}{name}"

    response = requests.get(url)

    if(response.status_code == 200):
        data = response.json()
        print(f"{data[0]["word"]}")
    

baseUrl = "https://api.dictionaryapi.dev/api/v2/entries/en/"
name = input("Input a word you want to descramble: ")
answer = input("Do you want to descramble this word or get the possible combinations(Y/y for descramble and N/n for combinations): ")
print(f"Their are {factorial(len(name))} possible combinations of the word {name}.")
if answer == 'y' or answer == 'Y':
    print(f"The possible words that can be made from {name} are:")
    GetPossibleWords(name, len(name))
else:
    print(f"The combinations of words that can be made from {name} are:")
    GetWordCombinations(name, len(name))
    print(f"Here are {factorial(len(name))} combinations of the word {name}.")
print("Finished")