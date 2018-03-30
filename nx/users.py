import _nx


class NoActiveUser(Exception):
    pass


class User:
    def __init__(self, id):
        if id is None:
            raise NoActiveUser("No active user, you need to launch and close a game prior to launching HBL.")
        self.id = id

    @property
    def is_active(self):
        return self.id == active_user.id


try:
    active_user = User(_nx.account_get_active_user())
except NoActiveUser:
    active_user = None
