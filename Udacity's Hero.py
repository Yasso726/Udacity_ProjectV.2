import random


def play_game():
    print("Welcome, Udacity Hero!")
    while True:
        print("Hackers have captured hostages and are threatening to corrupt Udacity's files.")
        print("Do you:")
        choice = input("1. Hack into the hacker's mainframe\n2. Infiltrate the hacker's hideout\n> ")

        if choice == "1":
            hack_mainframe()
        elif choice == "2":
            infiltrate_hideout()
        else:
            print("Invalid choice. You lose!")

        if input("Play again? (yes/no) ").lower() != "yes":
            break


def hack_mainframe():
    print("You try to hack into the mainframe. Do you:")
    choice = input("1. Use a brute force attack\n2. Use a stealth approach\n> ")

    if choice == "1":
        outcome = random.choice([
            "successfully bypass the security and rescue the hostages",
            "trigger an alarm and get caught by the hackers"
        ])
        print(f"You {outcome}.", "You win!" if "rescue" in outcome else "You lose!")
    elif choice == "2":
        outcome = random.choice([
            "infiltrate the system unnoticed and save the files",
            "get detected and locked out"
        ])
        print(f"You {outcome}.", "You win!" if "save the files" in outcome else "You lose!")
    else:
        print("Invalid choice. You lose!")


def infiltrate_hideout():
    print("You infiltrate the hacker's hideout. Do you:")
    choice = input("1. Take out the guards silently\n2. Create a distraction\n> ")

    if choice == "1":
        outcome = random.choice([
            "neutralize the guards and free the hostages",
            "get overpowered by the guards"
        ])
        print(f"You {outcome}.", "You win!" if "free the hostages" in outcome else "You lose!")
    elif choice == "2":
        outcome = random.choice([
            "cause chaos and rescue the hostages in the confusion",
            "get captured in the attempt"
        ])
        print(f"You {outcome}.", "You win!" if "rescue the hostages" in outcome else "You lose!")
    else:
        print("Invalid choice. You lose!")


play_game()
