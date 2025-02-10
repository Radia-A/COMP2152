# Import the functions from functions_lab05.py
from functions_lab05 import collect_loot, use_loot, inception_dream
import random

# Initialize variables (these may vary based on your setup, adjust accordingly)
belt = ""
loot_options = []
health_points = 100  # Example starting health
combat_strength = 10  # Example starting combat strength
stars_display = "☆☆☆☆☆"  # Example stars display

# Hero Name Input
hero_name = input("Enter your Hero's name (in two words): ")
while len(hero_name.split()) != 2 or not all(word.isalpha() for word in hero_name.split()):
    hero_name = input("Please enter two valid words for your Hero's name: ")
first_name, second_name = hero_name.split()
short_name = first_name[:2] + second_name[0]
print(f"Hero {short_name} gets {stars_display} stars")

# Collect Loot
belt, loot_options = collect_loot(belt, loot_options)
print(f"Belt: {belt}, Loot Options: {loot_options}")

# Use Loot
belt, health_points = use_loot(belt, health_points)
print(f"Belt: {belt}, Health Points: {health_points}")

# Roll for Attack Order
attack_roll = random.randint(1, 6)
print(f"Attack Roll: {attack_roll}")
if attack_roll in [1, 3, 5]:
    print("Hero attacks first!")
    # Add hero attack logic here
else:
    print("Monster attacks first!")
    # Add monster attack logic here

# Call inception_dream function for recursion
crazy_level = 0
crazy_level = inception_dream(crazy_level)
print(f"Inception Dream complete! Crazy Level: {crazy_level}")

# Update health and combat strength
health_points -= 1  # Reduce health after dream
combat_strength += crazy_level  # Increase combat strength based on crazy_level
print(f"After the dream, Health Points: {health_points}, Combat Strength: {combat_strength}")





