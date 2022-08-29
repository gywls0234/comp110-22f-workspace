"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730617586"

word: str= input("Enter a 5-character word")

character: str= input("Enter a single character")
print("searching for" + character + "in"+ word)

counting: int= 0 

if len(word) != 5:
    exit("Error: Word must contain 5 characters")

if len(character) != 1:
    exit("Error: Character must be a single character.")


if character == word[0]: 
    print(character + "found at index 0")
    counting = counting + 1




if character == word[1]:
    print(character + "found at index 1")
    counting = counting + 1


if character == word[2]:
    print(character + "found at index 2")
    counting = counting + 1

if character == word[3]:
    print(character + "found at index 3")
    counting = counting + 1

if character == word[4]:
    print(character + "found at index 4")
    counting = counting + 1

if counting == 0:
    print("No instances of" + character + "found in world")

if counting == 1:
    print("1 instance of" + character + "found in world")



 
