import _nx

from .utils import cached_property


def _determine_controller_type(player):
    # TODO determine the type of the controller for this player via _nx
    return DualJoyconController


class Controller:
    def __init__(self, player):
        self.player = player
        self.a_button = Button(self.player, 0)
        self.b_button = Button(self.player, 1)
        self.x_button = Button(self.player, 2)
        self.y_button = Button(self.player, 3)

    @staticmethod
    def from_player(player):
        controller_class = _determine_controller_type(player)
        return controller_class(player)


class JoyconController(Controller):
    def __init__(self, player, is_left, parent=None):
        super().__init__(player)
        self.is_left = is_left
        self.parent = parent

        if is_left:
            self.stick_button = Button(self.player, 4)
            self.l_or_r_button = Button(self.player, 6)
            self.zl_or_zr_button = Button(self.player, 8)
            self.plus_or_minus_button = Button(self.player, 11)
            self.stick = Stick(self.player, is_left=True)
        else:
            self.stick_button = Button(self.player, 5)
            self.l_or_r_button = Button(self.player, 7)
            self.zl_or_zr_button = Button(self.player, 9)
            self.plus_or_minus_button = Button(self.player, 10)
            self.stick = Stick(self.player, is_left=False)

        self.left = Button(player, self.stick.left_key_bit)
        self.right = Button(player, self.stick.right_key_bit)
        self.up = Button(player, self.stick.up_key_bit)
        self.down = Button(player, self.stick.down_key_bit)

    @cached_property
    def sl_button(self):
        if self.parent is not None and self.parent.is_attached:
            return None
        return Button(self.player, 24)

    @cached_property
    def sr_button(self):
        if self.parent is not None and self.parent.is_attached:
            return None
        return Button(self.player, 25)


class StandardController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self.left_stick_button = Button(self.player, 4)
        self.right_stick_button = Button(self.player, 5)
        self.l_button = Button(self.player, 6)
        self.r_button = Button(self.player, 7)
        self.zl_button = Button(self.player, 8)
        self.zr_button = Button(self.player, 9)
        self.plus_button = Button(self.player, 10)
        self.minus_button = Button(self.player, 11)
        self.left_button = Button(self.player, 12)
        self.right_button = Button(self.player, 13)
        self.up_button = Button(self.player, 14)
        self.down_button = Button(self.player, 15)
        self.left_stick = Stick(self.player, is_left=True)
        self.right_stick = Stick(self.player, is_left=False)
        self.stick = self.left_stick
        self.left = Button(player, self.stick.left_key_bit, self.left_button.key_bits[0])
        self.right = Button(player, self.stick.right_key_bit, self.right_button.key_bits[0])
        self.up = Button(player, self.stick.up_key_bit, self.up_button.key_bits[0])
        self.down = Button(player, self.stick.down_key_bit, self.down_button.key_bits[0])


class SwitchProController(StandardController):
    pass


class DualJoyconController(StandardController):
    def __init__(self, player):
        super().__init__(player)
        self.is_attached = True
        self.left_joycon = JoyconController(player, is_left=True, parent=self)
        self.right_joycon = JoyconController(player, is_left=False, parent=self)


class FreeDualJoyconController(DualJoyconController):
    def __init__(self, player):
        super().__init__(player)
        self.is_attached = False


class Button:
    def __init__(self, player, *key_bits):
        self.player = player
        self.key_bits = key_bits

    @property
    def is_pressed(self):
        return any_pressed(self.player, self)


class Stick:
    def __init__(self, player, is_left):
        self.player = player
        self.is_left = is_left
        if is_left:
            self.left_key_bit = 16
            self.right_key_bit = 18
            self.up_key_bit = 17
            self.down_key_bit = 19
        else:
            self.left_key_bit = 20
            self.right_key_bit = 22
            self.up_key_bit = 21
            self.down_key_bit = 23

    @property
    def left(self):
        return self.x < 0.0

    @property
    def right(self):
        return self.x > 0.0

    @property
    def up(self):
        return self.y > 0.0

    @property
    def down(self):
        return self.y < 0.0

    @property
    def x(self):
        keys_pressed = _nx.hid_keys_pressed(self.player.number - 1)
        if keys_pressed & self.left_key_bit:
            return -1.0
        if keys_pressed & self.right_key_bit:
            return 1.0
        return 0.0

    @property
    def y(self):
        keys_pressed = _nx.hid_keys_pressed(self.player.number - 1)
        if keys_pressed & self.up_key_bit:
            return 1.0
        if keys_pressed & self.down_key_bit:
            return -1.0
        return 0.0


def any_pressed(player, *buttons: Button):
    keys_pressed = _nx.hid_keys_pressed(player.number - 1)
    if len(buttons) == 0:
        return not keys_pressed == 0
    for button in buttons:
        for key_bit in button.key_bits:
            if keys_pressed & key_bit:
                return True
    return False
