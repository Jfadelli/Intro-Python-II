from room import Room

class Item:
    def __init__(self, i_name, i_description):
        self.i_name = i_name
        self.i_description = i_description

    def __repr__(self):
        return f'Item:{self.i_name} Description: {self.i_description}'
