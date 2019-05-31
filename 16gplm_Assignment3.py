# Gabrielle Mehltretter 20065730 March 7, 2019
# This program is a spell checker.
# A word is typed into the program and if it is spelt wrong the program
# suggests low and high probabilty words for what the user meant.
# If the word is spelt correctly the program will print
# words similar to the given word.
# alphabet will be used later in a couple functions so I will set it now.

alphabet = "abcdefghijklmnopqrstuvwxyz"

#The readDictionary function retrieves the file with the dictionary
# so that it can be used throughout the program.

def readDictionary() :
    path = "/Users/ellie/Desktop/spellChecker/dictionaryfile.txt"
    try :
        dictionaryFile = open("dictionaryfile.txt", "r")
        a = []
        for line in dictionaryFile :
            for word in line.split() :
                a.append(word)
        dictionaryFile.close()
        return a
    except :
        setdic = set()
        print(setdic)
readDictionary()
# Let wordlen = the number of letters in the given word
#The next function takes the given word and removes each letter individually
# it will produce the same number of candidate words as letters in the given word

def removeLetterCandidate(targetWord) :
    candidates = []
    wordSize = len(targetWord)
    for pos in range(wordSize) :
        candidates.append(targetWord[0 : pos] + targetWord[pos + 1 : wordSize])   
    return candidates

#The next funtion takes the given word and swaps each letter
# this produces one less candidate word than letters in the given word

def swapLetterCandidate(targetWord) :
    candidates = []
    wordSize = len(targetWord)
    for pos in range(wordSize-1) :
        candidates.append(targetWord[: pos] + targetWord[pos + 1] + targetWord[pos] + targetWord[pos + 2 :])
    return candidates

#This function replaces each individual letter in the given word
# with every letter of the alphabet resulting in 26 * the number
# of letters in the given word candidate words

def replaceLetterCandidate(targetWord) :
    candidates = []
    wordSize = len(targetWord)
    for pos in range(wordSize) :
        for letter in alphabet :
            candidates.append(targetWord[: pos] + letter + targetWord[pos + 1:])
    return candidates

#The next function inserts every letter in the alphabet between
# each letter in the given word resulting in 26 * number of letters in the
# given word + 1 candidate words

def insertLetterCandidate(targetWord) :
    candidates = []
    wordSize = len(targetWord) + 1
    for pos in range(wordSize) :
        for letter in alphabet :
            candidates.append(targetWord[: pos] + letter + targetWord[pos :])
    return candidates

#this function uses each of the four list of candidate words to come
# up with a large set of candidate words with one change to the given word
# the high probability words will come from this set of words

def getOneEditWords(goal) :
    possibilities = []
    possibilities.extend(removeLetterCandidate(goal))
    possibilities.extend(swapLetterCandidate(goal))
    possibilities.extend(replaceLetterCandidate(goal))
    possibilities.extend(insertLetterCandidate(goal))
    return possibilities
    
# This function uses the set from the getOneEditWords to run through
# those possible words to change the word again using the four different ways
# this comes up with a set of words from the dictionary with two changes
# from the given word (low probability words)

def getTwoEditWords(goal) :
    
    possibilities = getOneEditWords(goal)
    morePossibilities = []
    for word in possibilities:
        morePossibilities.extend(removeLetterCandidate(word))
        morePossibilities.extend(swapLetterCandidate(word))
        morePossibilities.extend(replaceLetterCandidate(word))
        morePossibilities.extend(insertLetterCandidate(word))
    return morePossibilities

# For correctly spelt words this function will print
# similar words, this is similar to the high probability words
# for words misspelt

def getSimilarWords(goal) :
    wordSet1 = set(getOneEditWords(goal))

    highProbabilityWords = []
    for word in wordSet1 :
        if word in dictionary :
            highProbabilityWords.append(word)
    print("Similar words are: \n",highProbabilityWords)
    
#This function goes through all the candidate words to find
# which are actual words found in the dictionary
# it then prints the low probability words (two changes to the given
# word) and the high probability words (one change to the given word)
# for missplet words

def getPossibleWords(goal) :
    wordSet1 = set(getOneEditWords(goal))
    wordSet2 = set(getTwoEditWords(goal))
    word = True
    
    highProbabilityWords = []
    for word in wordSet1 :
        if word in dictionary :
            highProbabilityWords.append(word)
    print("High probability words \n",highProbabilityWords)

    lowProbabilityWords = []
    for word in wordSet2 :
        if word in dictionary :
            lowProbabilityWords.append(word)
    print("Low probability words \n",lowProbabilityWords)

# The main function calls in the dictionary and if dictionary
# does not exists then the program will close.
# The program will then prompt the user for a word to check.
# If the word is spelt correctly then the program will print words
# that are similar to the given word. If the word given was
# spelt incorrectly then the program will give high and
# low possibility words for what the user meant to type.
# If the user puts in characters other than the alphabet
# the program will tell the user to only use letters and promt
# them again for a word.

def main() :
    global dictionary
    dictionary = readDictionary()
    if len(dictionary) == 0 :
        print("Dictionary not available! Exiting program.")
        return

    while(True) :
        targetWord= input("Please enter a word you wish to check the spelling of (press <enter> to exit): ")
        if targetWord == "" :
            print("Shutting down...")
            break
        else :
            if targetWord in dictionary and targetWord.isalpha():
                print("You have spelled that word correctly!")
                getSimilarWords(targetWord)
            elif targetWord is not dictionary and targetWord.isalpha() : 
                getPossibleWords(targetWord)
            else :
                print("Use only letters in your word.")
main()
