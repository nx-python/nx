from .controllers import Controller


class Player:
    def __init__(self, number):
        self.number = number
        self.controller = Controller.from_player(self)
