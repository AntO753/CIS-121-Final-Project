import random
import time


''' ToDO

room3, room4, room5 battle functions (room3())
    each room should handle defeat with map object
set battles in map.init

'''

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
        
class Room:
    def __init__(self, room_num, north=None, west=None, east=None, south=None) -> None:
        self.room_num = room_num
        self.battle = None
        self.defeated = False
        self.north = north
        self.west = west
        self.east = east
        self.south = south

    def add_north(self, north):
        self.north = north
    def add_east(self, east):
        self.east = east
    def add_west(self, west):
        self.west = west
    def add_south(self, south):
        self.south = south
    def set_battle(self, battle):
        self.battle = battle
    def defeat(self):
        self.defeated = True
    def __str__(self) -> str:
        return self.room_num
    
    
class Map:
    rooms = {
        'room_1': Room('1'),
        'room_2': Room('2'),
        'room_3': Room('3'),
        'room_4': Room('4'),
        'room_5': Room('5')
    }
    player_location = None
    def __init__(self, player) -> None:
        self.player = player
        self.player_location = self.rooms['room_1']
        # connect rooms
        self.rooms['room_1'].add_north(self.rooms['room_2'])
        self.rooms['room_1'].add_east(self.rooms['room_3'])
        self.rooms['room_1'].add_west(self.rooms['room_5'])
        self.rooms['room_1'].add_south(self.rooms['room_4'])
        self.rooms['room_2'].add_south(self.rooms['room_1'])
        self.rooms['room_3'].add_west(self.rooms['room_1'])
        self.rooms['room_4'].add_north(self.rooms['room_1'])
        self.rooms['room_5'].add_east(self.rooms['room_1'])
        # set battles
        self.rooms['room_1'].set_battle(room1)
        self.rooms['room_2'].set_battle(room2)

    def travel(self, direction):
        if direction == 'north' and self.player_location.north != None:
            self.player_location = self.player_location.north
        elif direction == 'west' and self.player_location.west != None:
            self.player_location = self.player_location.west
        elif direction == 'east' and self.player_location.east != None:
            self.player_location = self.player_location.east
        elif direction == 'south' and self.player_location.south != None:
            self.player_location = self.player_location.south
        else:
            print("Sorry, you can't go there.")
            return
        print(f'You have entered room {self.player_location}')

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

        while True:
            player_choice = input(
                "Would you like to attack? (Enter yes or no): ")
            if player_choice == 'yes' or player_choice == 'no':
                break
            else:
                print('Please enter a valid choice!')
        

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

def move_through_rooms(direction: str):
    map.travel(direction)

def room1():
    room_num = 'room_1'
    if map.rooms[room_num].defeated:
        print("The Goon is dead.")
        return
    print("You enter the first room in the thieves hide out and realize there's someone waiting there for you.\n")
    v1 = Thief("Goon", "Super sword", 1500, "1")
    v1.intro_self()

    battle(p1, v1)
    if p1.hp > 0:
        map.rooms[room_num].defeat()
        player_weapons.append("Super Sword")
        print('Congrats! You beat the Goon! You have received a Super Sword! It has been added to your inventory.')
    else:
        while True:
            deathChoice = str(input('Do you want to try over again? Please enter "yes" or "no": '))
            if deathChoice == 'yes':
                p1.hp = 3000
                return map.player_location.battle()
            elif deathChoice == 'no':
                print('Better luck next time!')
                exit()
            else:
                print('Please enter "yes" or "no" only. Try again.')
    return

def room2():
    room_num = 'room_2'
    if map.rooms[room_num].defeated:
        print("The Hooligan is dead.")
        return
    print("You enter the second room in the thieves hide out and realize there's someone waiting there for you.\n")
    v2 = Thief("Hooligan", "Gauntlets", 1800, "2")
    v2.intro_self()

    battle(p1, v2)
    if p1.hp > 0:
        map.rooms[room_num].defeat()
        player_weapons.append("Gauntlets")
        print('Congrats! You beat the Hooligan! You have received Gauntlets! They have been added to your inventory.')
    else:
        while True:
            deathChoice = str(input('Do you want to try over again? Please enter "yes" or "no": '))
            if deathChoice == 'yes':
                p1.hp = 3000
                return map.player_location.battle()
            elif deathChoice == 'no':
                print('Better luck next time!')
                exit()
            else:
                print('Please enter "yes" or "no" only. Try again.')
    return

def hestia(map: Map):
    map.player_location.battle()
    userDirection = None
    while True:
        userDirection = str(input('Please enter a direction to move to another room: '))
        if userDirection.lower() in ['north', 'south', 'east', 'west']:
            break
        else:
            print('Please enter a valid direction! You may enter "North", "South", "East" or "West". Try again!')
    move_through_rooms(userDirection)
    hestia(map)


player_name = input("Enter your Name: ")

while True:
    player_type = input(
    "Choose your hero type: \n1. Shooter \n2. Boxer \n3. Sword-Fighter \nEnter fighter: ").lower()
    if player_type == 'shooter' or player_type == 'boxer' or player_type == 'sword-fighter':
        break
    else:
        print('Please enter a correct hero type. You may enter "Shooter", "Boxer", or "Sword-Fighter". Please try again.')

player_hp = 3000

p1 = Player(player_name, player_type, player_hp)
player_weapons = ["Lazer Pistol"]

map = Map(p1)
print("\n\nWelcome to the kingdom of Hestia. For years Hestia has thrived because of a mysterious crystal rightfully dubbed: The sacred Jewel.")
print("The Sacred Jewel is the central power source for the kingdom. It provides energy for every house including the castle. Unfortunately,")
print("Theives have managed to steal the Sacred Jewel and take it back to their own hide out.")
print("As the Hero of Hestia it's up to you to navigate through the thieves hideout and the take the Jewel back. Without it Hestia will remain in darkness...\n\n\n")
hestia(map)

