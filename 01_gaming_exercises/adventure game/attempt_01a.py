# Adventure attempt 1, Roy Smith IV, V0.4
# You have a lot of code to add.   You need to finish by Friday. 
# Roy, I am glad you used some outside resources for this project. 
# BUT it doesn't all work.  You need to do one of two things:  make it work or remove it. 
# You have until 2024-12-16 @ 3:00PM to resubmit any changes. 

import random
import time
import datetime
import elements
import region
import Battle
import elementalReaction
import characters

# SAVING DATA TO A FILE
# STeP 1 -- Create the file name
logFileName = "dragonrealmlog" # add .txt to the file name.  
# Example: dragonrealmlog1132AM.txt

# STEP 2 -- Create / Open the file to save the data

saveData = open(logFileName, "a")
# FILE MODES
# "X" CREATES FILE, IF FILE EXIST, EXIST WITH ERROR MESSSAGE
# "W" CREATES FILE, IF FILE EXIST, ERASE AND OVERWRITE CONTENTS
# "a" CREATES FILE, IF FILE EXIST, APPEND DATA TO THE FILE

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")



def main():
    print("Welcome to Genshin Adventure!")
    traveler_name = input("Enter your Traveler's name: ")
    traveler_element = input("Choose your element (Anemo, Geo, Electro, Pyro): ").capitalize()

    # Create the Traveler
    player = Traveler(traveler_name, traveler_element)
    print(f"You are {player.name}, a {player.element} Traveler.")
    print("Explore regions, battle enemies, and uncover treasures!")

    # Define regions
    mondstadt = Region(
        "Mondstadt", 
        enemies=["Slime", "Hilichurl", "Abyss Mage"], 
        treasures=["Apple", "Iron Chunk", "Artifact"]
    )
    liyue = Region(
        "Liyue", 
        enemies=["Treasure Hoarder", "Fatui Agent", "Geo Slime"], 
        treasures=["Jade Parcel", "Cor Lapis", "Glaze Lily"]
    )

    # Main game loop
    while True:
        print("\nWhat would you like to do?")
        action = input("Options: Explore Mondstadt, Explore Liyue, Inventory, Stats, Quit: ").strip().lower()

        if action == "explore mondstadt":
            explore_region(player, mondstadt)
        elif action == "explore liyue":
            explore_region(player, liyue)
        elif action == "inventory":
            print("Your inventory:", player.list_inventory())
        elif action == "stats":
            print(player)
        elif action == "quit":
            print("Goodbye, Traveler!")
            break
        else:
            print("Invalid option. Try again.")

def explore_region(player, region):
    result = region.explore()
    if result["type"] == "enemy":
        print(f"You encountered a {result['enemy'].name}!")
        battle(player, result["enemy"])
    elif result["type"] == "treasure":
        print(f"You found a treasure: {result['treasure']}!")
        player.add_item(result["treasure"])
    else:
        print("You found nothing this time.")

if __name__ == "__main__":
    main()


# Character


class Character:
    def __init__(self, name, health, attack, element):
        self.name = name
        self.health = health
        self.attack = attack
        self.element = element

    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0  # True if dead

    def __str__(self):
        return f"{self.name} | HP: {self.health} | ATK: {self.attack} | Element: {self.element}"

class Traveler(Character):
    def __init__(self, name, element):
        super().__init__(name, 100, 20, element)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def list_inventory(self):
        return ", ".join(self.inventory) if self.inventory else "nothing"

class Enemy(Character):
    def __init__(self, name, health, attack, element):
        super().__init__(name, health, attack, element)


# Region

import random
from characters import Enemy

class Region:
    def __init__(self, name, enemies, treasures):
        self.name = name
        self.enemies = enemies
        self.treasures = treasures

    def explore(self):
        if random.choice([True, False]):  # 50% chance to find something
            if random.choice([True, False]):  # 50% chance of enemy or treasure
                enemy_name = random.choice(self.enemies)
                enemy_element = random.choice(["Anemo", "Pyro", "Electro", "Geo"])
                return {"type": "enemy", "enemy": Enemy(enemy_name, random.randint(30, 60), random.randint(5, 15), enemy_element)}
            else:
                return {"type": "treasure", "treasure": random.choice(self.treasures)}
        return {"type": "nothing"}


# Combat

import random
from Elements import ElementalReaction

def battle(player, enemy):
    print(f"Battle Start: {player.name} vs {enemy.name} ({enemy.element})")

    while player.health > 0 and enemy.health > 0:
        action = input("Options: Attack, Heal: ").strip().lower()
        if action == "attack":
            base_damage = random.randint(player.attack - 5, player.attack + 5)
            reaction_bonus = ElementalReaction.calculate(player.element, enemy.element)
            total_damage = base_damage + reaction_bonus
            print(f"You dealt {total_damage} damage!")
            if enemy.take_damage(total_damage):
                print(f"You defeated the {enemy.name}!")
                return
        elif action == "heal":
            heal = random.randint(10, 20)
            player.health += heal
            print(f"You healed for {heal} HP.")
        else:
            print("Invalid action.")

        # Enemy's turn
        damage = random.randint(enemy.attack - 3, enemy.attack + 3)
        print(f"The {enemy.name} dealt {damage} damage!")
        if player.take_damage(damage):
            print("You were defeated. Game Over.")
            return

    print("Battle End.")


# Elemental Reaction

class ElementalReaction:
    reaction_bonus = {
        ("Pyro", "Electro"): 10,  # Overloaded
        ("Electro", "Hydro"): 15,  # Electro-Charged
        ("Cryo", "Pyro"): 20,  # Melt
        ("Hydro", "Pyro"): 20,  # Vaporize
    }

    @staticmethod
    def calculate(player_element, enemy_element):
        return ElementalReaction.reaction_bonus.get((player_element, enemy_element), 0)




# ClOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()