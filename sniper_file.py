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
    print(f"Currently Aiming?: {player1.get_aiming_status()}")
    print(f"Distance from Opponent: {player2.get_position() - player1.get_position()} units")
    print()


print_sniper_v_stock_moveset(p1, p2)
if __name__ == "__main__":
    print_sniper_v_stock_moveset(p1, p2)
