from random import randint
from enum import IntEnum
    
past_actions = []

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2

def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer")        


    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
        else:
            print("Paper covers rock, You lost!")

    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock, You won!")
        else:
            print("Scissors cut paper, You lost!")

    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Paper:
            print("Scissors cut paper, You won!")
        else:
            print("Rock smashes scissors, You lost!")

        

def get_computer_action():
    
    len_past_actions = len(past_actions)
    if len_past_actions == 0:
        return GameAction.Scissors
    else :
        if past_actions[len_past_actions].get("Victory") == 0:
            return past_actions[len_past_actions].get("rival_action")
        else:    
            if past_actions[len_past_actions].get("Victory") == 2:
                next_action = past_actions[len_past_actions].get("computer_action") - 1
                if next_action < 0:
                    next_action = 2
                return next_action    
            else:
                return randint(0,len(GameAction) - 1)
    


   





def get_user_action():
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection  = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'

def main():
    current_play = {}
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)


        if not play_another_round():
            break


if __name__=="__main__":
    main()