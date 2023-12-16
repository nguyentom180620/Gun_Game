# Gun Game Project
# Start Date: 12/16/2023
# By Tom Nguyen
# Check Gun_Game.docx for more info of project guidelines

def main():
    print("Welcome to Gun Game!")
    print()
    # First while loop for menu
    program_running = True
    while program_running:
        print("Gun Game Menu")
        print("-----------------")
        print("1. Start Game!")
        print("2. Character Wiki")
        print("3. Quit")
        print()
        menu_input = input("What would you like to do? ")
        print()
        if menu_input == "3":
            program_running = False
        elif menu_input == "2":
            # implement wiki class before proceeding
            pass
        elif menu_input != "1":
            print("Invalid menu choice! Please enter a valid option.")
            print()
        else:
            # implement after dealing with the rest of the classes
            pass


main()
