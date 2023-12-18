# Gun Game Project
# Start Date: 12/16/2023
# By Tom Nguyen
# Check Gun_Game.docx for more info of project guidelines

from Battle_Action import battle_action
from wiki import wiki
from character_list import Stock, Samurai


def main():
    print("Welcome to Gun Game!")
    print()
    # First while loop for menu
    program_running = True
    p1_score = 0
    p2_score = 0
    while program_running:
        if p1_score or p2_score != 0:
            print(f"Your Score: {p1_score}, AI Score: {p2_score}, Win Rate: {int(p1_score/(p1_score+p2_score)*100)}%")
        print("Gun Game Menu")
        print("-----------------")
        print("1. Start Game!")
        print("2. Game Wiki")
        print("0. Quit")
        print()
        menu_input = input("What would you like to do? ")
        print()
        if menu_input == "0":
            program_running = False
        elif menu_input == "2":
            wiki()
            pass
        elif menu_input != "1":
            print("Invalid menu choice! Please enter a valid option.")
            print()
        else:
            # First Character Select
            select_1_run = True
            while select_1_run:
                print("Select your character:")
                print("-----------------------------------")
                print("1. Stock")
                print("2. Samurai")
                print()
                player_1_choice = input("Choice: ")
                if player_1_choice == "1":
                    # Here implement classes so this saves Stock as P1 choice
                    p1 = Stock()
                    select_1_run = False
                elif player_1_choice == "2":
                    p1 = Samurai()
                    select_1_run = False
                else:
                    print("Invalid choice, try again.")
                    print()
            print()

            # Second Character Select
            select_2_run = True
            while select_2_run:
                print("Select your opponent's character:")
                print("-----------------------------------")
                print("1. Stock")
                print("2. Samurai")
                print()
                player_2_choice = input("Choice: ")
                if player_2_choice == "1":
                    p2 = Stock()
                    select_2_run = False
                elif player_2_choice == "2":
                    p2 = Samurai()
                    select_2_run = False
                else:
                    print("Invalid choice, try again.")
                    print()
            print()
            print()
            print("BATTLE START!")
            print("--------------")
            print(f"You are {p1.get_name()}, your opponent is {p2.get_name()}")
            print()
            result = battle_action(p1, p2)
            if result == "Draw":
                pass
            elif result == "P1 Win":
                p1_score += 1
            elif result == "P2 Win":
                p2_score += 1
            else:
                pass


main()
