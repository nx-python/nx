import _nx
import warnings

from .utils import bit, cached_property


def _determine_controller_type(player):
    # TODO determine the type of the controller for this player via _nx
    return DualJoyconController


class Controller:
    """
    Represents a standard type of controller

    :attribute: player
    :type: Player

    <todo>

    :attribute: a_button
    :type: Button

    The A button of the controller

    :attribute: b_button
    :type: Button

    The B button of the controller

    :attribute: x_button
    :type: Button

    The X button of the controller

    :attribute: y_button
    :type: Button

    The Y button of the controller
    """
    def __init__(self, player):
        self.player = player
        self.a_button = Button(self.player, bit(0))
        self.b_button = Button(self.player, bit(1))
        self.x_button = Button(self.player, bit(2))
        self.y_button = Button(self.player, bit(3))

    @staticmethod
    def from_player(player):
        """
        <todo>
        
        :param player: player param

        :returns: <todo> Controller class
        :rtype: Controller
        """
        controller_class = _determine_controller_type(player)
        return controller_class(player)


class JoyconController(Controller):
    """
    Represents a single Joycon controller

    :attribute: is_left
    :type: bool

    Whether the controller is the left or right Joycon

    :attribute: parent
    :type: <todo>

    The parent of the controller

    :attribute: stick_button
    :type: Button

    <todo>
    
    :attribute: l_or_r_button
    :type: Button

    <todo>

    :attribute: zl_or_zr_button
    :type: Button

    <todo>

    :attribute: plus_or_minus_button
    :type: Button

    <todo>

    :attribute: stick
    :type: Stick

    <todo>
    """
    def __init__(self, player, is_left, parent=None):
        super().__init__(player)
        self.is_left = is_left
        self.parent = parent

        if is_left:
            self.stick_button = Button(self.player, bit(4))
            self.l_or_r_button = Button(self.player, bit(6))
            self.zl_or_zr_button = Button(self.player, bit(8))
            self.plus_or_minus_button = Button(self.player, bit(11))
            self.stick = Stick(self.player, is_left=True)
        else:
            self.stick_button = Button(self.player, bit(5))
            self.l_or_r_button = Button(self.player, bit(7))
            self.zl_or_zr_button = Button(self.player, bit(9))
            self.plus_or_minus_button = Button(self.player, bit(10))
            self.stick = Stick(self.player, is_left=False)

        self.left = Button(player, self.stick.left_key_bit)
        self.right = Button(player, self.stick.right_key_bit)
        self.up = Button(player, self.stick.up_key_bit)
        self.down = Button(player, self.stick.down_key_bit)

    @cached_property
    def sl_button(self):
        if self.parent is not None and self.parent.is_attached:
            return None
        return Button(self.player, bit(24))

    @cached_property
    def sr_button(self):
        if self.parent is not None and self.parent.is_attached:
            return None
        return Button(self.player, bit(25))


class StandardController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self.left_stick_button = Button(self.player, bit(4))
        self.right_stick_button = Button(self.player, bit(5))
        self.l_button = Button(self.player, bit(6))
        self.r_button = Button(self.player, bit(7))
        self.zl_button = Button(self.player, bit(8))
        self.zr_button = Button(self.player, bit(9))
        self.plus_button = Button(self.player, bit(10))
        self.minus_button = Button(self.player, bit(11))
        self.left_button = Button(self.player, bit(12))
        self.right_button = Button(self.player, bit(13))
        self.up_button = Button(self.player, bit(14))
        self.down_button = Button(self.player, bit(15))
        self.left_stick = Stick(self.player, is_left=True)
        self.right_stick = Stick(self.player, is_left=False)
        self.stick = self.left_stick
        self.left = Button(player, self.stick.left_key_bit, self.left_button.key_bits[0])
        self.right = Button(player, self.stick.right_key_bit, self.right_button.key_bits[0])
        self.up = Button(player, self.stick.up_key_bit, self.up_button.key_bits[0])
        self.down = Button(player, self.stick.down_key_bit, self.down_button.key_bits[0])


class SwitchProController(StandardController):
    """
    Yet to be implemented
    """
    pass


class DualJoyconController(StandardController):
    """
    Represents both Joycon controllers when attached to the console
    """
    def __init__(self, player):
        super().__init__(player)
        self.is_attached = True
        self.left_joycon = JoyconController(player, is_left=True, parent=self)
        self.right_joycon = JoyconController(player, is_left=False, parent=self)


