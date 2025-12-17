import random
computer = random.randint(1, 3);

player = int(input("Enter stone(1) scissors(2) cloth(3): "))

print("Computer chose:%d" % computer)
print("You chose:%d" % player)

if ((player == 1 and computer == 2) or
    (player == 2 and computer == 3) or
    (player == 3 and computer == 1)):
    print("You win!")
elif ((player == computer)):
    print("It's a tie!")
else:
    print("You lose!")

