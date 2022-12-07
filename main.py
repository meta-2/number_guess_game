import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5
def check_answer(choice,computer_choice,game):
    '''it is used to compare the user and computer choice. if both are same than return you win'''
    global turn
    if choice < computer_choice:
        print("too low")

        turn -= 1
        print(f"Now you have {turn} turns")
        return turn
    elif choice > computer_choice:
        print("too high")
        turn -= 1
        print(f"Now you have {turn} turns")
        return turn
    else:
        print(f"you got it!,computer choice is{computer_choice} and user choice is {choice}")
        game = False
        return game
def set_turn():
    ''':return the level esay ang hard, which is depend upon the user choice'''
    level = input("select the game level, easy and hard!")
    if level == "easy":
        print("you select easy level")
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN


print("welcome to the number guess game,")
print("think a number between 1 to 100")
computer_choice = random.randint(1,100)
print(f"computer choice is {computer_choice}")
turn = set_turn()
game = True
while game:
    choice = int(input("guess a  number between 1 to 100"))
    check_answer(choice,computer_choice,game)

    if turn == 0:
        print("you lose your all changes, you lose")
        game = False
    elif choice != computer_choice:
        print("guess again")
