import pathlib
import _nx

from . import users


SAVEDATA_BASE_PATH = 'save:/'
ROMFS_BASE_PATH = 'romfs:/'


mounted_romfs = None
mounted_savedata = None


class FileSystem:
    def __init__(self, base_path: str):
        self.base_path = pathlib.Path(base_path)

    def open(self, file_path: str, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None):
        return self.base_path.joinpath(file_path).open(mode=mode, buffering=buffering,
                                                       encoding=encoding, errors=errors,
                                                       newline=newline)


class MountableFileSystem(FileSystem):
    """
    Represents a File System that is able to be mounted. The class provides methods for mounting and manipulating the filesystem.
    """
    def __init__(self, base_path):
        super().__init__(base_path)

    @property
    def is_mounted(self):
        """
        Yet to be implemented
        """
        raise NotImplementedError

    def open(self, file_path: str, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None):
        if not self.is_mounted:
            self.mount()
        return super().open(file_path, mode=mode, buffering=buffering, encoding=encoding,
                            errors=errors, newline=newline)

    def mount(self):
        """
        Yet to be implemented
        """
        raise NotImplementedError

    def commit(self):
        """
        Yet to be implemented
        """
        raise NotImplementedError

    def unmount(self):
        """
        Yet to be implemented
        """
        raise NotImplementedError

    def __enter__(self):
        self.mount()

    def __exit__(self):
        self.commit()
        self.unmount()


class RomFS(MountableFileSystem):
    """
    The filesystem of a ROM
    """
    def __init__(self, title):
        super().__init__(ROMFS_BASE_PATH)
        self.title = title

    @property
    def is_mounted(self):
        """
        :return: Whether the specific RomFS is mounted
        :rtype: bool
        """
        return self is mounted_romfs

    def mount(self):
        """
        Yet to be implemented
        """
        raise NotImplementedError  # TODO: implement RomFS.mount

    def unmount(self):
        """
        Unmounts a mounted ROM filesystem
        """
        _nx.fsdev_unmount_device('romfs')

    def __exit__(self):
        self.unmount()


class Savedata(MountableFileSystem):
    """
    Represents a game's savedata on a specified MountableFileSystem.
    """
    def __init__(self, title, user=None):
        super().__init__(SAVEDATA_BASE_PATH)
        self.title = title
        self.user = user if user is not None else users.active_user

    @property
    def is_mounted(self):
        """
        :return: Whether the savedata itself has been mounted.
        :rtype: bool
        """
        return self is mounted_savedata

    def mount(self):
        """
        Mounts the savedata.
        """
        if self.is_mounted:
            return
        if self.user is None:
            raise users.NoActiveUser("No active user, you need to launch and "
                                     "close a game prior to launching HBL.")
        _nx.fs_mount_savedata('save', self.title.id, self.user.id)

    def commit(self):
        _nx.fsdev_commit_device('save')

    def unmount(self):
        """
        Unmounts the savedata.
        """
        _nx.fsdev_unmount_device('save')
