import imgui

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


class Settings(object):
    def __init__(self, KEY_FUNC_COLOR, KEY_COLOR_BLACK, INPUT):
        # Button toggles: Default = False
        self.setting_toggle = False
        self.KEY_FUNC_COLOR = KEY_FUNC_COLOR
        self.KEY_COLOR_BLACK = KEY_COLOR_BLACK

        self.input = INPUT

        # Set button size
        self.BTN_WIDTH = 194
        self.BTN_HEIGHT = 58

    def toggle(self):
        """
        Button toggle
        :return:
        """
        if self.setting_toggle:
            self.setting_toggle = False
        else:
            self.setting_toggle = True

    def placeholder(self):
        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BLACK)
        # Create a button "PLACEHOLDER"
        if imgui.button("...", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)


    def render(self):
        # Create a GUI group
        imgui.begin_group()

        """
        NEW ROW STARTS HERE ROW #1
        """
        for i in range(5):
            self.placeholder()
            imgui.same_line()
        self.placeholder()

        """
        NEW ROW STARTS HERE ROW #2
        """
        for i in range(5):
            self.placeholder()
            imgui.same_line()
        self.placeholder()

        """
        NEW ROW STARTS HERE ROW #3
        """

        for i in range(5):
            self.placeholder()
            imgui.same_line()
        self.placeholder()

        """
        NEW ROW STARTS HERE ROW #4
        """

        for i in range(5):
            self.placeholder()
            imgui.same_line()
        self.placeholder()

        """
        NEW ROW STARTS HERE ROW #5
        """
        for i in range(5):
            self.placeholder()
            imgui.same_line()
        self.placeholder()

        imgui.end_group()
