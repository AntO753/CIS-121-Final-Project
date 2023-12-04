import random
import time


class Player:
    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp


class Thief(Player):
    def __init__(self, name, weapon, hp, room_number):
        super().__init__(name, "Thief", hp)
        self.weapon = weapon
        self.room = room_number

    def intro_self(self):
        print(
            f"My name is {self.name} You won't be able to make it past room {self.room}!")


def weapons_choice():
    if len(player_weapons) > 1:
        num = 1
        for weapon in player_weapons:
            num += 1
            print(f"{num}. {weapon}")
        choose_weapon = int(
            input("Choose the number asscoiated with the weapon you want to choose: "))
    else:
        choose_weapon = 1
        print("Your Weapon to start is a Lazer Pistol.")
    return choose_weapon


def damage(player_type, weapon):
    damage = random.randint(0, 901)
    if player_type == "boxer":
        if weapon == 3 or weapon == 6 or weapon == 9:
            if damage != 0:
                damage += damage * .10
    elif player_type == "sword-fighter":
        if weapon == 2 or weapon == 4 or weapon == 8:
            if damage != 0:
                damage += damage * .10
    elif player_type == "shooter":
        if weapon == 1 or weapon == 5 or weapon == 7:
            if damage != 0:
                damage += damage * .10
    return damage


def perform_attack(attacker, defender, weapon):
    damage_value = damage(attacker.type, weapon)
    attacker_name = attacker.name
    defender_name = defender.name

    defender.hp -= damage_value
    print(f"{attacker_name} attacks {defender_name} and does {damage_value}pt damage")

    if damage_value == 0:
        print(f"{attacker_name} missed...")
    elif 20 < damage_value < 800:
        print(f"{attacker_name} got a hit.")
    elif damage_value >= 800:
        print("CRITICAL HIT!")
    else:
        print("hit wasn't effective.")
    return


def battle(player, enemy):
    print(f"{player.name} vs {enemy.name}")
    player_weapon = weapons_choice()
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}: {player.hp}")
        print(f"{enemy.name}: {enemy.hp}\n")

        player_choice = input(
            "Would you like to attack? (Enter yes or no): ")

        if player_choice.lower() == "yes":
            perform_attack(player, enemy, player_weapon)

        if enemy.hp > 0:
            print(f"{enemy.name} is attacking...")
            perform_attack(enemy, player, enemy.weapon)

        if player.hp <= 0:
            print(f"{player.name} lost...")
            break
        elif enemy.hp <= 0:
            print(f"{player.name} WON!")
            break

    return


def move_through_rooms():
    rooms = []
    return


player_name = input("Enter your Name: ")
player_type = input(
    "Choose your hero type: \n1. Shooter \n2. Boxer \n3. Sword-Fighter \nEnter fighter: ").lower()
player_hp = 3000

p1 = Player(player_name, player_type, player_hp)
player_weapons = ["Lazer Pistol"]

print("\n\nWelcome to the kingdom of Hestia. For years Hestia has thrived because of a mysterious crystal rightfully dubbed: The sacred Jewel.")
print("The Sacred Jewel is the central power source for the kingdom. It provides energy for every house including the castle. Unfortunately,")
print("Theives have managed to steal the Sacred Jewel and take it back to their own hide out.")
print("As the Hero of Hestia it's up to you to navigate through the thieves hideout and the take the Jewel back. Without it Hestia will remain in darkness...\n\n\n")


