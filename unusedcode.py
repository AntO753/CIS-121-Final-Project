    # if current_room == room_1:
    #     if player in room_1:
    #         current_room.remove(player)
    #         if direction.lower() == "north":
    #             room_2.append(player)
    #         elif direction.lower() == "south":
    #             room_3.append(player)
    #         elif direction.lower() == "east":
    #             room_4.append(player)
    #         elif direction.lower() == "west":
    #             room_5.append(player)
    #         else:
    #             print("Invalid direction. Please choose north, south, east or west.")
    #     else:
    #         print("You are not in the current room.")
    # elif current_room == room_2:
    #     if player in room_2:
    #         current_room.remove(player)
    #         if direction.lower() == "south":
    #             room_1.append(player)
    #         else:
    #             print("Invalid direction. Please choose north, south, east or west.")
    #     else:
    #         print("You are not in the current room.")
    # elif current_room == room_3:
    #     if player in room_3:
    #         current_room.remove(player)
    #         if direction.lower() == "east":
    #             room_1.append(player)
    #         else:
    #             print("Invalid direction. Please choose north, south, east or west.")
    #     else:
    #         print("You are not in the current room.")
    # elif current_room == room_4:
    #     if player in room_4:
    #         current_room.remove(player)
    #         if direction.lower() == "north":
    #             room_1.append(player)
    #         else:
    #             print("Invalid direction. Please choose north, south, east or west.")
    #     else:
    #         print("You are not in the current room.")
    # elif current_room == room_5:
    #     if player in room_5:
    #         current_room.remove(player)
    #         if direction.lower() == "west":
    #             room_1.append(player)
    #         else:
    #             print("Invalid direction. Please choose north, south, east or west.")
    #     else:
    #         print("You are not in the current room.")

    #return




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