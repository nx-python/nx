from .filesystem import RomFS, Savedata


class Title:
    def __init__(self, title_id: int):
        self.title_id = title_id
        self.romfs = RomFS(self)
        self.savedata = Savedata(self)


class _Titles(dict):
    def __getitem__(self, title_id):
        _title = Title(title_id)


_titles = _Titles()


def __getitem__(title_id):
    return _titles[title_id]
