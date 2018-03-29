def _determine_controller_type(player):
    # TODO determine the type of the controller for this player via _nx
    return DualJoyconController


class Controller:
    def __init__(self):
        pass

    @staticmethod
    def from_player(player):
        controller_class = _determine_controller_type(player)
        return controller_class()


class SwitchProController(Controller):
    pass


class JoyconController(Controller):
    pass


class DualJoyconController(Controller):
    pass


class FreeDualJoyconController(DualJoyconController):
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
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def wait_for_movement(self):
        raise NotImplementedError

    def wait_for_neutral_position(self):
        raise NotImplementedError
