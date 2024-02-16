import json
import sys
import random

with open('D:/VScode/รับงาน/rooms.json') as f:
     rooms = json.load(f)

# Retrieve the starting inventory, if any.
inventory = []
if 'starting_inventory' in rooms:
    inventory = rooms['starting_inventory']
    
# Variables that store the current room we're in and the next room we will visit.
room = None

#random starting point
randomRooms = random.randint(0,1)
if randomRooms == 0:
    # The game starts in the room called 'plane crash'.
    next_room = rooms["plane crash"]
else:
    # The game starts in the room called 'tree'.
    next_room = rooms["tree"]

# Continue looping so long as the next room isn't an exit room.
while not(next_room['exit']):
    # Move to the next room.
    room = next_room
    next_room = None
        
    # Obtain the description of the room. If this room's description changes when
    # the user is carrying a specific item, change the description accordingly.
    description = room['description']
    if room['if_has'] is not None and room['if_has']['item'] in inventory:
        description = room['if_has']['description']
        
    # Print the description.
    print(description)

    # Keep grabbing user input until user switches to another room.
    while next_room is None:
        # List all valid actions specific to this room.
        print("You can...")
        for possible_action in room['actions'].keys():
            print("\t" + possible_action)

        # List inventory items in room, if any
        if len(room['in_room']) > 0:
            print("You see...")
            for item in room['in_room']:
                print ("\t{}".format(item))

        # Prompt for, read, and clean the user's input.
        user_input = input('> ').strip().lower()

        # Actions that aren't room-specific are parsed first.
        if user_input == "help":
            print("Available commands:")
            print("help - Displays a list of available commands and their functionality.")
            print("look - Repeats the room description.")
            print("inventory - Displays the items currently held by the player.")
            print("get [item] - Picks up an item from the room and adds it to the player's inventory.")
            print("drop [item] - Drops an item from the player's inventory and adds it to the current room.")
            print("[direction] - Moves the player to a different room in the specified direction (if available).")
        elif user_input == "look":
            # Update and print the description.
            description = room['description']
            if room['if_has'] is not None and room['if_has']['item'] in inventory:
                description = room['if_has']['description']
            print(description)
        elif user_input == "i" or user_input == "inventory":
            # TODO: FILL IN HERE.
            # List inventory.
            if len(inventory) == 0:
                print("You are not carrying anything.")
            else:
                print("You are holding " + ", ".join(inventory) + ".")
        elif user_input.startswith("get"):
            # Try to pick up an item.
            item_name = user_input[4:]
            if item_name in room['in_room']:
                inventory.append(item_name)
                room['in_room'].remove(item_name)
                print("You pick up the {}.".format(item_name))
            else:
                print("I don't see that here.")
        elif user_input.startswith("drop"):
             # Try to drop an item.
            item_name = user_input[5:]
            if item_name in inventory:
                inventory.remove(item_name)
                room['in_room'].append(item_name)
                print("You drop the {}.".format(item_name))
            else:
                print("You don't appear to be carrying that.")

        # Process requests for the user to move to a new room.
        elif user_input in room['actions']:
            # Tentatively advance to the next room.
            candidate_room = rooms[room['actions'][user_input]]
            
            # Keeps track of whether the user has all necessary items and doesn't have
            # any disallowed items.
            has_disallowed_item = False
            missing_required_item = False

            # If person is holding item in the cannot_have list, block the choice.
            for disallowed_item in candidate_room['cannot_have']:
                if disallowed_item in inventory:
                    has_disallowed_item = True

            # If person is not holding item in the must_have list, block the choice.
            for required_item in candidate_room['must_have']:
                missing_required_item = True
                if required_item in inventory:
                    missing_required_item = False

            # If one of the tests failed, print accordingly. Otherwise, advance.
            if has_disallowed_item:
                print("A strange force prevents you from doing that.")
            elif missing_required_item:
                print("You cannot do that. Maybe you are missing an item?")
            else:
                next_room = candidate_room
        
        else:
            print(user_input + " is not supported. Please try again.")

# The game is now complete. Print the description of the final room.
description = next_room['description']
if next_room['if_has'] is not None and next_room['if_has']['item'] in inventory:
    description = next_room['if_has']['description']
print(description)

print()
print("Game over. Thank you for playing!")