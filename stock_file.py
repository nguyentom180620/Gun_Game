# This contains the functions for stock vs stock that build up Battle_Action, making that file easier to read
from random import choice


# For stock vs stock moveset print
def print_stock_v_stock_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Current Bullets: {player1.get_bullet_count()}": <20}"
          f"{f"Your Opponent's Bullets: {player2.get_bullet_count()}": >50}"
          )
    print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
          f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
    print()


# For stock vs samurai moveset print
def print_stock_v_samurai_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Current Bullets: {player1.get_bullet_count()}": <20}"
          f"{f"Your Opponent's Blade: {player2.get_unsheathed()}": >50}"
          )
    print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
          f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
    print()


# For stock vs sniper moveset print
def print_stock_v_sniper_moveset(player1, player2):
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
    print(f"Your Opponent's Grapple Hook: {player2.get_grapple_status()}")
    print(f"Opponent Scoped?: {player2.get_aiming_status()}")
    print(f"Distance from You: {player2.get_position() - player1.get_position()} units")
    if player2.get_position() - player1.get_position() >= 4: print(f"(Sniping Range!)")
    print()


# For player 1 choice when player 1 is Stock
def player_1_stock_choice(player1, prio_list):
    player1_choosing = True
    while player1_choosing:
        player_1_input = input("What will you do? ")
        if player_1_input == "1":
            prio_list[2] = player1.reload()
            player1_choosing = False
        elif player_1_input == "2":
            if player1.get_bullet_count() <= 0:
                print("You don't have enough bullets! Choose something else.")
                continue
            else:
                prio_list[2] = player1.shoot()
                player1_choosing = False
        elif player_1_input == "3":
            if player1.get_block_count() <= 0:
                print("You have 0 blocks. Choose something else.")
                continue
            else:
                prio_list[2] = player1.block()
                player1_choosing = False
        elif player_1_input == "4":
            if player1.get_bullet_count() <= 0:
                print("You don't have enough bullets! Choose something else.")
                continue
            else:
                prio_list[2] = player1.reflect()
                player1_choosing = False
        else:
            print("Invalid choice. Please choose again.")
            print()


# Player 2 Stock vs Player 1 Stock AI
def player_2_stock_vs_stock_ai(player2, prio_list, player1):
    if prio_list[3] == "":
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
        prio_list[3] = player2.reload()
    elif player_2_input == "2":
        prio_list[3] = player2.shoot()
    elif player_2_input == "3":
        prio_list[3] = player2.block()
    elif player_2_input == "4":
        prio_list[3] = player2.reflect()
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Player 2 Stock vs Player 1 Samurai AI
def player_2_samurai_vs_stock_ai(player2, prio_list, player1):
    if prio_list[3] == "":
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
        else:
            player_2_input = "1"

    if player_2_input == "1":
        prio_list[3] = player2.reload()
    elif player_2_input == "2":
        prio_list[3] = player2.shoot()
    elif player_2_input == "3":
        prio_list[3] = player2.block()
    elif player_2_input == "4":
        prio_list[3] = player2.reflect()
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Player 2 Stock vs Player 1 Sniper AI
def player_2_sniper_vs_stock_ai(player2, prio_list, player1):
    if prio_list[3] == "":
        player_2_input = "1"
    else:
        if player1.get_block_count() == 0:
            if player1.get_aiming_status() == "Yes" and player1.get_bullet_count() != 0:
                if player2.get_bullet_count() == 0 and player2.get_block_count() != 0:
                    player_2_input = choice(["1", "3"])
                elif player2.get_bullet_count() == 0 and player2.get_block_count() == 0:
                    player_2_input = "1"
                else:
                    player_2_input = choice(["1", "2", "2", "4"])
            else:
                if player2.get_bullet_count() == 0:
                    player_2_input = "1"
                else:
                    player_2_input = "2"
        elif player1.get_aiming_status() == "Yes" and player1.get_bullet_count() != 0:
            if player2.get_bullet_count() == 0 and player2.get_block_count() != 0:
                player_2_input = choice(["1", "3"])
            elif player2.get_bullet_count() == 0 and player2.get_block_count() == 0:
                player_2_input = "1"
            else:
                player_2_input = choice(["1", "2", "3", "4"])
        else:
            if player2.get_bullet_count() == 0:
                player_2_input = "1"
            else:
                player_2_input = choice(["2", "2", "2", "1"])

    if player_2_input == "1":
        prio_list[3] = player2.reload()
    elif player_2_input == "2":
        prio_list[3] = player2.shoot()
    elif player_2_input == "3":
        prio_list[3] = player2.block()
    elif player_2_input == "4":
        prio_list[3] = player2.reflect()
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Stock vs Stock Interactions
def stock_vs_stock_interactions(p1_move, p2_move, player1, player2):
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


# Stock vs Samurai Interactions
def stock_vs_samurai_interactions(p1_move, p2_move, player1, player2):
    if p2_move == "slash" and p1_move == "shoot":
        print("Your bullet was cut! You were sliced!")
        player1.die()
    elif p2_move == "slash" and p1_move == "block":
        print("You blocked, shattering your opponent's katana!")
        player2.shatter()
    elif p2_move == "block" and p1_move == "shoot":
        print("Your bullet was blocked!")
    elif p1_move == "shoot":
        print("You shot your opponent!")
        player2.die()
    elif p2_move == "slash":
        print("You were sliced in half!")
        player1.die()
    else:
        pass


# Stock vs Sniper Interactions
def stock_vs_sniper_interactions(p1_move, p2_move, player1, player2):
    if player2.get_position() - player1.get_position() >= 4:
        if p2_move == "shoot" and p1_move == "block":
            print("You blocked their bullet!")
        elif p2_move == "shoot" and p1_move == "reflect":
            print("You reflected their bullet!")
            player2.die()
        elif p2_move == "shoot":
            print("You were sniped!")
            player1.die()
        elif p1_move == "shoot":
            print("You tried to shoot, but they were too far away!")
        else:
            pass
    elif p1_move == "shoot" and p2_move == "block":
        print("Your bullet was blocked!")
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
        print("You shot them!")
        player2.die()
    elif p2_move == "shoot":
        print("You were shot!")
        player1.die()
    else:
        pass