class FreeDualJoyconController(DualJoyconController):
    """
    Represents both joycon controllers when detached from the console
    """
    def __init__(self, player):
        super().__init__(player)
        self.is_attached = False


class Button:
    """
    Represents a specific button on the Joycons
    """
    def __init__(self, player, *key_bits):
        self.player = player
        self.key_bits = key_bits

    @staticmethod
    def from_buttons(*buttons):
        """
        **THIS FUNCTION IS DEPRECATED**

        The function may be removed in a following release. Please construct a ButtonGroup instead.
        """
        warnings.warn("Usage of Button.from_buttons is deprecated, "
                      "construct a ButtonGroup instead", DeprecationWarning)
        return ButtonGroup(*buttons)

    @property
    def is_pressed(self):
        """
        :return: A boolean indicating whether the button is pressed
        :rtype: bool
        """
        return any_pressed(self.player, self)

    def __eq__(self, other):
        if not isinstance(other, Button):
            raise TypeError("Can only compare a Button to another Button")
        return self.key_bits == other.key_bits


class ButtonGroup(Button):
    def __init__(self, *buttons):
        if not buttons:
            raise TypeError("At least one Button must be passed")

        key_bits = [key_bit for button in buttons for key_bit in button.key_bits]
        super().__init__(buttons[0].player, *key_bits)

        self.buttons = buttons

    @property
    def pressed(self):
        return which_pressed(self.player, self.buttons)


class Stick:
    """
    Represents the analogue stick on the controller
    """
    def __init__(self, player, is_left):
        self.player = player
        self.is_left = is_left
        if is_left:
            self.left_key_bit = bit(16)
            self.right_key_bit = bit(18)
            self.up_key_bit = bit(17)
            self.down_key_bit = bit(19)
        else:
            self.left_key_bit = bit(20)
            self.right_key_bit = bit(22)
            self.up_key_bit = bit(21)
            self.down_key_bit = bit(23)

    @property
    def left(self):
        """
        :return: A boolean indicating whether or not the stick is in the left position
        :rtype: bool
        """
        return self.x < 0.0

    @property
    def right(self):
        """
        :return: A boolean indicating whether or not the stick is in the right position
        :rtype: bool
        """
        return self.x > 0.0

    @property
    def up(self):
        """
        :return: A boolean indicating whether or not the stick is in the up position
        :rtype: bool
        """
        return self.y > 0.0

    @property
    def down(self):
        """
        :return: A boolean indicating whether or not the stick is in the down position
        :rtype: bool
        """
        return self.y < 0.0

    @property
    def x(self):
        """
        The current x value of the analogue stick

        :return: The float value of the stick's x location.
        :rtype: float
        """
        _nx.hid_scan_input()
        keys_pressed = _nx.hid_keys_down(self.player.number - 1)
        if keys_pressed & self.left_key_bit:
            return -1.0
        if keys_pressed & self.right_key_bit:
            return 1.0
        return 0.0

    @property
    def y(self):
        """
        The current y value of the analogue stick
        
        :return: The float value of the stick's y location.
        :rtype: float
        """
        _nx.hid_scan_input()
        keys_pressed = _nx.hid_keys_down(self.player.number - 1)
        if keys_pressed & self.up_key_bit:
            return 1.0
        if keys_pressed & self.down_key_bit:
            return -1.0
        return 0.0


def any_pressed(player, *buttons: Button, refresh_input=True):
    if refresh_input:
        _nx.hid_scan_input()
    keys_pressed = _nx.hid_keys_down(player.number - 1)
    if len(buttons) == 0:
        return not keys_pressed == 0
    for button in buttons:
        for key_bit in button.key_bits:
            if keys_pressed & key_bit:
                return True
    return False


def is_pressed(player, button: Button, refresh_input=True):
    return any_pressed(player, button, refresh_input=refresh_input)


def which_pressed(player, *buttons: Button, refresh_input=True):
    if refresh_input:
        _nx.hid_scan_input()
    keys_pressed = _nx.hid_keys_down(player.number - 1)
    if not buttons:
        raise TypeError("At least one Button must be passed")
    return [button for button in buttons if keys_pressed & button.key_bit]
