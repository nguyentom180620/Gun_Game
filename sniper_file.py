# Sniper logic file
from random import choice
from character_list import *

p1 = Sniper()
p2 = Stock(position=1)


# For Sniper vs Stock moveset
def print_sniper_v_stock_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Current Bullets: {player1.get_bullet_count()}": <20}"
          f"{f"Your Opponent's Bullets: {player2.get_bullet_count()}": >50}"
          )
    print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
          f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
    print()
    print("Sniper Specifics")
    print("-----------------")
    print(f"Your Grapple Hook: {player1.get_grapple_status()}")
    print(f"Scoped?: {player1.get_aiming_status()}")
    print(f"Distance from Opponent: {player2.get_position() - player1.get_position()} units")
    if player2.get_position() - player1.get_position() >= 4: print(f"(Sniping Range!)")
    print()


# For player 1 choice when player 1 is Sniper
def player_1_sniper_choice(player1, prio_list):
    player1_choosing = True
    while player1_choosing:
        player_1_input = input("What will you do? ")
        if player_1_input == "1":
            prio_list[2] = player1.reload()
            player1.aiming = False
            player1_choosing = False
        elif player_1_input == "2":
            prio_list[2] = player1.aim()
            player1_choosing = False
        elif player_1_input == "3":
            if player1.get_aiming_status() == "No" or player1.get_bullet_count() == 0:
                print(f"You failed to shoot! (Not aiming or no bullets) Choose something else.")
                continue
            else:
                prio_list[2] = player1.shoot()
                player1.aiming = False
                player1_choosing = False
        elif player_1_input == "4":
            if player1.get_grapple_status() != "Loaded":
                print(f"You failed to grapple! (not loaded) Choose something else.")
                continue
            else:
                prio_list[2] = player1.grapple_away()
                player1.aiming = False
                player1_choosing = False
        elif player_1_input == "5":
            if player1.get_block_count() <= 0:
                print("You have 0 blocks. Choose something else.")
                continue
            else:
                prio_list[2] = player1.block()
                player1.aiming = False
                player1_choosing = False
        else:
            print("Invalid choice. Please choose again.")
            print()


# Sniper vs Stock Interactions
def sniper_vs_stock_interactions(p1_move, p2_move, player1, player2):
    if player2.get_position() - player1.get_position() >= 4:
        if p1_move == "shoot" and p2_move == "block":
            print("Your bullet was blocked!")
        elif p1_move == "shoot" and p2_move == "reflect":
            print("Your bullet was reflected!")
            player1.die()
        elif p1_move == "shoot":
            print("You sniped them!")
            player2.die()
        elif p2_move == "shoot":
            print("They tried to shoot you, but you were too far!")
        else:
            pass
    elif p1_move == "shoot" and p2_move == "block":
        print("Your bullet was blocked!")
    elif p1_move == "shoot" and p2_move == "reflect":
        print("Your bullet was reflected!")
        player1.die()
    elif p2_move == "shoot" and p1_move == "block":
        print("You blocked their bullet!")
    elif p1_move == "shoot" and p2_move == "shoot":
        print("You both shot each other!")
        player1.die()
        player2.die()
    elif p1_move == "shoot":
        print("You sniped them!")
        player2.die()
    elif p2_move == "shoot":
        print("You were shot!")
        player1.die()
    else:
        pass


if __name__ == "__main__":
    print_sniper_v_stock_moveset(p1, p2)
