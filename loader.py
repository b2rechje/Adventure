# ***************************************************************************
# * loader.py
# *
# * Minor programmeren - Programmeren 2
# * Brechje Seegers
# *
# * - Defining load functions for the game adventure
# ***************************************************************************

from room import Room
from item import Item


def load_room_graph(filename):
    """
    Load function which loads information from a text file and
    stores information about the rooms with their connections
    """
    rooms = {}
    items = {}

    # Read the rooms from the file and add them to the dictionary rooms
    with open(filename) as file:
        line = file.readline()

        while line != "\n":
            read_part = line.split("\t")
            room = Room(read_part[0], read_part[1], read_part[2])
            rooms[int(read_part[0])] = room
            line = file.readline()

        assert 1 in rooms
        assert rooms[1]._short_description == "Outside building"

        # Read the directions and split conditional movements
        line = file.readline()
        while line != "\n":
            read_part = line.strip().split("\t")
            source_room = rooms[int(read_part[0])]

            for i in range(1, len(read_part), 2):
                if '/' in read_part[i + 1]:
                    direction = read_part[i]
                    destination_room, item = read_part[i + 1].split('/')
                    source_room.add_connection(direction, rooms[int(destination_room)], item)
                else:
                    direction = read_part[i]
                    destionation_room = rooms[int(read_part[i+1])]
                    item = None
                    source_room.add_connection(direction, destionation_room, item)
                    
            line = file.readline()

        # Read items from file and add to item objects and place in correct room
        line = file.readline()
        while line != "":
            item = line.strip().split("\t")
            name = item[0]
            description = item[1]
            source_room = int(item[2])
            item = Item(name, description)
            rooms[source_room].add_inventory(name, item)
            line = file.readline()

    return rooms[1]


def load_synonyms(filename):
    """
    Load function that loads the information about synonyms from a text
    file and stores it in a dictionary called synonyms.
    """
    synonyms = {}

    # Read lines from file and split the parts based on the '=', save them
    with open(filename) as file:
        line = file.readline()
        while line != "":
            synonym_info = line.strip().split("=")
            letter = synonym_info[0]
            word = synonym_info[1]
            synonyms[letter] = word
            line = file.readline()
    # Return de dictionary to adventure
    return synonyms
