"""EX06 - Choose Your Own Adventure."""

__author__ = "730617586"

from random import randint
FACE_1: str = "\U0002F63A"
FACE_2: str = "\U0001F619"

points: int
player: str
still_playing: bool = True


def main() -> None:
    """Moving to greeting function."""
    global points
    global still_playing
    points = 0

    greet()

    # while loop
    while still_playing:
        options: str = input(f"{player} is at a fork in the road. Which way you want to go? Right? Left? or Stop playing")
    
        if options == "Stop playing":
            print("Goodbye!")
            still_playing = False
            points += 0

        if options == "Right":
            Right()
            still_playing = False

        if options == "Left":
            points = Left(points)

    faces: list[str] = [FACE_1, FACE_2]
    print("Thanks for playing this game!" + faces[randint(0, 1)])


def greet() -> None: 
    """Greeting player."""
    global player
    print("Welcome! This is a choice game, so depending on which option you choose, you will get different amount of advanture points.")
    player = input("Enter your player name.")


def Right() -> None:
    """When player goes to right."""
    global points
    global player
    mushroom: str = input(f"While {player} was going to right, you found a rainbow-colored mushroom! Do want to eat this? Yes? or No?")
  
    if mushroom == "Yes":
        print("It was a poisonous mushroom! Game over!")
        points += 30
    else: 
        points += 20
        Left(points)


def Left(points: int) -> int:
    """When player goes to left."""
    global player
    someone: str = input(f"While {player} was going to left, you realized someone is behiind you! Do you want to look back? Yes? or No?")
    
    if someone == "Yes": 
        print("It was your mom! Fortunately, you were able to come back to home with your mom. Happy Ending!")
        points += 30
    
    else: 
        print(f"{player} still keeps waling, but eventually {player} gets lost! No way to go back to home! Game Over!")
        points += 20

    return points


if __name__ == "__main__":
    main()