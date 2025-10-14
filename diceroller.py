import random

print("Virtual Dice Roller")

while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == "yes":
        number = random.randint(1, 6)
        print(f"You rolled a {number}.")
    elif roll == "no":
        print("Goodbye.")
        break
    else:
        print("Please type 'yes' or 'no'.")
