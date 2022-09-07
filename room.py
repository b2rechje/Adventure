# ***************************************************************************
# * room.py
# *
# * Minor programmeren - Programmeren 2
# * Brechje Seegers
# *
# * - Defining Class Room for adventure
# ***************************************************************************

class Room:
    """
    Initialize the object attributes of the class Room.
    """
    def __init__(self, name, short_description, long_description):
        self._short_description = short_description
        self._long_description = long_description
        self.visit = False
        self.connections = {}
        self.room_id = name
        self.inventory = {}

    def add_inventory(self, name, item):
        """
        Add items from loader to inventory
        """
        self.inventory[name] = item

    def print_inventory(self):
        """
        Loop through dictonary inventory by room and print contents
        """
        to_print = ""
        for key, value in self.inventory.items():
            to_print = to_print + '\n' + value.description_items()

        return to_print

    # checkt of request item is aanwezig in de kamer
    def check_item(self, request):
        """
        Check if item requested by user is present in inventory of room
        """
        if request in self.inventory:
            return True
            
        return False

    # weghalen uit inventory dictionary van room
    def remove_item_room(self, request):
        """
        Remove item from inventory
        """
        keys = self.inventory[request]
        del self.inventory[request]
        return keys

    #toevoegen aan je inventory dictionary van room
    def add_item_room(self, item):
        """
        Adds item to the inventory
        """
        self.inventory[item.item_name] = item

    # methode die bezochte kamer als bezocht markeert
    def set_visited(self):
        """
        Set not visited room as visited
        """
        self.visit = True

    def set_devisited(self):
        """
        Set visited as not visited
        """
        self.visit = False

    def description(self):
        """
        Give description of the room visited. If the room has already been visited
        then give small description, otherwise give long description.
        """
        if self.visit == False:
            return self._long_description
        else:
            return self._short_description

    def add_connection(self, direction, room, item):
        """
        Add connection to the room
        """
        if direction in self.connections:
            self.connections[direction].extend([room, item])
        else:
            self.connections[direction] = [room, item]

    def has_connection(self, direction):
        """
        Determines whether connection can be
        """
        if direction in self.connections:
            return True

        return False

    def get_connection(self, direction):
        """
        Receives a room and returns specific direction
        """
        return self.connections[direction]
