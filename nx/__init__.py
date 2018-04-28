import _nx

from .players import *
from .audio import *
from .controllers import Button
from .touch import screen
from .title import *


_nx.account_initialize()


class _Titles:
    def __init__(self):
        self._titles = {}

    def __getitem__(self, title_id):
        if title_id in self._titles:
            return self._titles[title_id]
        _title = Title(title_id)
        self._titles[title_id] = _title
        return _title


titles = _Titles()
