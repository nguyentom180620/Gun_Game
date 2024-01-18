# Samurai logic file
from random import choice
from character_list import Stock


# For samurai vs stock moveset
def print_samurai_v_stock_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Blade: {player1.get_unsheathed()}": <20}"
          f"{f"Your Opponent's Bullets: {player2.get_bullet_count()}": >53}"
          )
    print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
          f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
    print()


# For samurai vs samurai moveset
def print_samurai_v_samurai_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Blade: {player1.get_unsheathed()}": <20}"
          f"{f"Your Opponent's Blade: {player2.get_unsheathed()}": >50}"
          )
    print(f"{f"Your Current Number of Blocks: {player1.get_block_count()}": <20}"
          f"{f"Your Opponent's Blocks: {player2.get_block_count()}": >40}")
    print()


# For samurai vs sniper moveset
def print_samurai_v_sniper_moveset(player1, player2):
    print("Your Moveset:")
    print("---------------")
    player1.get_moveset()
    print(f"{f"Your Blade: {player1.get_unsheathed()}": <20}"
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


# For player 1 choice when player 1 is Samurai
def player_1_samurai_choice(player1, prio_list, player2=Stock()):
    player1_choosing = True
    while player1_choosing:
        player_1_input = input("What will you do? ")
        if player_1_input == "1":
            prio_list[2] = player1.unsheathe()
            player1_choosing = False
        elif player_1_input == "2":
            if player1.get_unsheathed() == "Sheathed":
                print("You sword is not unsheathed! Choose something else.")
                continue
            else:
                if player2.get_name() == "Sniper" and player2.position > player1.position:
                    player1.position += 1
                prio_list[2] = player1.slash()
                player1_choosing = False
        elif player_1_input == "3":
            if player1.get_block_count() <= 0:
                print("You have 0 blocks. Choose something else.")
                continue
            else:
                prio_list[2] = player1.block()
                player1_choosing = False
        else:
            print("Invalid choice. Please choose again.")
            print()


# Player 2 Samurai vs Player 1 Stock AI
def player_2_stock_vs_samurai_ai(player2, prio_list, player1):
    if prio_list[3] == "":
        player_2_input = "1"
    # Here is the logic behind the "AI" moves
    else:
        if player2.get_unsheathed() == "Unsheathed":
            if player1.get_block_count() != 0 and player1.get_bullet_count() != 0:
                player_2_input = choice(["1", "2", "2", "3"])
            elif player1.get_block_count() == 0:
                player_2_input = "2"
            else:
                player_2_input = choice(["1", "2"])
        elif player2.get_unsheathed() == "Sheathed":
            if player1.get_bullet_count() == 0:
                player_2_input = "1"
            elif player2.get_block_count() == 0:
                player_2_input = "1"
            else:
                player_2_input = choice(["1", "3", "3", "3"])
        else:
            player_2_input = "1"

    if player_2_input == "1":
        prio_list[3] = player2.unsheathe()
    elif player_2_input == "2":
        prio_list[3] = player2.slash()
    elif player_2_input == "3":
        prio_list[3] = player2.block()
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Player 2 Samurai vs Player 1 Samurai AI
def player_2_samurai_vs_samurai_ai(player2, prio_list, player1):
    if prio_list[3] == "":
        player_2_input = "1"
    # Here is the logic behind the "AI" moves
    else:
        if player2.get_unsheathed() == "Sheathed":
            if player2.get_block_count() == 0:
                player_2_input = "1"
            else:
                player_2_input = choice(["1", "3"])
        elif player2.get_unsheathed() == "Unsheathed":
            if player2.get_block_count() == 0:
                if player1.get_block_count() != 0 and player1.get_unsheathed() == "Unsheathed":
                    player_2_input = choice(["1", "2", "2", "2"])
                elif player1.get_block_count() == 0 and player1.get_unsheathed() == "Unsheathed":
                    player_2_input = "2"
                else:
                    player_2_input = "2"
            elif player1.get_block_count() != 0 and player1.get_unsheathed() == "Unsheathed":
                player_2_input = choice(["1", "2", "2", "2", "3"])
            elif player1.get_block_count() == 0 and player1.get_unsheathed() == "Unsheathed":
                player_2_input = choice(["2", "2", "3", "3"])
            else:
                player_2_input = choice(["2", "2", "3"])
        else:
            player_2_input = "1"

    if player_2_input == "1":
        prio_list[3] = player2.unsheathe()
    elif player_2_input == "2":
        prio_list[3] = player2.slash()
    elif player_2_input == "3":
        prio_list[3] = player2.block()
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Player 2 Samurai vs Player 1 Sniper AI
def player_2_sniper_vs_samurai_ai(player2, prio_list, player1):
    if prio_list[3] == "":
        player_2_input = "1"
    else:
        if player1.get_block_count() == 0:
            if player1.get_aiming_status() == "Yes" and player1.get_bullet_count() != 0:
                if player2.get_unsheathed() == "Sheathed" and player2.get_block_count() != 0:
                    player_2_input = choice(["1", "3"])
                elif player2.get_unsheathed() == "Sheathed" and player2.get_block_count() == 0:
                    player_2_input = "1"
                else:
                    player_2_input = choice(["1", "2", "2", "3"])
            else:
                if player2.get_unsheathed() == "Sheathed":
                    player_2_input = "1"
                else:
                    player_2_input = "2"
        elif player1.get_aiming_status() == "Yes" and player1.get_bullet_count() != 0:
            if player2.get_unsheathed() == "Sheathed" and player2.get_block_count() != 0:
                player_2_input = choice(["1", "3"])
            elif player2.get_unsheathed() == "Sheathed" and player2.get_block_count() == 0:
                player_2_input = "1"
            else:
                player_2_input = choice(["1", "2", "3", "3", "3", "3"])
        else:
            if player2.get_unsheathed() == "Sheathed":
                player_2_input = "1"
            else:
                player_2_input = choice(["2", "2", "2", "1"])

    if player_2_input == "1":
        prio_list[3] = player2.unsheathe()
    elif player_2_input == "2":
        prio_list[3] = player2.slash()
        # melee attacks get samurai closer to the sniper
        if player1.position < player2.position:
            player2.position -= 1
    elif player_2_input == "3":
        prio_list[3] = player2.block()
    else:
        print("ERROR IN AI OPPONENT PROGRAM!")


# Samurai vs Stock Interactions
def samurai_vs_stock_interactions(p1_move, p2_move, player1, player2):
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


# Samurai vs Samurai Interactions
def samurai_vs_samurai_interactions(p1_move, p2_move, player1, player2):
    if p1_move == "slash" and p2_move == "slash":
        print("Your blades clashed with intense ferocity!")
    elif p1_move == "slash" and p2_move == "block":
        print("Your opponent blocked, shattering your katana!")
        player1.shatter()
    elif p1_move == "block" and p2_move == "slash":
        print("You blocked, shattering your opponent's katana!")
        player2.shatter()
    elif p1_move == "slash":
        print("You sliced through your opponent!")
        player2.die()
    elif p2_move == "slash":
        print("You were sliced in half!")
        player1.die()
    else:
        pass


def samurai_vs_sniper_interactions(p1_move, p2_move, player1, player2):
    if player2.get_position() - player1.get_position() >= 4:
        if p2_move == "shoot" and p1_move == "block":
            print("You blocked their bullet!")
        elif p2_move == "shoot" and p1_move == "slash":
            print("You tried to slash, but they sniped you!")
            player1.die()
        elif p2_move == "shoot":
            print("You were sniped!")
            player1.die()
        else:
            pass
    elif p2_move == "shoot" and p1_move == "block":
        print("You blocked their bullet!")
    elif p2_move == "shoot" and p1_move == "slash":
        print("You tried to slash, but they sniped you!")
        player1.die()
    elif p1_move == "slash" and p2_move == "block":
        print("Your opponent blocked, shattering your katana!")
        player1.shatter()
    elif p2_move == "shoot":
        print("You were sniped!")
        player1.die()
    elif p1_move == "slash" and player2.get_position() - player1.get_position() > 0:
        print("Samurai dashed forward!")
    elif p1_move == "slash":
        print("You sliced through your opponent!")
        player2.die()
    else:
        pass
