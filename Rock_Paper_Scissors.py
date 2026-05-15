import random
inputs = {1: "✊", 2: "✋", 3: "✌️"}

print("=========================")
print("ROCK PAPER SCISSORS")    
print("=========================")

print("\n1 is for  ✊")
print("\n2 is for ✋")
print("\n3 is for ✌️")

guess = int(input("Pick a number : "))

a = random.randint(1, 3)

print(f"You chose: {inputs[guess]}")
print(f"CPU chose:  {inputs[a]}")

if guess == 1 and a == 1:
    print("Tie")
elif guess == 1 and a == 2:
    print("CPU won")
elif guess == 1 and a == 3:
    print("You won")

elif guess == 2 and a == 1:
    print("You won")
elif guess == 2 and a == 2:
    print("Tie")
elif guess == 2 and a == 3:
    print("CPU won")

elif guess == 3 and a == 1:
    print("CPU won")
elif guess == 3 and a == 2:
    print("You won")
elif guess == 3 and a == 3:
    print("Tie")

else:
    print("Please select a number between 1 and 3")
