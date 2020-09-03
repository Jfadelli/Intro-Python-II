# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
    def add_items(self, item):
        self.items.append(item)
    
    def __str__(self):
        return f"\nThis is the {self.name} room.\n \nDescription: {self.description}\n\nItems in Room:{self.items}"