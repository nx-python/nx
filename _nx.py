def account_initialize():
    """Initializes the account service."""
    pass


def fs_mount_savedata(name: str, title_id: int, user_id: int):
    """
    Mounts a savedata filesystem.

    Parameters
    ----------
    name: ``str``
        The name of the filesystem, typically 'save'.
    title_id: int
        The title ID of the title whose savadata filesystem to mount.
        Should be a hexadecimal number.
    user_id: int
        The user ID of the user whose savedata filesystem to mount.
    """
    pass


def fsdev_unmount_device(mountpoint: str):
    """
    Unmounts a device, such as a filesystem.

    Parameters
    ----------
    mountpoint: str
        The mountpoint or name on which the device is mounted.
    """
    pass


def fsdev_commit_device(mountpoint: str):
    """Unmounts a device, such as a filesystem.

    Parameters
    ----------
    mountpoint: str
        The mountpoint or name on which the device is mounted.
    """
    pass


def hid_scan_input():
    """Scans for new input signals."""
    pass


def hid_keys_down(player_id: int):
    """Checks which keys are pressed that haven't been
    pressed in the previous frame.

    Example
    -------
    Check if button with given key_code is pressed: ::

        def is_pressed(key_code: int):
            return _nx.hid_keys_down() & (1 << key_code)

    For instance, to check if the A button is pressed: ::

        A_BUTTON = 0
        if is_pressed(A_BUTTON):
            # ...
    """
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