# def battle(vil):
#     if len(player_weapons) < 1:
#         print("You have a lazer pistol to start")
#         while vil.hp > 0:
#             if p1.hp == 0:
#                 print("You lost...")
#                 break
#             else:
#                 print(f"{p1.name}: {p1.hp}")
#                 print(f"{vil.name}: {vil.hp}")
#                 player_choice = input(
#                     "Would you like to attack? (Enter yes or no): ")
#                 player_damage = random.randint(0, 901)
#                 vil_damage = random.randint(0, 901)
#                 if player_choice.lower() == "yes":
#                     vil.hp -= player_damage
#                     print(
#                         f"{p1.name} Shoots {vil.name}  and does {player_damage}pt damage")
#                     if player_damage == 0:
#                         print("You missed...")
#                     elif player_damage <= 20:
#                         print("Shot wasn't effective.")
#                     elif player_damage >= 800:
#                         print("CRITICAL HIT!")
#                     else:
#                         print("Nice shot.")
#                     print(f"{vil.name} is attacking...")
#                     p1.hp -= vil_damage
#                     if vil_damage == 0:
#                         print("The Theif missed!")
#                     elif vil_damage <= 20:
#                         print("Shot wasn't effective.")
#                     elif vil_damage >= 800:
#                         print("CRITICAL HIT!")
#                     else:
#                         print("They're a good shot...")
#                 elif player_choice == "no":
#                     print(f"{vil.name} is attacking...")
#                     p1.hp -= vil_damage
#                     if vil_damage == 0:
#                         print("The Theif missed!")
#                     elif vil_damage <= 20:
#                         print("Shot wasn't effective.")
#                     elif vil_damage >= 2500:
#                         print("CRITICAL HIT!")
#                     else:
#                         print("They're a good shot...")
#     elif len(player_weapons) > 1:
#         player_weapon_choice = input(
#             f"Choose the number associated with the weapon you want to use: {player_weapons} ")
#         if player_weapon_choice == 1:
#             print("You chose a lazer pistol")
#             while vil.hp > 0:
#                 if p1.hp == 0:
#                     print("You lost...")
#                     break
#                 else:
#                     print(f"{p1.name}: {p1.hp}")
#                     print(f"{vil.name}: {vil.hp}")
#                     player_choice = input(
#                         "Would you like to attack? (Enter yes or no): ")
#                     player_damage = random.randint(0, 901)
#                     vil_damage = random.randint(0, 901)
#                     if player_choice.lower() == "yes":
#                         vil.hp -= player_damage
#                         print(
#                             f"{p1.name} Shoots {vil.name}  and does {player_damage}pt damage")
#                         if player_damage == 0:
#                             print("You missed...")
#                         elif player_damage <= 20:
#                             print("Shot wasn't effective.")
#                         elif player_damage >= 800:
#                             print("CRITICAL HIT!")
#                         else:
#                             print("Nice shot.")
#                         print(f"{vil.name} is attacking...")
#                         p1.hp -= vil_damage
#                         if vil_damage == 0:
#                             print("The Theif missed!")
#                         elif vil_damage <= 20:
#                             print("Shot wasn't effective.")
#                         elif vil_damage >= 800:
#                             print("CRITICAL HIT!")
#                         else:
#                             print("They're a good shot...")
#                     elif player_choice == "no":
#                         print(f"{vil.name} is attacking...")
#                         p1.hp -= vil_damage
#                         if vil_damage == 0:
#                             print("The Theif missed!")
#                         elif vil_damage <= 20:
#                             print("Shot wasn't effective.")
#                         elif vil_damage >= 800:
#                             print("CRITICAL HIT!")
#                         else:
#                             print("They're a good shot...")
#         elif player_weapon_choice == 2:
#             print("You chose a lazer Sword")
#             while vil.hp > 0:
#                 if p1.hp == 0:
#                     print("You lost...")
#                     break
#                 else:
#                     print(f"{p1.name}: {p1.hp}")
#                     print(f"{vil.name}: {vil.hp}")
#                     player_choice = input(
#                         "Would you like to attack? (Enter yes or no): ")
#                     player_damage = random.randint(0, 1001)
#                     vil_damage = random.randint(0, 1001)
#                     if player_choice.lower() == "yes":
#                         vil.hp -= player_damage
#                         print(
#                             f"{p1.name} Slashes {vil.name}  and does {player_damage}pt damage")
#                         if player_damage == 0:
#                             print("You missed...")
#                         elif player_damage <= 30:
#                             print("Shot wasn't effective.")
#                         elif player_damage >= 900:
#                             print("CRITICAL HIT!")
#                         else:
#                             print("Nice hit.")
#                         print(f"{vil.name} is attacking...")
#                         p1.hp -= vil_damage
#                         if vil_damage == 0:
#                             print("The Theif missed!")
#                         elif vil_damage <= 30:
#                             print("Shot wasn't effective.")
#                         elif vil_damage >= 900:
#                             print("CRITICAL HIT!")
#                         else:
#                             print("They're a good swordsman...")
#                     elif player_choice == "no":
#                         print(f"{vil.name} is attacking...")
#                         p1.hp -= vil_damage
#                         if vil_damage == 0:
#                             print("The Theif missed!")
#                         elif vil_damage <= 30:
#                             print("Shot wasn't effective.")
#                         elif vil_damage >= 900:
#                             print("CRITICAL HIT!")
#                         else:
#                             print("They're a good shot...")

#     return


def room1():
    print("You enter the first room in the thieves hide out and realize there's someone waiting there for you.\n")
    v1 = Thief("Goon", "Super sword", 1500, "1")
    v1.intro_self()

    battle(p1, v1)

    return


room1()
