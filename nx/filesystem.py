import pathlib
import _nx

from . import users


SAVEDATA_BASE_PATH = 'save:/'
ROMFS_BASE_PATH = 'romfs:/'


mounted_romfs = None
mounted_savedata = None


def wait_for_romfs_mount():
    raise NotImplementedError  # TODO: implement wait_for_romfs_mount


def wait_for_savedata_mount():
    raise NotImplementedError  # TODO: implement wait_for_savedata_mount


def wait_for_romfs_unmount():
    raise NotImplementedError  # TODO: implement wait_for_romfs_unmount


def wait_for_savedata_unmount():
    raise NotImplementedError  # TODO: implement wait_for_savedata_unmount


class Partition:
    def __init__(self, base_path: str):
        self.base_path = pathlib.Path(base_path)

    def open(self, file_path: str, *args, **kwargs):
        return self.base_path.joinpath(file_path).open(*args, **kwargs)


class MountablePartition(Partition):
    def __init__(self, base_path):
        super().__init__(base_path)
        self.is_mounted = False

    def open(self, file_path: str, *args, **kwargs):
        if not self.is_mounted:
            self.mount()
        return super().open(file_path, *args, **kwargs)

    def mount(self):
        raise NotImplementedError

    def unmount(self):
        raise NotImplementedError


class RomFS(MountablePartition):
    def __init__(self, title):
        super().__init__(ROMFS_BASE_PATH)
        self.title = title

    @property
    def is_mounted(self):
        return self is mounted_romfs

    def mount(self):
        raise NotImplementedError  # TODO: implement RomFS.mount

    def unmount(self):
        raise NotImplementedError  # TODO: implement RomFS.unmount


class Savedata(MountablePartition):
    def __init__(self, title, user=None):
        super().__init__(SAVEDATA_BASE_PATH)
        self.title = title
        self.user = user if user is not None else users.active_user

    def mount(self):
        if self.is_mounted:
            return
        if self.user is None:
            raise users.NoActiveUser("No active user, you need to launch and close a game prior to launching HBL.")
        _nx.fs_mount_savedata("save", self.title.title_id, self.user.user_id)
        self.is_mounted = True

    def unmount(self):
        raise NotImplementedError  # TODO: implement Savedata.unmount
