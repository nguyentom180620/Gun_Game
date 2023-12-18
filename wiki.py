# Contains the wiki of the game!


def wiki():
    wiki_running = True
    while wiki_running:
        print("Game Wiki")
        print("-------------")
        print("1. Characters")
        print("2. How to Play")
        print("0. Exit")
        print()
        wiki_input = input("What would you like to know? ")
        print()
        if wiki_input == "0":
            wiki_running = False
        elif wiki_input == "2":
            print('''Welcome to Gun Game!
This is a game based on Rock-Paper-Scissors, except now players have a unique skillset!
Each character in the game uses their own moves, and each have their own systems to manage, but
Use your skills to beat your opponent!

The game itself should explain itself fairly easily, so make sure to read everything on the screen.
To learn about each character, how about checking out the Characters section in the wiki!''')
            print()
        elif wiki_input != "1":
            print("Invalid choice. Please try again.")
        else:
            character_running = True
            while character_running:
                print("Characters")
                print("-----------")
                print("1. Stock")
                print("2. Samurai")
                print("0. Exit")
                print()
                chara_input = input("Who would you like to look into? ")
                print()
                if chara_input == "0":
                    character_running = False
                elif chara_input == "1":
                    print('''Stock:
The first ever character introduced in the game, stock wields a pistol!

This means that managing stock means managing the basics of the game, where
stock has to manage their 5 blocks along with reloading bullets, shooting bullets,
and finally using their signature move, reflect.

Reflect is a move that uses 1 bullet to make a bullet mirror, meaning if the enemy
shoots you when you use reflect, their bullet will fly back and kill them instead!

Mastering stock is mastering Gun Game.''')
                    print()
                elif chara_input == "2":
                    print('''Samurai:
Having almost completely disappearing in 1868 with the end of the Edo period, the
Samurai is now back with their katana to fight for their honor!

Samurai will start with their sword sheathed, so make sure to pull it out before
starting a fight! Then, balancing offense and defense, balance your 5 blocks and
your katana\'s slash to defeat your enemy!

The katana is a melee weapon that when a bullet is shot towards Samurai while
slashing, the katana will cut through the bullet, giving Samurai an edge vs ranged
matchups! However, if the opponent uses block, the katana will shatter, meaning
the Samurai will need to take their sword out of their sheathe again. Don't worry,
because the blade will instantly regenerate into the sheathe once it is broken!

\"Everyone feels fear. What a samurai is, is what you do when you feel fear.\" - Enson Inoue''')
                    print()
                else:
                    print("Invalid choice, please try again.")
                    print()


if __name__ == "__main__":
    wiki()
