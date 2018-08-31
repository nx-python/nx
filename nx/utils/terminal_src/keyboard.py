import imgui

class Keyboard(object):
    def colorToFloat(self, t):
        """
        Used to convert RGB to a float value
        :param t: Tuple (R,G,B)
        :return: Floats (0.0, 0.0, 0.0)
        """
        nt = ()
        for v in t:
            nt += ((1 / 255) * v,)
        return nt

    def __init__(self, cli_history, logger):
        # Button toggles: Default = False
        self.keyboard_toggled = False

        # Set logger
        self.logger = logger

        # Assign CLI History
        self.cli_history = cli_history

        # Define keyboard layout
        # Layout 1
        self.keyboard = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['TAB', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'],
            ['SYS', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '\\'],
            ['SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
        ]
        # Layout 2
        self.sys_keyboard = [
            ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
            ['TAB', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}'],
            ['SYS', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', '"', '|'],
            ['SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?']
        ]

        # Color based on floats
        # (r, g, b)
        self.KEY_COLOR_ORANGE = self.colorToFloat((230, 126, 34))
        self.KEY_COLOR_BLACK = self.colorToFloat((0, 0, 0))
        self.KEY_COLOR_BGRAY = self.colorToFloat((32, 32, 32))
        self.KEY_COLOR_LGRAY = self.colorToFloat((64, 64, 64))

        # User input, what the user types on his keyboard
        self.input = ""

        # Button toggles: Default = False
        self.keyboard_toggled = False
        self.setting_toggle = False
        self.setting_toggle = False
        self.CAPS = False
        self.SYS = False
        self.TAB = False

    # Check if shift key is used
    def shift_key(self):
        if self.CAPS:
            self.CAPS = False
        else:
            self.CAPS = True

    # Check if special character key is used
    def sys_key(self):
        if self.SYS:
            self.SYS = False
        else:
            self.SYS = True

    def keyboard_key(self, key:str, same_line=False, *, default:str=None):
        """
        This is a multi functional function.
        Key: The key of the key
        same_line: True or False, for if the next key should be on the same line
        optional:
        color: set color
        """
        if same_line:
            imgui.same_line()

        if self.CAPS:
            key = key.upper()

        try:
            if default == 'SHIFT' or default == 'SYS' or default == 'TAB':
                imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BGRAY)
            else:
                imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)

            #imgui.push_style_color(imgui.COLOR_TEXT, *self.KEY_COLOR_ORANGE)
            if imgui.button(key, width=80, height=60):
                if default is None:
                    if self.input == '':
                        self.input = key
                    else:
                        self.input = self.input + key
                elif default == 'SHIFT':
                    self.shift_key()
                elif default == 'SYS':
                    self.sys_key()
                elif default == 'TAB':
                    if self.TAB == False:
                        self.input = self.input.replace('>>>', '>>>\n')
                        self.TAB = True
                    self.input = self.input + '    '
            imgui.pop_style_color(1)
        except Exception as e:
            self.logger.error(e)

    # Toggle keyboard on or off
    def toggleKeyboard(self):
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
        if imgui.button("Keyboard", width=200, height=60):
            if self.keyboard_toggled:
                self.keyboard_toggled = False
            else:
                self.keyboard_toggled = True
        imgui.pop_style_color(1)

    def krender(self):
        # After that check if the keyboard is open
        if self.keyboard_toggled:
            # If the keyboard is open we want to generate a imgui group so we can render the keyboard
            imgui.begin_group()

            # Check whatever layout is selected
            # The keyboard adapt to its layout
            if self.SYS:
                keyboard = self.sys_keyboard
            else:
                keyboard = self.keyboard

            # Here we "Compile" our keyboard. This is just magic
            for rows in keyboard:
                for row in rows:
                    if row == 'TAB' or row == 'SYS' or row == 'SHIFT':
                        self.keyboard_key(row, False, default=row)
                    elif row == '`' or row == '~':
                        self.keyboard_key(row, False)
                    else:
                        self.keyboard_key(row, True)

            # I have space left on the same line
            # I fill this space with a enter key
            imgui.same_line()

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BGRAY)
            # Create a button "Enter"
            if imgui.button("ENTER", width=175, height=60):
                # Execute code when button is pressed
                self.input = self.input + "\n"
            # push style
            imgui.pop_style_color(1)

            # Notice there is no "imgui.same_line()" here. This is a new line

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BGRAY)
            # Create a button "SPACE"
            if imgui.button("SPACE", width=970, height=50):
                # Execute code when button is pressed
                self.input = self.input + " "
            # push style
            imgui.pop_style_color(1)

            # I want to use the space after the spacebar for clearing options
            # So on the same line we create two buttons
            imgui.same_line()

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BGRAY)
            # Create a button "CLEAR"
            if imgui.button("CLEAR", width=80, height=50):
                # Execute code when button is pressed
                self.cli_history = []
                self.input = ""
            # push style
            imgui.pop_style_color(1)

            # Again same line
            imgui.same_line()

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BGRAY)
            # Create a button "BACKSPACE"
            if imgui.button("BACKSPACE", width=150, height=50):
                # Execute code when button is pressed
                self.input = self.input[:-1]
            # push style
            imgui.pop_style_color(1)
            imgui.end_group()
