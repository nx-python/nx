from imgui.integrations.nx import NXRenderer

class Screen(object):
    def __str__(self):
        return "Our screen objects will be created here"

    def __init__(self):
        # Our render object
        self.renderer = NXRenderer()
