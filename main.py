import random
from game_data import runs_data

print("WELCOME TO THE GAME")
print("GUESS WHO HAS THE HIGHEST RUNS IN A SINGLE IPL SEASON")
def formated_data(option):
    """format the data into printable format"""
    option_name = option["name"]
    option_runs = option["runs"]
    option_team = option["team"]
    return(f"{option_name} has played for {option_team}")

def check_answer(user_guess,option_01_runs,option_02_runs):
    if option_01_runs > option_02_runs:
        return user_guess == "1"
    else:
        return user_guess == "2"


print("WELCOME TO THE GAME")
print("GUESS WHO HAS THE HIGHEST RUNS IN A SINGLE IPL SEASON")
score = 0
should_continue = True
option_02 = random.choice(runs_data)
while should_continue:
    option_01 = option_02
    option_02 = random.choice(runs_data)
    if option_01 == option_02:
        option_02 = random.choice(runs_data)


    print('\n' )
    print(f" player 01 : {formated_data(option_01)}")
    print( "\t \t\t\t\t vs")
    print(f" player 02 : {formated_data(option_02)}")
    user_guess = input("who has more runs? 1 or 2: ").lower()

    option_01_runs = option_01["runs"]

    option_02_runs = option_02["runs"]

    is_correct = check_answer(user_guess,option_01_runs,option_02_runs)
    if is_correct :
        score += 1
        print(f"ur right !! | current score is {score}")
    else:
        print(f"smoked ! || final score is {score}")
        should_continue = False
