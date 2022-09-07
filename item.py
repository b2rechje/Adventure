# ***************************************************************************
# * item.py
# *
# * Minor programmeren - Programmeren 2
# * Brechje Seegers
# *
# * - Defining Item Class for adventure
# ***************************************************************************

class Item:

    def __init__(self, name, description):
        """
        Initialize the object attributes of the class item.
        """
        self.item_name = name
        self.item_description = description

    def description_items(self):
        """
        Returns the key (name of the item) and the value (item description).
        """
        return f"{self.item_name}: {self.item_description}"
