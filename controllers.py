def _determine_controller_type(player):
    # TODO determine the type of the controller
    # for this player using libnx
    return Controller


class Controller:
    def __init__(self, player):
        self._player = None
        self.player = player

    @staticmethod
    def from_player(player):
        controller_class = _determine_controller_type(player)
        return controller_class(player)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player


class SwitchProController(Controller):
    pass


class JoyconController:
    pass


class DualJoyconController:
    pass


class Button:
    def __init__(self, controller):
        self.controller = controller

    def is_pressed(self):
        # TODO
        pass

    def is_released(self):
        # TODO
        pass


class Joystick:
    pass
