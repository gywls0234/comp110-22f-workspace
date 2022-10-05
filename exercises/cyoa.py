"""EX06 - Choose Your Own Adventure."""

__author__ = "730617586"

from random import randint
face_1: str = "U+263A"
face_2: str = "U+1F619"

points: int
player: str


def main() -> None:
    """Moving to greeting function."""
    global points
    points = 0

    greet()

    still_playing: bool = True

    # while loop
    while still_playing:
      options = input(f"{player} is at a fork in the road. Which way you want to go? Right? Left? or Stop playing")
    
    if options == "Stop playing":
      print("Goodbye!")
      points += 0

    if options == "Right":
      Right()

    if options == "Left":
      points = Left(points)

    faces = [face_1, face_2]
    print("Thanks for playing this game!" + randint(faces))


def greet() -> None: 
    """Greeting player."""
    print(f"Welcome! This is a choice game, so depending on which option you choose, you will get different amount of advanture points.")
    player = input("Enter your player name.")


def Right() -> None:
    """When player goes to right."""
    global points
    global player
    print(f"While {player} was going to right, you found a rainbow-colored mushroom! Do want to eat this? Yes? or No?")
    mushroom: str = input(f"While {player} was going to right, you found a rainbow-colored mushroom! Do want to eat this? Yes? or No?")
  
    if mushroom == "Yes":
      print("It was a poisonous mushroom! Game over!")
      points += 30
    else: 
      points += 20


def Left(points: int) -> int:
    """When player goes to left."""
    print(f"While {player} was going to left, you realized someone is behiind you! Do you want to look back? Yes? or No?")
    someone: str = input(f"While {player} was going to left, you realized someone is behiind you! Do you want to look back? Yes? or No?")
    
    if someone == "Yes": 
      print(f"It was your mom! Fortunately, you were able to come back to home with your mom. Happy Ending!")
      mom: str = input(f"It was your mom! Fortunately, you were able to come back to home with your mom. Happy Ending!")
      points += 30
    
    else: 
      print(f"{player} still keeps waling, but eventually {player} gets lost! No way to go back to home! Game Over!")
      points += 20

    return points


if __name__ == "__main__":
    main()