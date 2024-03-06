'''DISCLAIMER: Some words are not recognized by PyDictionary (ex: the)'''


# Used to check if input is a real word in the dictionary
from PyDictionary import PyDictionary
dictionary = PyDictionary()

POINTS = {
    "a": 1, "e": 1, "i": 1, "o": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1, "u": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10
}

def display_title():
    '''Displays program title'''
    print("Welcome to Assignment 1 - Scrabble")
    print("----------------------------------")


def error_check(word):
    '''Makes sure input is valid'''

    # Checks is word is alpha (A-Z)
    if not word.isalpha():
        print("Word must be only letters.")

    # Checks if there is more than one word (spaces)
    elif " " in word:
        print("Must be a single word.")

    # Checks for word in PyDictionary
    elif  not bool(dictionary.meaning(word, disable_errors=True)):
        print("Word was not found in dictionary.")

    else:
        return True



def calculate_score(word):
    '''Calculates the total score of the word'''
    
    score = 0
    # For each letter in the word add the score
    for l in word:
        score += POINTS[l]
    return score
           

def main():
    display_title()
    word = input("Enter a word: ").lower().strip()
    if error_check(word):
        print(calculate_score(word))


if __name__ == "__main__":
    main()