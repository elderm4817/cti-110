# Michael Elder
# 05/01/2025
# P5HW
# This game lets users create characters, display them, and simulate an attack using functions and loops.

import random

# --- DICE AND MODIFIERS ---
def roll_4d6_drop_lowest():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def get_modifier(stat):
    return (stat - 10) // 2

def roll_attack_damage(stat_value):
    return random.randint(1, 6) + get_modifier(stat_value)

# --- CHARACTER FUNCTIONS ---
def create_character():
    print("Welcome to Character Creation!\n")
    available_stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    stats = {}

    while available_stats:
        print(f"\nRemaining stats to roll: {', '.join(available_stats)}")
        stat_choice = input("Which stat would you like to roll for? ").capitalize()
        if stat_choice in available_stats:
            roll = roll_4d6_drop_lowest()
            mod = get_modifier(roll)
            stats[stat_choice] = roll
            print(f"You rolled a {roll} for {stat_choice}! Modifier: {mod:+}")
            available_stats.remove(stat_choice)
        else:
            print("Invalid choice or stat already chosen.")

    # --- Optional reroll logic ---
    reroll_used = False
    while not reroll_used:
        print("\nHere are your final stats:")
        for stat, value in stats.items():
            print(f"{stat}: {value} (Modifier: {get_modifier(value):+})")

        choice = input("\nWould you like to reroll up to 2 stats? (yes/no): ").lower()
        if choice == "yes":
            for i in range(2):
                stat_to_reroll = input(f"Enter stat #{i+1} to reroll (or press Enter to skip): ").capitalize()
                if stat_to_reroll in stats:
                    new_roll = roll_4d6_drop_lowest()
                    stats[stat_to_reroll] = new_roll
                    print(f"{stat_to_reroll} is now {new_roll} (Modifier: {get_modifier(new_roll):+})")
                elif stat_to_reroll == "":
                    break
                else:
                    print("Invalid stat name.")
            reroll_used = True
        elif choice == "no":
            reroll_used = True
        else:
            print("Please type 'yes' or 'no'.")

    name = input("\nEnter your character's name: ")
    hp = 15 + get_modifier(stats["Constitution"])

    character = {
        "name": name,
        "stats": stats,
        "hp": hp
    }

    display_character(character)
    input("\nPress Enter to continue to the game...")
    return character

def heal_after_battle(player):
    heal_amount = random.randint(4, 10)  # like rolling 1d8 + 2
    player["hp"] += heal_amount
    print(f"\n✨ You take a moment to rest and heal for {heal_amount} HP.")
    print(f"❤️ Your HP is now {player['hp']}.\n")

def display_character(character):
    print("\n--- Character Sheet ---")
    print(f"Name: {character['name']}")
    for stat, val in character['stats'].items():
        mod = get_modifier(val)
        print(f"{stat}: {val} (Modifier: {mod:+})")
    print(f"HP: {character['hp']}")
    print("------------------------")

# --- ENEMY FUNCTIONS ---
def create_enemy():
    names = ["Goblin", "Orc", "Skeleton", "Bandit", "Zombie"]
    name = random.choice(names)
    strength = random.randint(10, 16)
    hp = random.randint(10, 20)
    enemy = {"name": name, "strength": strength, "hp": hp}
    print(f"\n⚔️  A wild {name} appears with {hp} HP and Strength {strength}!")
    return enemy

# --- GAMEPLAY LOOP ---
def main():
    print("=== D&D Style Game ===")
    playing = True

    while playing:
        player = create_character()

        in_battle = True
        while in_battle:
            enemy = create_enemy()

            while player["hp"] > 0 and enemy["hp"] > 0:
                print("\nYour Turn!")
                print("1. Attack with Strength")
                print("2. Cast Magic (INT or CHA)")
                print("3. Show Character")
                print("4. Exit Game")
                action = input("Choose an action: ")

                if action == "1":
                    dmg = roll_attack_damage(player["stats"]["Strength"])
                    print(f"You strike with your weapon and deal {dmg} damage!")
                    enemy["hp"] -= dmg
                elif action == "2":
                    stat = input("Use Intelligence or Charisma? ").capitalize()
                    if stat in ["Intelligence", "Charisma"]:
                        dmg = roll_attack_damage(player["stats"][stat])
                        print(f"You cast a spell and deal {dmg} damage!")
                        enemy["hp"] -= dmg
                    else:
                        print("Invalid stat.")
                        continue
                elif action == "3":
                    display_character(player)
                    continue
                elif action == "4":
                    print("You flee the battle. Goodbye!")
                    return
                else:
                    print("Invalid input.")
                    continue

                if enemy["hp"] <= 0:
                    print(f"\n🎉 You defeated the {enemy['name']}!")
                    heal_after_battle(player)
                    break

                # Enemy's turn
                print(f"\n😈 The {enemy['name']} attacks!")
                enemy_dmg = roll_attack_damage(enemy["strength"])
                player["hp"] -= enemy_dmg
                print(f"The {enemy['name']} deals {enemy_dmg} damage to you!")

                if player["hp"] <= 0:
                    print("💀 You have been defeated! Game over.")
                    break
                else:
                    print(f"You have {player['hp']} HP remaining.")

            # Post-combat options
            if player["hp"] <= 0:
                choice = input("\nWould you like to play again with a new character? (yes/no): ").lower()
                if choice != "yes":
                    playing = False
                break
            else:
                choice = input("\nDo you want to fight another enemy? (yes/no): ").lower()
                if choice != "yes":
                    playing = False
                    in_battle = False

    print("\nThanks for playing! 🎲")

# --- RUN THE GAME ---
if __name__ == "__main__":
    main()
