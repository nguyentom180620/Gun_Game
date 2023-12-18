# Gun Game Project
# Start Date: 12/16/2023
# By Tom Nguyen
# Check Gun_Game.docx for more info of project guidelines

from Battle_Action import battle_action
from character_list import Stock, Samurai


def main():
    print("Welcome to Gun Game!")
    print()
    # First while loop for menu
    program_running = True
    while program_running:
        print("Gun Game Menu")
        print("-----------------")
        print("1. Start Game!")
        print("2. Character Wiki")
        print("3. Quit")
        print()
        menu_input = input("What would you like to do? ")
        print()
        if menu_input == "3":
            program_running = False
        elif menu_input == "2":
            # implement wiki class before proceeding
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
                    # Similar here
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
                    # Here implement classes so this saves Stock as P1 choice
                    p2 = Stock()
                    select_2_run = False
                elif player_2_choice == "2":
                    # Similar here
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
            battle_action(p1, p2)


main()
