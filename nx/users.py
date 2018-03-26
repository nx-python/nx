import _nx

from .utils.cached_property import cached_property


class NoActiveUser(Exception):
    pass


class User:
    def __init__(self, user_id):
        if user_id is None:
            raise NoActiveUser("No active user, you need to launch and close a game prior to launching HBL.")
        self.user_id = user_id

    @property
    def is_active(self):
        return self.user_id == active_user.user_id


@cached_property
def active_user():
    try:
        return User(_nx.account_get_active_user())
    except NoActiveUser:
        return None
