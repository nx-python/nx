# MAIN REPO https://github.com/Annihilator708/PyNX_Terminal

import imgui
import imguihelper
import os
import _nx
import sys
from io import StringIO
import contextlib
import logging

from nx.utils.terminal_src.screen import Screen
from nx.utils.terminal_src.keyboard import Keyboard
from nx.utils.terminal_src.python import Python
from nx.utils.terminal_src.menu import Settings
from nx.utils.terminal_src.utils import Utils

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

@contextlib.contextmanager
def stderrIO(stderr=None):
    old = sys.stdout
    if stderr is None:
        stderr = StringIO()
    sys.stderr = stderr
    yield stderr
    sys.stderr = old

class Terminal(Screen, Keyboard):
    def __str__(self):
        return "Terminal for the switch, made by PuffDip"

    def __init__(self):
        # Debug setting && Version Number
        self.DEBUG = False
        self.version_number = '0.2A'

        # Useful static variables
        self.currentDir = os.getcwd()
        self.CONSOLE_TEXT = "Python {} on Nintendo Switch\n\n>>>".format(sys.version)
        # A check to see if the terminal just started or not
        self.just_booted = True

        # Set log settings
        if self.DEBUG:
            logging.basicConfig(filename='lib/python3.5/nx/utils/terminal.log',
                                format='%(levelname)s:%(message)s',
                                level=logging.DEBUG)
        else:
            logging.basicConfig(filename='terminal.log',
                                format='%(levelname)s:%(message)s',
                                level=logging.ERROR)

        # Initialize class as super
        Screen.__init__(self)
        # A storage for our history
        self.cli_history = []
        Keyboard.__init__(self, self.cli_history, logging)

        # Initialize class as object
        self.python = Python(logging)
        self.utils = Utils(logging)

        # Initialize menu's, usually a class object
        # Those menus are most of the time static
        self.settings = Settings(self.KEY_COLOR_LGRAY, self.KEY_COLOR_BLACK, self.input)


    def main(self):
        """
        This is the main loop.
        Most action happens here
        """
        # This is the loop I was talking about
        while True:
            # Look for any user input
            self.renderer.handleinputs()

            # Create a new frame
            imgui.new_frame()
            # Get screen width and height
            self.width, self.height = self.renderer.io.display_size
            # Set the frame as big as the screen resolution
            imgui.set_next_window_size(self.width, self.height)
            # Put the frame in the top left corner
            imgui.set_next_window_position(0, 0)

            # Create a window in the frame we created ( Ignore pep8 for this line)
            imgui.begin("", flags=imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_SAVED_SETTINGS)
            # Version placeholder
            imgui.text("PyNx Terminal By PuffDip" + " - V" + str(self.version_number))

            # This check looks if any menu is open
            # If so the terminal rescales so the menu fits on screen
            if \
                    self.keyboard_toggled or\
                    self.settings.setting_toggle:
                # end check
                # Set the region so a new menu can fit
                imgui.begin_child("region", -5, -430, border=True)
            else:
                # Set terminal fullscreen if no menu has been found
                imgui.begin_child("region", -5, -110, border=True)

            # Show interpreter output on screen
            # If this is the first time the console need to show text
            if self.just_booted:
                # set boot bool to false
                if len(self.input) > 0:
                    self.just_booted = False
                # Show version number
                imgui.text(self.CONSOLE_TEXT)
            else:
                if self.cli_history:
                    imgui.text("{}\n\n>>>\n{}".format("\n".join(self.cli_history), self.input))
                else:
                    imgui.text(">>>\n{}".format(self.input))

            # Make sure the screen stays fullscreen
            imgui.end_child()

            """
            If the setting menu not is selected, most likely the user is in his keyboard layout
            We first want to check if the user is using the setting menu. After that we check
            if the user uses its keyboard. If so we render the keyboard.
            """
            # Check if the setting page is toggled
            if not self.settings.setting_toggle:
                    # Render keyboard
                    self.render()
            # If the setting page is active show the setting page instead of rendering the keyboard
            else:
                self.settings.render()

            # Command line
            imgui.text("Keyboard: {} | Shift: {} | SYS: {}".format(self.keyboard_toggled, self.CAPS, self.SYS))

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
            # Create a button "Import"
            if imgui.button("Import", width=200, height=60):
                # Toggle Keyboard if not already
                if not self.keyboard_toggled:
                    self.keyboard_toggled = True
                #self.input = "https://pastebin.com/"
                self.input = "dpaste:>>"
            # push style
            imgui.pop_style_color(1)

            imgui.same_line()

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
            # Create a button "Export"
            if imgui.button("Export", width=200, height=60):
                export_check = "".join(self.utils.export(self.cli_history))
                self.cli_history.append(export_check)

            # push style
            imgui.pop_style_color(1)

            imgui.same_line()

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BLACK)
            # Create a button "Cursor"
            if imgui.button("...", width=200, height=60):
                pass # TODO Import a cursor method
            # push style
            imgui.pop_style_color(1)

            # Create the keyboard toggle button
            imgui.same_line()

            self.toggleKeyboard()
            # If settings was already opened close setting page
            if self.keyboard_toggled and self.settings.setting_toggle:
                self.settings.setting_toggle = False

            imgui.same_line()

            # Give a style to the button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_LGRAY)
            # Create a button "Confirm" if the input from the user is higher then 0
            if imgui.button("Confirm", width=200, height=60) and len(self.input) > 0:
                # If pastebin is used
                if self.input.startswith("dpaste:>>"):
                    # Make a usable url
                    url_redirecter = self.input.split(sep=":>>")[1]
                    # Clear user input
                    # generate url
                    url = "http://dpaste.com/" + url_redirecter + ".txt"
                    # Start to fetch the data
                    self.input = self.utils.import_url(url)
                else:
                    # Execute user command
                    out, err, exc = self.python.execute(self.input)
                    # Append user command to history
                    self.input += "\n"
                    self.cli_history.append(self.input)
                    # Check whatever the result was of the command
                    if out:
                        self.input = out
                    if err:
                        self.input = err
                    if exc:
                        self.input = exc
                    # Append result to history
                    self.cli_history.append(self.input)
                    # Clear variable to get used once more
                    self.input = ""

            # Push style of the button
            imgui.pop_style_color(1)

            # On the same line we want our next object
            imgui.same_line()

            # Create a style for a new button
            imgui.push_style_color(imgui.COLOR_BUTTON, *self.KEY_COLOR_BGRAY)
            # Create a button "Settings"
            if imgui.button("S", width=40, height=40):
                # If the keyboard was toggled turn it off
                if self.keyboard_toggled:
                    self.keyboard_toggled = False
                # Finally render the settings
                self.settings.toggle()
            # Push style of the button
            imgui.pop_style_color(1)

            imgui.end()
            imgui.render()
            self.renderer.render()

        # This function is needed else the switch crashes
        self.renderer.shutdown()
