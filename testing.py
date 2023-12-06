class Room:
    def __init__(self, room_num, north=None, west=None, east=None, south=None) -> None:
        self.room_num = room_num
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

def tests():
    map = Map('leanne')
    print(*map.rooms)
    # print(map.rooms['room_1'].north)
    print(map.player_location)
    map.travel('north')
    print(map.player_location)
    map.travel('south')
    map.travel('south')
    print(map.player_location)

tests()