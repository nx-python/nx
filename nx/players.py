from .controllers import Controller


class Player:
    def __init__(self, number):
        self.number = number
        self.controller = Controller.from_player(self)

    @property
    def a_button(self):
        return self.controller.a_button

    @property
    def b_button(self):
        return self.controller.b_button

    @property
    def x_button(self):
        return self.controller.x_button

    @property
    def y_button(self):
        return self.controller.y_button

    @property
    def left(self):
        return self.controller.left

    @property
    def right(self):
        return self.controller.right

    @property
    def up(self):
        return self.controller.up

    @property
    def down(self):
        return self.controller.down

    @property
    def stick(self):
        return self.controller.stick
