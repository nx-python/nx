from .filesystem import RomFS, Savedata


class Title:
    def __init__(self, id: int):
        self.id = id
        self.romfs = RomFS(self)
        self.savedata = Savedata(self)
