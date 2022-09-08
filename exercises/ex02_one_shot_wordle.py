"""EX02 - One Shot Wordle."""

__author__ = "730617586"

secret = "python"
index = 0
emojis = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")

while len(guess) != len(secret):
    print(f"That was not " + str(len(secret)) + "-letters! Try again: ")
    exit()
    
while index < len(secret):
    if guess[index] == secret[index]:
        emojis = emojis + GREEN_BOX
    else:
        guessed_character : bool = False 
        i : int = 0
        while guessed_character is not True and i < len(secret):
            if guess[index] == secret[i]:
                guessed_character = True 
            else: i = i + 1

        if guessed_character is True:
            emojis = emojis + YELLOW_BOX
        else : emojis = emojis + WHITE_BOX 
        
    
               
    index = index + 1

print(emojis)



if guess == secret:
    print(f"Woo! You got it!")
else:
    print(f"Not quite. Play again soon!")

