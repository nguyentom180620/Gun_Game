# This contains the function in which the action of the game runs
from character_list import *
from random import choice
from stock_file import *
from samurai_file import *
from sniper_file import *

p1 = Sniper()
p2 = Stock(position=1)


def check_if_alive(prio_list, player1, player2):
    prio_list[4] = player1.get_is_alive()
    prio_list[5] = player2.get_is_alive()
    if not (prio_list[4] and prio_list[5]):
        return True
    return False


def print_action(prio_list):
    print()
    print(f"You chose to {prio_list[2]}, your opponent chose to {prio_list[3]}!")
    print()


def load_next_page():
    input("Press Enter.")
    print("\n\n\n\n\n\n\n\n")


def check_winner(prio_list):
    print()
    if not (prio_list[4] or prio_list[5]):
        print("Draw. Noone wins.")
        print("\n\n\n\n\n\n\n\n")
        return "Draw"
    elif not prio_list[4]:
        print("You lose! GG!")
        print("\n\n\n\n\n\n\n\n")
        return "P2 Win"
    elif not prio_list[5]:
        print("You won the duel!")
        print("\n\n\n\n\n\n\n\n")
        return "P1 Win"
    else:
        pass


def battle_action(player1, player2):
    battle_running = True
    # priority list will contain the strings from the classes that determine the action
    # indexes 0 and 1 are not used yet, but maybe include function in the future
    # indexes 2 and 3 are the player action
    # indexes 4 and 5 check if each player is still alive
    priority_list = ["", "", "", "", "", ""]

    while battle_running:
        match player1.get_name(), player2.get_name():

            # Stock vs Stock
            case "Stock", "Stock":
                if check_if_alive(priority_list, player1, player2):
                    break
                print_stock_v_stock_moveset(player1, player2)

                # Opponent Move Selection Section
                player_2_stock_vs_stock_ai(player2, priority_list, player1)

                # Player Move Selection Section
                player_1_stock_choice(player1, priority_list)

                # Simple line to print action
                print_action(priority_list)

                p1_move = priority_list[2]
                p2_move = priority_list[3]
                # Interactions based on indexes 2 and 3
                stock_vs_stock_interactions(p1_move, p2_move, player1, player2)
                load_next_page()

            # Samurai vs Stock
            case "Samurai", "Stock":
                if check_if_alive(priority_list, player1, player2):
                    break
                print_samurai_v_stock_moveset(player1, player2)

                # Opponent Move Selection Section
                player_2_samurai_vs_stock_ai(player2, priority_list, player1)

                # Player Move Selection Section
                player_1_samurai_choice(player1, priority_list)

                # Simple line to print action
                print_action(priority_list)

                p1_move = priority_list[2]
                p2_move = priority_list[3]
                # Interactions based on indexes 2 and 3
                samurai_vs_stock_interactions(p1_move, p2_move, player1, player2)
                load_next_page()

            # Stock vs Samurai
            case "Stock", "Samurai":
                if check_if_alive(priority_list, player1, player2):
                    break
                print_stock_v_samurai_moveset(player1, player2)

                # Opponent Move Selection Section
                player_2_stock_vs_samurai_ai(player2, priority_list, player1)

                # Player Move Selection Section
                player_1_stock_choice(player1, priority_list)

                # Simple line to print action
                print_action(priority_list)

                p1_move = priority_list[2]
                p2_move = priority_list[3]
                # Interactions based on indexes 2 and 3
                stock_vs_samurai_interactions(p1_move, p2_move, player1, player2)
                load_next_page()

            # Samurai vs Samurai
            case "Samurai", "Samurai":
                if check_if_alive(priority_list, player1, player2):
                    break
                print_samurai_v_samurai_moveset(player1, player2)

                # Opponent Move Selection Section
                player_2_samurai_vs_samurai_ai(player2, priority_list, player1)

                # Player Move Selection Section
                player_1_samurai_choice(player1, priority_list)

                # Simple line to print action
                print_action(priority_list)

                p1_move = priority_list[2]
                p2_move = priority_list[3]
                # Interactions based on indexes 2 and 3
                samurai_vs_samurai_interactions(p1_move, p2_move, player1, player2)
                load_next_page()

            # Sniper vs Stock
            case "Sniper", "Stock":
                if check_if_alive(priority_list, player1, player2):
                    break
                print_sniper_v_stock_moveset(player1, player2)

                # Opponent Move Selection Section
                player_2_sniper_vs_stock_ai(player2, priority_list, player1)

                # Player Move Selection Section
                player_1_sniper_choice(player1, priority_list)

                # Simple line to print action
                print_action(priority_list)

                p1_move = priority_list[2]
                p2_move = priority_list[3]
                # Interactions based on indexes 2 and 3
                sniper_vs_stock_interactions(p1_move, p2_move, player1, player2)
                load_next_page()

            case _:
                print("Oh no, invalid classes! Or something else went wrong :[")
    result = check_winner(priority_list)
    return result


if __name__ == "__main__":
    battle_action(p1, p2)
