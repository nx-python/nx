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
    def __init__(self, KEY_FUNC_COLOR, INPUT):
        # Button toggles: Default = False
        self.setting_toggle = False
        self.KEY_FUNC_COLOR = KEY_FUNC_COLOR

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

    def render(self):
        # Create a GUI group
        imgui.begin_group()

        """
        NEW ROW STARTS HERE ROW #1
        """

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)





        """
        NEW ROW STARTS HERE ROW #2
        """

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)





        """
        NEW ROW STARTS HERE ROW #3
        """

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)






        """
        NEW ROW STARTS HERE ROW #4
        """

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)





        """
        NEW ROW STARTS HERE ROW #5
        """

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.same_line()

        # Give a style to the button
        imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_FUNC_COLOR)
        # Create a button "PLACEHOLDER"
        if imgui.button("PLACEHOLDER", width=self.BTN_WIDTH, height=self.BTN_HEIGHT):
            # Execute code when button is pressed
            pass  # PLACEHOLDER
        # push style
        imgui.pop_style_color(1)

        imgui.end_group()
