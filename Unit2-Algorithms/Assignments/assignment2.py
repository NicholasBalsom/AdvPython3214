# Write a recursive function that determines whether or not a string is a palindrome

# --------------------> start and end positions of word
def palindrome(word:str, start:int, end:int):
    # If start postition equals end position (one letter left to check)
    if start >= end:
        return True
    # If first and last letters are not equal
    if word[start] != word[end]:
        return False
    # Moves start pos + 1 and end - 1 and recursively checks
    return palindrome(word, start+1, end-1)
    

def main():
    word = input("Input word: ")
    # Gets rid of spaces
    pal_word = word.replace(" ", "").lower()
    length = len(pal_word)

    if length == 0:
        print("An empty string is still considered a palindrome!")

    if palindrome(pal_word, 0, length-1):
        print(f"'{word}' is a palindrome!")
    else:
        print(f"'{word}' is NOT a palindrome.")


if __name__ == "__main__":
    main()
