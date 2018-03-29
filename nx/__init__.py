import _nx

from .audio import *
from .controllers import *
from .title import *
from .players import *


_nx.account_initialize()


p1 = Player(1)
p2 = Player(2)
p3 = Player(3)
p4 = Player(4)


class _Titles(dict):
    def __getitem__(self, title_id):
        return Title(title_id)


titles = _Titles()
