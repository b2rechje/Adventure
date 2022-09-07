# ***************************************************************************
# * adventure.py
# *
# * Minor programmeren - Programmeren 2
# * Brechje Seegers
# *
# * - Play the game of adventure
# ***************************************************************************

import loader

class Adventure():

    def __init__(self, filename):
        """
        Initialiseer de object's attributes van de class adventure.
        """
        self.rooms = {}
        self._current_room = loader.load_room_graph(filename)
        self.backpack = {}
        self.synonyms = loader.load_synonyms("data/Synonyms.dat")

    def room_description(self):
        """
        Pass along the description of the current room, be it short or long.
        """
        return self._current_room.description()

    def has_item_backpack(self, item):
        """
        Checks the item for the move needed is in the backpack.
        """
        if item in self.backpack:
            return True

        return False

    def move(self, direction):
        """
        Move to a different room by changing "current" room, if possible.
        """
        if self._current_room.has_connection(direction):
            self._current_room.set_visited()
            current_connection = self._current_room.get_connection(direction)

            for i in range(0, len(current_connection), 2):
                if current_connection[i + 1] is None:
                    self._current_room = current_connection[i]
                    return True
                else:
                    # Check if the user has the correct item, if so, move to room
                    if self.has_item_backpack(current_connection[i + 1]) is True:
                        self._current_room = current_connection[i]
                        return True

        return False


    def take(self, request):
        """
        Takes item and adds it to the user's backpack (and remove from inventory
        room) if item is present in the current room.
        """
        if self._current_room.check_item(request):
            self.backpack[request] = self._current_room.remove_item_room(request)
            return True

        return False

    def drop(self, request):
        """
        Dropped item from backpack if it was in it and added the item to the
        inventory of the current room.
        """
        if request in self.backpack:
            keys = self.backpack[request]
            del self.backpack[request]
            self._current_room.add_item_room(keys)
            return True

        return False


if __name__ == "__main__":

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python3 adventure.py [name]")
        exit(1)

    # Load the requested game or else Tiny
    print("Loading...")

    if len(argv) == 2:
        game_name = argv[1]
    elif len(argv) == 1:
        game_name = "Tiny"

    filename = f"data/{game_name}Adv.dat"

    # Create game
    adventure = Adventure(filename)

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.room_description())

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt, converting all input to upper case
        command = input("> ").upper()

        # If synonym is entered, pass command
        if command in adventure.synonyms:
            command = adventure.synonyms[command]

        # Calls methods if user wants to take an item
        if "TAKE" in command:
            command = command.split()

            if adventure.take(command[1]):
                print(f"{command[1]} taken")
            else:
                print("No such item.")

        # Calls methods if user wants to drop an item
        elif "DROP" in command:
            command = command.split()

            if adventure.drop(command[1]):
                print(f"{command[1]} dropped")
            else:
                print("No such item.")

        # Print the instructions
        elif "HELP" in command:
            print("You can move by typing directions such as EAST/WEST/IN/OUT."
                "QUIT quits the game."
                "HELP prints instructions for the game."
                "LOOK lists the complete description of the room and its contents."
                "INVENTORY lists all items in your inventory.")

        # Print the room description of the current room
        elif "LOOK" in command:
            adventure._current_room.set_devisited()
            print(adventure.room_description())
            print(adventure._current_room.print_inventory())
            adventure._current_room.set_visited()

        # Print the items of the inventory of the user
        elif "INVENTORY" in command:
            if len(adventure.backpack) == 0:
                print("Your inventory is empty")
            else:
                for key, value in adventure.backpack.items():
                    print(value.description_items())

        # Perform the move or other command
        elif adventure.move(command) == False:
            print("Invalid command.")

        else:
            print(adventure.room_description())
            print(adventure._current_room.print_inventory())

        while adventure.move("FORCED"):
            print(adventure.room_description())

        # Allows player to exit the game loop
        if command == "QUIT":
            break
