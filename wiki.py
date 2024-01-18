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
                print("3. Sniper")
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
                elif chara_input == "3":
                    print('''Sniper:
The cool ranged character where distance matters! Make distance to out range
other ranged characters, or control the flow of battle by aiming down your sight
onto melee characters!

The Sniper starts with their grapple and one bullet loaded. This lets you choose
to either aim or grapple first turn. The sniper has to aim before being able to
shoot, but can hold aim to bait out blocks and can continuously fire while aiming.
Doing other actions will stop aiming. The grapple increases distance between the
two characters by 1, however melee attack are like dashes and reduce distance, so
be careful managing distance. Finally, vs ranged characters, reaching a distance
of 4 units puts you out of range of their attacks, making it easy pickings to snipe!

Sniper is all about patience.''')
                    print()
                else:
                    print("Invalid choice, please try again.")
                    print()


if __name__ == "__main__":
    wiki()
