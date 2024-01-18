# Sniper logic file
from random import choice
from character_list import *

p1 = Sniper()
p2 = Sniper(position=1)


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


# For Sniper vs Samurai moveset
def print_sniper_v_samurai_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Current Bullets: {player1.get_bullet_count()}": <20}"
          f"{f"Your Opponent's Blade: {player2.get_unsheathed()}": >50}"
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


# For Sniper vs Sniper moveset
def print_sniper_v_sniper_moveset(player1, player2):
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
    print(f"{f"Your Grapple Hook: {player1.get_grapple_status()}"}"
          f"{f"Your Opponent's Grapple Hook: {player2.get_grapple_status()}": >58}")
    print(f"{f"Scoped?: {player1.get_aiming_status()}"}"
          f"{f"Opponent Scoped?: {player2.get_aiming_status()}": >56}")
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


# Player 2 Sniper vs Player 1 Sniper AI
def player_2_sniper_vs_sniper_ai(player2, prio_list, player1):
    if prio_list[3] == "":
        player_2_input = choice(["1", "2"])
    else:
        if player1.get_aiming_status() == "Yes" and player1.get_bullet_count() != 0:
            if player2.get_aiming_status() == "Yes" and player2.get_bullet_count() != 0:
                player_2_input = choice(["3", "5"])
            else:
                player_2_input = choice(["2", "5"])
        else:
            if player2.get_bullet_count() == 0:
                player_2_input = "1"
            elif player2.get_aiming_status() == "No":
                player_2_input = "2"
            elif player2.get_aiming_status() == "Yes":
                if player1.get_block_count() != 0:
                    player_2_input = choice(["2", "3"])
                else:
                    player_2_input = "3"
            else:
                player_2_input = "1"

    if player_2_input == "1":
        prio_list[3] = player2.reload()
        player2.aiming = False
    elif player_2_input == "2":
        prio_list[3] = player2.aim()
    elif player_2_input == "3":
        prio_list[3] = player2.shoot()
    elif player_2_input == "4":
        prio_list[3] = player2.grapple_away()
        player2.aiming = False
    elif player_2_input == "5":
        prio_list[3] = player2.block()
        player2.aiming = False
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Player 2 Sniper vs Player 1 Stock AI
def player_2_stock_vs_sniper_ai(player2, prio_list, player1):
    if prio_list[3] == "":
        player_2_input = "4"
    else:
        if player2.get_position() - player1.get_position() >= 4:
            if player2.get_aiming_status() == "No":
                player_2_input = "2"
            elif player2.get_bullet_count() == 0:
                player_2_input = "1"
            else:
                if player1.get_bullet_count() == 0:
                    player_2_input = choice(["2", "3", "3"])
                elif player2.get_bullet_count() > player1.get_block_count():
                    if player1.get_bullet_count() == 0:
                        player_2_input = "3"
                    else:
                        player_2_input = choice(["2", "2", "3"])
                else:
                    player_2_input = choice(["2", "2", "3"])
        elif player1.get_bullet_count() != 0:
            if player2.get_grapple_status() == "Loaded" and player2.get_position() - player1.get_position() == 3:
                player_2_input = "4"
            elif player2.get_block_count() == 0:
                if player2.get_grapple_status() == "Unloaded":
                    player_2_input = "1"
                else:
                    player_2_input = "4"
            elif player2.get_grapple_status() == "Unloaded":
                player_2_input = choice(["1", "5"])
            else:
                player_2_input = choice(["4", "5"])
        else:
            if player2.get_grapple_status() == "Unloaded":
                player_2_input = "1"
            else:
                player_2_input = "4"

    if player_2_input == "1":
        prio_list[3] = player2.reload()
        player2.aiming = False
    elif player_2_input == "2":
        prio_list[3] = player2.aim()
    elif player_2_input == "3":
        prio_list[3] = player2.shoot()
    elif player_2_input == "4":
        prio_list[3] = player2.grapple_away()
        player2.aiming = False
    elif player_2_input == "5":
        prio_list[3] = player2.block()
        player2.aiming = False
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Player 2 Sniper vs Player 1 Stock AI
def player_2_samurai_vs_sniper_ai(player2, prio_list, player1):
    # TODO Make this AI by considering how sniper should play against samurai, then do wiki, then work on GUI
    if prio_list[3] == "":
        player_2_input = "4"
    else:
        if player1.get_block_count() == 0 and player2.get_aiming_status() == "Yes" and player2.get_bullet_count() != 0:
            player_2_input = "3"
        if player2.get_position() - player1.get_position() >= 2:
            if player2.get_aiming_status() == "No":
                player_2_input = "2"
            elif player2.get_bullet_count() == 0:
                player_2_input = "1"
            else:
                if player1.get_unsheathed() == "Sheathed":
                    player_2_input = choice(["2", "3", "3"])
                elif player2.get_bullet_count() > player1.get_block_count():
                    player_2_input = "3"
                else:
                    player_2_input = choice(["2", "3"])
        else:
            if player1.get_unsheathed() == "Sheathed":
                if player2.get_grapple_status() == "Loaded" and player2.get_position() - player1.get_position() >= 1:
                    player_2_input = "4"
                elif player2.get_bullet_count() > 0 and player2.get_aiming_status() == "Yes":
                    player_2_input = choice(["2", "3"])
                elif player2.get_bullet_count() > 0 and player2.get_aiming_status() == "No":
                    player_2_input = "2"
                else:
                    player_2_input = "1"
            elif player1.get_unsheathed() == "Unsheathed":
                if player2.get_grapple_status() == "Loaded" and player2.get_position() - player1.get_position() >= 1:
                    player_2_input = "4"
                elif player2.get_bullet_count() > 0 and player2.get_aiming_status() == "Yes":
                    player_2_input = choice(["2", "3"])
                elif player2.get_block_count() == 0:
                    if player2.get_bullet_count() > 0 and player2.get_aiming_status() == "No":
                        player_2_input = "2"
                    elif player2.get_bullet_count() == 0:
                        player_2_input = "1"
                    else:
                        player_2_input = "3"
                elif player2.get_bullet_count() > 0 and player2.get_aiming_status() == "No":
                    player_2_input = choice(["2", "5", "5", "5", "5", "5"])
                else:
                    player_2_input = choice(["1", "5", "5", "5", "5", "5"])
            else:
                pass

    if player_2_input == "1":
        prio_list[3] = player2.reload()
        player2.aiming = False
    elif player_2_input == "2":
        prio_list[3] = player2.aim()
    elif player_2_input == "3":
        prio_list[3] = player2.shoot()
    elif player_2_input == "4":
        prio_list[3] = player2.grapple_away()
        player2.aiming = False
    elif player_2_input == "5":
        prio_list[3] = player2.block()
        player2.aiming = False
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


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


# Sniper vs Samurai Interactions
def sniper_vs_samurai_interactions(p1_move, p2_move, player1, player2):
    if player2.get_position() - player1.get_position() >= 4:
        if p1_move == "shoot" and p2_move == "block":
            print("Your bullet was blocked!")
        elif p1_move == "shoot" and p2_move == "slash":
            print("They tried to slash, but you sniped them!")
            player2.die()
        elif p1_move == "shoot":
            print("You sniped them!")
            player2.die()
        else:
            pass
    elif p1_move == "shoot" and p2_move == "block":
        print("Your bullet was blocked!")
    elif p1_move == "shoot" and p2_move == "slash":
        print("They tried to slash, but you sniped them!")
        player2.die()
    elif p2_move == "slash" and p1_move == "block":
        print("You blocked, shattering your opponent's katana!")
        player2.shatter()
    elif p1_move == "shoot":
        print("You sniped them!")
        player2.die()
    elif p2_move == "slash" and player2.get_position() - player1.get_position() > 0:
        print("Samurai dashed forward!")
    elif p2_move == "slash":
        print("You were sliced in half!")
        player1.die()
    else:
        pass


# Sniper vs Sniper Interactions
def sniper_vs_sniper_interactions(p1_move, p2_move, player1, player2):
    if p1_move == "shoot" and p2_move == "block":
        print("Your bullet was blocked!")
    elif p2_move == "shoot" and p1_move == "block":
        print("You blocked their bullet!")
    elif p1_move == "shoot" and p2_move == "shoot":
        print("You both sniped each other!")
        player1.die()
        player2.die()
    elif p1_move == "shoot":
        print("You sniped them!")
        player2.die()
    elif p2_move == "shoot":
        print("You were sniped!")
        player1.die()
    else:
        pass


if __name__ == "__main__":
    print_sniper_v_sniper_moveset(p1, p2)
