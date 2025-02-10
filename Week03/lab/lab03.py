import random

# dice options using list() and range()
diceOptions = list(range(1, 7))

# weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    combatStrength = 1  # Default value for invalid input

# input combat strength for monster
mCombatStrength = int(input("Enter monster's combat strength (1-6)"))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input! Monster combat strength should be between 1 and 6.")
    mCombatStrength = 1  # Default value for invalid input

# simulate Battle rounds
for j in range(1, 21, 2):  # Simulation of 20 reloads, stepping by 2
    # Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # calculate the weapons
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll

    # print round details
    print(f"\nRound {j} Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}")
    print(f"Hero total strength: {heroRoll}, Monster total strength: {monsterTotal}")

    # determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round")
    else:
        print("It's a tie!")

    if j == 11:
        print("\n Battle Truce declared in Round 11. Game Over!")
        break
if j != 11:
    print("\n Battle concluded after 20 rounds!")