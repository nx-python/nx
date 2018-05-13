def account_initialize():
    """
    Yet to be implemented
    """
    pass


def fs_mount_savedata(name: str, title_id: int, user_id: int):
    """
    Yet to be implemented
    """
    pass


def fsdev_unmount_device(mountpoint: str):
    """
    Yet to be implemented
    """
    pass


def fsdev_commit_device(mountpoint: str):
    """
    Yet to be implemented
    """
    pass


def hid_scan_input():
    """
    Yet to be implemented
    """
    pass


def hid_keys_down(player_id: int):
    if player_id < 0 or player_id > 7:
        raise ValueError
    return 0


def hid_get_touches():
    return ((640, 360, 10, 10, 0),)


def account_get_active_user():
    """
    Yet to be implemented
    """
    return 0
