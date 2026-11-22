print("------Vice Heart------")

try:
    with open("Save.txt", "r") as file:
        money = int(file.read())
        print("Old Save Loaded! Money:", money)
except:
    money = 5000
    print("New Game Started! Money:", money)

health = 100

print("Screen Loading")
print("------Main Menu------")
print("Start Game")
print("Setting")
print("Exit")

choice = input("What do you want: ")
if choice.lower() == "start game":
    print("Game Started Please Wait")
elif choice.lower() == "setting":
    print("Setting Is Open")
elif choice.lower() == "exit":
    print("Game Exit")
else:
    print("Invalid")

print("For Earn Money")
print("1. Go To Rob The Bank")
print("2. Do A Job")
print("3. Rob Peoples Money")

choice = int(input("What do you want (1-3): "))

if choice == 1:
    print("Mission Activated")
    print("Money Before Rob:", money)
    print("Change Getup And Cover Your Face")
    print("Rob Bank")
    money = money + 6000
    print("Money After Rob:", money)
    star = 3
    print("Police Is Chasing You, Stars:", star)
    print("Run With Car")
    print("Police Attacked You")
    health = health - 10
    print("Health:", health)
    print("You Lost Cops")
    if star == 0:
        print("You Are Safe")

elif choice == 2:
    print("Job Mission Activated")
    print("You Are Now A Taxi Driver")
    print("Money Before Job:", money)
    print("Picking Up Passenger...")
    print("Dropping Passenger At Location...")
    money = money + 1500
    print("You Earned 1500!")
    print("Money After Job:", money)
    print("Health:", health)
    print("Good Job! Honest Money!")

elif choice == 3:
    print("Rob People Mission Activated")
    print("Money Before Rob:", money)
    print("Walking On Street...")
    print("Found A Rich Man With Wallet")
    print("You Robbed Him!")
    money = money + 2000
    print("You Got 2000!")
    print("Money After Rob:", money)
    star = 2
    print("Police Is Chasing You, Stars:", star)
    print("Police Attacked You")
    health = health - 20
    print("Health:", health)
    print("You Escaped!")

else:
    print("Invalid Mission")

print("Go To Hospital For Health (500$): ")
hospital = input("Do you want to go to hospital? (yes/no): ")
if hospital == "yes":
    money = money - 500
    health = 100
    print("Health Full! Money Now:", money)

with open("Save.txt", "w") as file:
    file.write(str(money))

print("Game Saved! Money:", money)
print("Health:", health)