# This contains the function in which the action of the game runs
from character_list import *

p1 = Stock()
p2 = Stock()


def battle_action(player1, player2):
    battle_running = True
    # priority list will contain the strings from the classes that determine the action
    # indexes 0 and 1 are not used yet, but maybe include function in the future
    # indexes 2 and 3 are the player action
    # indexes 4 and 5 check if each player is still alive
    priority_list = ["", "", "", "", "", ""]

    while battle_running:
        if player1.get_name() == "Stock" and player2.get_name() == "Stock":
            priority_list[4] = player1.get_is_alive()
            priority_list[5] = player2.get_is_alive()
            print("Your Moveset:")
            print("---------------")
            player1.get_moveset()
            print(f"Current Bullets: {player1.get_bullet_count()}")
            print(f"Current Number of Blocks: {player1.get_block_count()}")
            print()

            player1_choosing = True
            while player1_choosing:
                player_1_input = input("What will you do? ")
                if player_1_input == "1":
                    priority_list[2] = player1.reload()
                    player1_choosing = False
                elif player_1_input == "2":
                    priority_list[2] = player1.shoot()
                    player1_choosing = False
                elif player_1_input == "3":
                    priority_list[2] = player1.block()
                    player1_choosing = False
                elif player_1_input == "4":
                    priority_list[2] = player1.reflect()
                    player1_choosing = False
                else:
                    print("Invalid choice. Please choose again.")
                    print()


battle_action(p1, p2)
