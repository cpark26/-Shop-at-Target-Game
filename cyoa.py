"""EX06 - making your own game."""
__author__ = "730611743"

from random import randint

star_head: str = "\U0001F929"
think_bubble: str = "\U0001F4AD"
bye_hand: str = "\U0001F44B"
eye: str = "\U0001F440"
silouette: str = "\U0001F464"
frog: str = "\U0001F438"
ball: str = "\U000026BD"
rainbow: str = "\U0001F308"
skate: str = "\U000026F8"
food: str = "\U0001F35C"
start: str = "\U0001F4CD"
money: str = "\U0001F4B5"
player: str = ""
points: int = 0


def greet() -> None:
    """Prints a welcome statement for the player."""
    global player
    print(f"{frog} Welcome to \"What happens at Franklin?: Target\" You have four players to choose from: \n{food} Lucia\n{skate}  Abi\n{ball} Danny\n{rainbow} Jennifer\nThey're freshmans at UNC Chapel Hill and good friends {star_head}\nIn this game, you're goal is to predict what you're character will buy at Target.")
    player = input("Choose your character! What is your name? ")
    print(f"Hi {player}! A tip for you before the game starts!\nMake sure to type in choices inside the paranthesis only. Good luck!")


def done() -> None:
    """Prints a byebye statement when player finishes the game."""
    print(f"{silouette}Good job finishing the game! Thanks to you, {player} successfully finished shopping from Target.")
    print(f"{bye_hand}END OF GAME: Your score is {points} / 30! Bye!{bye_hand}")


def store(s_answer: str) -> None:
    """Simulates what will happen when player wants to exit the store."""
    global points
    if s_answer == "Lucia":
        points += 30
        print(f"{silouette}{player}: Oops! I meant to go to Trader Joes, bye!\n{think_bubble}Lucia goes to Trader Joes every week!")
    else:
        points = -10
        print(f"{silouette}{player}: Hmm..I guess I'll leave\n{think_bubble} {player} headed to the Davis library but couldn't finish EX06...too tired to study and no snacks to eat!")
    

def drinks() -> None:
    """Simulates what will happen when a player decides to purchase a drink."""
    global points
    what_d = input(f"Hey {player}. Which drink do you want? (Celsius / Starbucks) ")
    if what_d == "Starbucks":
        points -= 10
        print(f"{think_bubble} Starbucks at Target doesn't taste nice. {player} would rather go to Yaya Tea.")
    if what_d == "Celsius":
        if not player == "Abi":
            points += 20
            print(f"{silouette}{player}: Gotta get Abi that Celsius!")
        else:
            points += 10
            print(f"{silouette}{player}: I need that Celsius to run and study!")
    print(f"{frog}Your score is {points} / 30!")


def snacks(score: int) -> int:
    """Simulates what will happen when a player decides to purchase a snack."""
    extra: int = randint(0, 10)
    how_many: int = int(input(f"{player}, how many clif bars do you want to buy? (0 / 1 / 2) "))
    if how_many == 0:
        if player == "Abi":
            print(f"{silouette}{player}: I can't go through a week without my clif bars...")
        else:
            score += 5
            print(f"{silouette}{player}: I guess I don't need any.")
    if how_many == 1:
        score += 10
        if player == "Abi":
            print(f"{silouette}{player}: I'll have to come back next week")
        else:
            print(f"{silouette}{player}: I'll try one! I might eat it tonight while studying for compsci. ")
    if how_many == 2:
        if player == "Abi":
            score += 20
            print(f"{silouette}{player}: I need my clif bars! Never forget these! ")
        else:
            score += 10
            print(f"{silouette}{player}: I guess I'll share one with Abi then. ")
    score += extra
    print(f"{frog} You got bonus points for playing this game! (+{extra}pt)\n{frog} Your score is {score} / 30!")
    return score
        
        
def main() -> None:
    """Allows player to play the game What happens at Franklin: Target."""
    ask_again: str = "True"
    global points
    greet()
    print(f"{start} S T A R T")
    print(f"{think_bubble} Hooray! You arrived at {money}Target{money}! ")
    while ask_again == "True": 
        first_ask: str = input("What do you want to do first? (buy drinks / buy clif bar / exit the store): ")
        if first_ask == "exit the store":
            store(player)
            ask_again = "False"
        if first_ask == "buy drinks":
            drinks()
            points = snacks(points)
        if first_ask == "buy clif bar":
            points = snacks(points)
            drinks()
        done()
        again: str = input(f"{frog}Would you like to play again? (Yes / No) ")
        if again == "Yes":
            points = 0
        else:
            quit()     


if __name__ == "__main__":
    main()