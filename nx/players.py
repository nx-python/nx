from .controllers import Controller, any_pressed as _any_pressed


class Player:
    def __init__(self, number):
        self.number = number
        self.controller = Controller.from_player(self)

    _extra_controller_attributes = ('left', 'right', 'up', 'down', 'stick', 'left_stick',
                                    'right_stick', 'left_joycon', 'right_joycon')

    def __getattr__(self, item):
        if item.endswith('_button') or item in self._extra_controller_attributes:
            try:
                return getattr(self.controller, item)
            except AttributeError:
                return None

    def any_pressed(self, *buttons):
        return _any_pressed(self, *buttons)
