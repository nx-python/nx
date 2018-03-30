def account_initialize():
    pass


def fs_mount_savedata(name: str, title_id: int, user_id: int):
    pass


def hid_keys_pressed(player_id: int):
    if player_id < 0 or player_id > 7:
        raise ValueError
    return 0


def account_get_active_user():
    return 0
