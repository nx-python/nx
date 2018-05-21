.. _getting_started-installation:

To run Python code on your Switch, or a Switch emulator, you need to use PyNX. Here's how to get started.

==================
Installing PyNX
==================

Switch
------------------
**You need a Switch with access to the Homebrew Menu in order to run PyNX on your Switch.**

1. Insert the SD card into your development device.
2. Copy the content of the `zip release of PyNX <https://github.com/nx-python/PyNX/releases>`_ into the ``/switch`` directory on your SD card.
3. Edit the main.py file within the extracted contents.
4. Insert the SD card back into the Switch.
5. Run PyNX from the Homebrew Menu.

Yuzu
------------------
1. Install the Yuzu emulator if you haven't already. You can build it from `source <https://github.com/yuzu-emu/yuzu>`_ or get a pre-compiled build from `their website <https://yuzu-emu.org/downloads/>`_.
2. Run Yuzu at least once so that it can create default directories.
3. Build PyNX from `source <https://github.com/nx-python/PyNX>`_, or download a release build from `here <https://github.com/nx-python/PyNX/releases>`_.
4. Extract the nx-python files into Yuzu's sdmc directory.
    - On Windows this directory is located in ``C:/Users/{USER}/AppData/Roaming/yuzu/sdmc``.
    - On Linux and OS X it is located in ``~/.local/share/yuzu-emu/``.
5. Edit the main.py file as you wish, then launch the PyNX.nro with Yuzu.

RyujiNX
------------------
<todo>
