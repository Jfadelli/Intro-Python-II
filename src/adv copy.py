from room import Room
from player import Player
from items import Item


# Declare all the rooms

outside = Room("Outside Cave Entrance", "North of you, the cabe mount beckons")
foyer = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")
overlook = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.")
narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")
treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [])

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Dang')
player.current_room = outside
foyer.add_items('sword')

sword = Item('sword', 'Unique Sword')
shield = Item('shield', 'Rare Shield')

# Write a loop that:
#
# * Prints the current room name
print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
print(player.current_room.description)
# * Waits for user input and decides what to do.
user = input('enter command: [move NSEW] [get/drop] [name item]:')
command = user.split(' ')[0]
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

if len(user.split(' ')) > 1:
    action = user.split(' ')[1]
    item_name = user.split(' ')[2]

while not command == 'q':
    if command in {'n','s','e','w'}:
        if hasattr(player.current_room, f'{command}_to'):
            player.current_room = getattr(
                player.current_room, f'{command}_to')
            print(player.current_room)
            user = input('choose command: N, S, W, E, --or-- q to quit: ')
            command = user.split(' ')[0]
            if command in {'i', 'get', 'drop'}:
                if command == 'i':
                    print(player.items)
                elif command == 'get':
                    item = user.split(' ')[1]
                    if player.current_room.items.count(f'{item}') > 0:
                        print(player.current_room.items)
                        player.current_room.items.remove(f'{item}')
                        print(player.current_room.items)
                    else:
                        print('That item is not in this room.')
                elif command == 'drop'
                item 

        else: 
            print('cannot move in that direction')
            user = input('choose direction: N, S, W, E --or-- q to quit: ')
            command = user.split(' ')[0]
    else:
        print('enter in a valid direction')
        user = input('choose direction: N, S, W, E --or-- q to quit: ')
        command = user.split(' ')[0]