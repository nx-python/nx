.. _getting_started-installation:

==================
Installating nx-python
==================

<placeholder: How to install nx-python>

Switch
------------------
**You require a Switch with access to the Homebrew Launcher**

1. Insert the SD card into your development device.
2. Copy the content of the `zip release <https://github.com/nx-python/PyNX/releases>`_ into the ``/switch`` directory on your SD card.
3. Edit the main.py file within the extracted contents.
4. Insert the SD card back into the Switch.
5. Run PyNX from the Homebrew launcher

Yuzu
------------------
1. Install Yuzu emulator from their `Github repo <https://github.com/yuzu-emu/yuzu>`_ or `webpage <https://yuzu-emu.org/>`_.
2. Run Yuzu at least once so that it can create default directories.
3. Build an PyNX release, or download one from `here <https://github.com/nx-python/nx/releases>`_.
4. Extract the nx-python files into Yuzu's sdmc directory.
    - On Windows this directory is located in ``C:/Users/<USER>/AppData/Roaming/yuzu/sdmc``
    - <todo: add location for other operating systems>
5. Edit the main.py file, and open PyNX.nro in Yuzu
6. Your code should run successfully in the Yuzu emulator.


RyujiNX
------------------