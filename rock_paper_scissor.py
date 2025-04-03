import random

jokenpo = ['Rock', 'Paper', 'Scissor']

choice = int(input('Choice between 1 - rock, 2 - paper, 3 - scissor: '))

random_jokenpo = random.randint(0, 2)

if 1 <= choice <= 3:
    choice -= 1
    random_jokenpo = random.randint(0, 2)

    print(f"\nYou chose: {jokenpo[choice]}")
    print(f"Computer chose: {jokenpo[random_jokenpo]}\n")

    if choice == random_jokenpo:
        print("Draw")
    elif (choice == 0 and random_jokenpo == 2) or (choice == 1 and random_jokenpo == 0) or (choice == 2 and random_jokenpo == 1):
        print("You win")
    else:
        print("You lose")
else:
    print("Invalid choice! Please enter 1, 2, or 3.")

