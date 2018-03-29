from .filesystem import RomFS, Savedata


class Title:
    def __init__(self, title_id: int):
        self.title_id = title_id
        self.romfs = RomFS(self)
        self.savedata = Savedata(self)
