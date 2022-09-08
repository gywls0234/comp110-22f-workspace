"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730617586"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

counting: int = 0 
 

if character == word[0]: 
    print(character + " found at index 0")
    counting = counting + 1
if character == word[1]:
    print(character + " found at index 1")
    counting = counting + 1
if character == word[2]:
    print(character + " found at index 2")
    counting = counting + 1
if character == word[3]:
    print(character + " found at index 3")
    counting = counting + 1
if character == word[4]:
    print(character + " found at index 4")
    counting = counting + 1

if counting == 1:
    print("1 instance of " + character + " found in " + word)

if counting > 1:
    print(str(counting) + " instances of " + character + " found in " + word)

if counting == 0:
    print("No instances of " + character + " found in " + word)
    



 
