# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__ (self, name, current_room=None):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_item(self, item):
        self.items.append(item)
        return self.items

    def drop_item(self, item):
        self.items.remove(item)
        return self.items
    
    def __str__(self):
        return f'Current location:\n {self.current_room}'