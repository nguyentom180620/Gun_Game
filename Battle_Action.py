# This contains the function in which the action of the game runs
from character_list import *
from random import choice

p1 = Samurai()
p2 = Stock()


def battle_action(player1, player2):
    battle_running = True
    # priority list will contain the strings from the classes that determine the action
    # indexes 0 and 1 are not used yet, but maybe include function in the future
    # indexes 2 and 3 are the player action
    # indexes 4 and 5 check if each player is still alive
    priority_list = ["", "", "", "", "", ""]

    while battle_running:
        # Stock vs Stock
        if player1.get_name() == "Stock" and player2.get_name() == "Stock":
            priority_list[4] = player1.get_is_alive()
            priority_list[5] = player2.get_is_alive()
            if not (priority_list[4] and priority_list[5]):
                break
            print("Your Moveset:")
            print("---------------")
            player1.get_moveset()
            print(f"{f"Your Current Bullets: {player1.get_bullet_count()}": <20}"
                  f"{f"Your Opponent's Bullets: {player2.get_bullet_count()}": >50}"
                  )
            print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
                  f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
            print()

            # Player Move Selection Section
            player1_choosing = True
            while player1_choosing:
                player_1_input = input("What will you do? ")
                if player_1_input == "1":
                    priority_list[2] = player1.reload()
                    player1_choosing = False
                elif player_1_input == "2":
                    if player1.get_bullet_count() <= 0:
                        print("You don't have enough bullets! Choose something else.")
                        continue
                    else:
                        priority_list[2] = player1.shoot()
                        player1_choosing = False
                elif player_1_input == "3":
                    if player1.get_block_count() <= 0:
                        print("You have 0 blocks. Choose something else.")
                        continue
                    else:
                        priority_list[2] = player1.block()
                        player1_choosing = False
                elif player_1_input == "4":
                    if player1.get_bullet_count() <= 0:
                        print("You don't have enough bullets! Choose something else.")
                        continue
                    else:
                        priority_list[2] = player1.reflect()
                        player1_choosing = False
                else:
                    print("Invalid choice. Please choose again.")
                    print()

            # Opponent Move Selection Section
            if priority_list[3] == "":
                player_2_input = "1"
            # Here is the logic behind the "AI" moves
            else:
                if player1.get_bullet_count() == 0 and player2.get_bullet_count() == 0:
                    player_2_input = "1"
                elif player2.get_bullet_count() == 0 and player2.get_block_count() != 0:
                    player_2_input = choice(["1", "1", "1", "3", "3"])
                elif player2.get_bullet_count() != 0 and player2.get_block_count() == 0:
                    player_2_input = choice(["1", "1", "2", "2", "2", "2", "2", "4"])
                elif player2.get_bullet_count() != 0 and player2.get_block_count() != 0:
                    player_2_input = choice(
                        ["1", "1", "1", "1", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "3", "3", "3", "4"])
                else:
                    player_2_input = "1"

            if player_2_input == "1":
                priority_list[3] = player2.reload()
            elif player_2_input == "2":
                priority_list[3] = player2.shoot()
            elif player_2_input == "3":
                priority_list[3] = player2.block()
            elif player_2_input == "4":
                priority_list[3] = player2.reflect()
            else:
                print("ERROR IN AI OPPONENT PROGRAM!")
                break

            # Simple line to print action
            print()
            print(f"You chose to {priority_list[2]}, your opponent chose to {priority_list[3]}!")
            print()

            p1_move = priority_list[2]
            p2_move = priority_list[3]
            # Interactions based on indexes 2 and 3
            if p1_move == "shoot" and p2_move == "block":
                print("Your bullet was blocked!")
            elif p1_move == "shoot" and p2_move == "reflect":
                print("Your bullet was reflected!")
                player1.die()
            elif p2_move == "shoot" and p1_move == "block":
                print("You blocked their bullet!")
            elif p2_move == "shoot" and p1_move == "reflect":
                print("You reflected their bullet!")
                player2.die()
            elif p1_move == "shoot" and p2_move == "shoot":
                print("You both shot each other!")
                player1.die()
                player2.die()
            elif p1_move == "shoot":
                print("Your bullet hit them!")
                player2.die()
            elif p2_move == "shoot":
                print("You were shot!")
                player1.die()
            else:
                pass
            input("Press Enter.")
            print("\n\n\n\n\n\n\n\n")

        # Samurai vs Stock
        elif player1.get_name() == "Samurai" and player2.get_name() == "Stock":
            priority_list[4] = player1.get_is_alive()
            priority_list[5] = player2.get_is_alive()
            if not (priority_list[4] and priority_list[5]):
                break
            print("Your Moveset:")
            print("---------------")
            player1.get_moveset()
            print(f"{f"Your Blade: {player1.get_unsheathed()}": <20}"
                  f"{f"Your Opponent's Bullets: {player2.get_bullet_count()}": >53}"
                  )
            print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
                  f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
            print()

            # Player Move Selection Section
            player1_choosing = True
            while player1_choosing:
                player_1_input = input("What will you do? ")
                if player_1_input == "1":
                    priority_list[2] = player1.unsheathe()
                    player1_choosing = False
                elif player_1_input == "2":
                    if player1.get_unsheathed() == "Sheathed":
                        print("You sword is not unsheathed! Choose something else.")
                        continue
                    else:
                        priority_list[2] = player1.slash()
                        player1_choosing = False
                elif player_1_input == "3":
                    if player1.get_block_count() <= 0:
                        print("You have 0 blocks. Choose something else.")
                        continue
                    else:
                        priority_list[2] = player1.block()
                        player1_choosing = False
                else:
                    print("Invalid choice. Please choose again.")
                    print()

            # Opponent Move Selection Section
            if priority_list[3] == "":
                player_2_input = "1"
            # Logic behind the "AI" moves
            else:
                if player1.get_unsheathed() == "Sheathed":
                    if player2.get_bullet_count() == 0:
                        player_2_input = "1"
                    elif player2.get_bullet_count() != 0:
                        player_2_input = choice(["2", "2", "2", "1"])
                elif player1.get_unsheathed() == "Unsheathed":
                    if player2.get_bullet_count() == 0 and player2.get_block_count() != 0:
                        player_2_input = choice(["1", "3", "3"])
                    elif player2.get_bullet_count() != 0 and player2.get_block_count() == 0:
                        player_2_input = "2"
                    elif player2.get_bullet_count() != 0 and player2.get_block_count() != 0:
                        player_2_input = choice(
                            ["1", "2", "2", "2", "2", "2", "3", "3", "3", "3", "3", "3", "3", "3"])
                else:
                    player_2_input = "1"

            if player_2_input == "1":
                priority_list[3] = player2.reload()
            elif player_2_input == "2":
                priority_list[3] = player2.shoot()
            elif player_2_input == "3":
                priority_list[3] = player2.block()
            elif player_2_input == "4":
                priority_list[3] = player2.reflect()
            else:
                print("ERROR IN AI OPPONENT PROGRAM!")
                break

            # Simple line to print action
            print()
            print(f"You chose to {priority_list[2]}, your opponent chose to {priority_list[3]}!")
            print()

            p1_move = priority_list[2]
            p2_move = priority_list[3]
            # Interactions based on indexes 2 and 3
            if p1_move == "slash" and p2_move == "shoot":
                print("You cut through your opponent's bullet! You killed them!")
                player2.die()
            elif p1_move == "slash" and p2_move == "block":
                print("Your opponent blocked, shattering your katana!")
                player1.shatter()
            elif p1_move == "block" and p2_move == "shoot":
                print("You blocked their bullet!")
            elif p2_move == "shoot":
                print("You were shot!")
                player1.die()
            elif p1_move == "slash":
                print("The enemy was sliced in half!")
                player2.die()
            else:
                pass
            input("Press Enter.")
            print("\n\n\n\n\n\n\n\n")

    print()
    if not (priority_list[4] or priority_list[5]):
        print("Draw. Noone wins.")
        print("\n\n\n\n\n\n\n\n")
        return "Draw"
    elif not priority_list[4]:
        print("You lose! GG!")
        print("\n\n\n\n\n\n\n\n")
        return "P2 Win"
    elif not priority_list[5]:
        print("You won the duel!")
        print("\n\n\n\n\n\n\n\n")
        return "P1 Win"
    else:
        pass


if __name__ == "__main__":
    battle_action(p1, p2)
