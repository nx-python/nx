import imgui

class Settings(object):
    def __init__(self, KEY_FUNC_COLOR, KEY_COLOR_BLACK, INPUT, KEY_COLOR_BGRAY, KEY_COLOR_LGRAY):
        # Button toggles: Default = False
        self.setting_toggle = False
        self.KEY_FUNC_COLOR = KEY_FUNC_COLOR
        self.KEY_COLOR_BLACK = KEY_COLOR_BLACK
        self.KEY_COLOR_BGRAY = KEY_COLOR_BGRAY
        self.KEY_COLOR_LGRAY = KEY_COLOR_LGRAY

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


    def srender(self):
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
        # TESTS
        """
        Give code for a long list, test long outputs        
        """
        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
        # Create a button "Long Output"
        if imgui.button("Long Output", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            self.input = "dpaste:>>070KVYA"
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        """
        Test SSL
        """
        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
        # Create a button "Test SSL"
        if imgui.button("Test SSL", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            self.input = "dpaste:>>0P6AH88"
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        """
        import this        
        """
        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
        # Create a button "Import this"
        if imgui.button("Import this", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            self.input = "dpaste:>>1441C4D"
        # push style
        imgui.pop_style_color(1)

        for i in range(3):
            imgui.same_line()
            self.placeholder()

        imgui.end_group()
