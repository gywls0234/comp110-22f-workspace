"""EX03 - Structured Wordle."""

__author__ = "730617586"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool: 
    """Check if Any index in second string is in the first string."""
    assert len(char) == 1
    index = 0
    char_check = False
    while index < len(word):
        if word[index] == char:
            char_check = True
        index += 1
    if char_check is True:
        return True        
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Express green, yellow, white boxes depdending on whether the index on guess matches the index on secret."""
    assert len(guess) == len(secret)
    emojis: str = ""
    index = 0
    while index < len(str(secret)):
        if guess[index] == secret[index]:
            emojis = emojis + GREEN_BOX
        elif contains_char(secret, guess[index]):
            # add a yellow box
            emojis = emojis + YELLOW_BOX
        else: 
            emojis = emojis + WHITE_BOX         
        index = index + 1
    return emojis    


def input_guess(length: int) -> str:
    """Telling user to input the guess word."""
    input_guess: str = input(f"Enter a {length} character word: ")
    while length != len(input_guess):
        input_guess = input(f"That wasn't {length} chars! Try again: ")
    return input_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    game_won = False 
    turn_length = 6
    secret = "codes"
    length_secret = len(secret)
    turn = 1
    player_guess: str = ""

    while turn <= turn_length and game_won is False: 
        print(f"=== Turn {turn}/{turn_length} ===")
        player_guess = input_guess(length_secret)
        print(emojified(player_guess, secret))
        if player_guess == secret: 
            game_won = True 
        else: 
            turn = turn + 1 

    if game_won is False:
        print("X/6 - Sorry, try again tomorrow!")
    else:       
        print(f"You won in {turn}/6 turns!") 


if __name__ == "__main__":
    main()