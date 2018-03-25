import path
import _nx

from .utils.cached_property import cached_property


SAVEDATA_BASE_PATH = 'save:/'
ROMFS_BASE_PATH = 'romfs:/'


mounted_title = None  # TODO: check for a mounted title
mounted_romfs = None  # TODO: check for a mounted romfs
mounted_savedata = None  # TODO: check for a mounted savedata

def wait_for_title_mount():
    raise NotImplemented  # TODO: implement wait_for_title_mount

def wait_for_romfs_mount():
    raise NotImplemented  # TODO: implement wait_for_romfs_mount

def wait_for_savedata_mount():
    raise NotImplemented  # TODO: implement wait_for_savedata_mount

def wait_for_title_unmount():
    raise NotImplemented  # TODO: implement wait_for_title_unmount

def wait_for_romfs_unmount():
    raise NotImplemented  # TODO: implement wait_for_romfs_unmount

def wait_for_savedata_unmount():
    raise NotImplemented  # TODO: implement wait_for_savedata_unmount


class Partition:
    def __init__(self, base_path):
        self.base_path = base_path

    def open(self, file_path: str):
        return open(path.join(self.base_path, file_path))


class MountablePartition(Partition):
    def open(self, file_path: str):
        if not self.is_mounted:
            self.mount()
        return super().open(file_path)

    @cached_property
    def is_mounted(self):
        raise NotImplemented

    def mount(self):
        raise NotImplemented

    def unmount(self):
        raise NotImplemented


class RomFS(MountablePartition):
    def __init__(self, title):
        super().__init__(ROMFS_BASE_PATH)
        self.title = title

    @property
    def is_mounted(self):
        return self is mounted_romfs

    def mount(self):
        raise NotImplemented  # TODO: implement RomFS.mount

    def unmount(self):
        raise NotImplemented  # TODO: implement RomFS.unmount


class Savedata(MountablePartition):
    def __init__(self, title):
        super().__init__(SAVEDATA_BASE_PATH)
        self.title = title

    @property
    def is_mounted(self):
        return self is mounted_savedata

    def mount(self):
        raise NotImplemented  # TODO: implement Savedata.mount

    def unmount(self):
        raise NotImplemented  # TODO: implement Savedata.unmount
