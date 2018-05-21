.. _getting_started-tutorial:

==================
Tutorial
==================

This quick tutorial will explain how you can use the nx package. We will start with a simple homebrew app that allows the user to backup the savedata of a selection of games.

Pre-requisites
------------------

1. A Switch device with access to the homebrew launcher **or** a compatible switch emulator. For help setting up the former, visit:
    * `Switch Hacks Guide <https://switch.hacks.guide/>`_
    * `Nintendo Homebrew Discord <https://discord.gg/C29hYvh>`_
    * `nx-python Discord <https://discord.gg/5Ga2Whf>`_

2. A device that you can develop Python applications on (preferably a desktop/laptop though it *is possible* on a mobile device)

3. An integrated development environment eg.
    * Visual Studio Code (Recommended)
    * PyCharm (Recommended)
    * Eclipse with PyDev
    * IDLE
    * Pydroid 3 (Android 4.4+)
    * Pythonista 3 (iOS 9.0+)

4. A basic understanding of Python 3.x+, there are many resources for learning Python including the ones below:
    * `Learn Python The Hard Way <https://learnpythonthehardway.org/>`_
    * `The Modern Python 3 Bootcamp <https://www.udemy.com/the-modern-python3-bootcamp/>`_
    * `SoloLearn <https://www.sololearn.com/Course/Python/>`_
    * `Python Discord <https://pythondiscord.com/>`_
    * `nx-python Discord <https://discord.gg/5Ga2Whf>`_

5. A Git installation for your operating system

To get started with nx-python, you will need to install the latest release of PyNX on your device. See :doc:`installation` for more information.

Starting development
------------------

To start developing, first clone the ``nx`` repository with the following command:

``git clone https://github.com/nx-python/nx.git``

There are three ways to run a Python program on your device.

Firstly, you can launch your IDE and open the freshly cloned repository as a workspace/project. Then open and edit ``test.py``. (Note: Controller input can not yet be tested on your development machine.)

**or**

You can test Python code on the Switch using a TCP REPL script located in ``examples/tcp_repl.py``.
You should use this script as your ``main.py`` to be able to run Python code from your PC to the switch.

After you launch PyNX on the device, connect to your switch via a TCP client on port 1337. The IP address can be found in your Switch's settings under the "Internet" tab.

On Linux you can connect with the following command:

``rlwrap cat | tee log.py | nc <SWITCH_IP> 1337``

This command will also log the inputs to a file called ``log.py``.

**or**

You can run an ftp server such as `ftpd <https://github.com/TuxSH/ftpd/tree/switch_pr>`_ (releases `here <https://www.switchbru.com/appstore/#/app/ftpd>`_) on your Switch and replace the main.py file using an FTP client.

A Simple Savedata Backup tool
------------------

Firstly, we need to import some libraries to begin work on our homebrew app, primarily the nx package.
We also want to show a selection menu to the user, so we should import the AnsiMenu utility class as well::

    import nx
    from nx.utils import AnsiMenu

Also, the main execution flow of every Python program (this does include Python homebrew apps) must be wrapped in a conditional clause as follows::

    if __name__ == '__main__':

Next, we create two lists. The names of the titles the user can select from are stored in ``title_name``. ``title_ids`` is used to store the title IDs of the games in the same order::

    # title IDs are hexadecimal numbers
    BOTW_TITLE_ID = 0x01007EF00011E000
    SMO_TITLE_ID = 0x0100000000010000
    title_names = ["The Legend of Zelda - Breath of the Wild", "Super Mario Odyssey"]
    title_ids = [BOTW_TITLE_ID, SMO_TITLE_ID]

Once our lists are set up, we can create a menu using the ``AnsiMenu`` library. This menu will allow the user to choose the game for which we will back up the save::

    select_title_menu = AnsiMenu(title_names)

The menu can now be rendered and queried using its ``query`` method::

    selected_index = select_title_menu.query()

The ``query`` method returns the index of the item selected by the user, which is now stored in the selected_index variable. As the order of the two lists we created earlier is equal, we can use the index to get the title ID from the title_ids list::

    selected_title_id = title_ids[selected_index]

``selected_title_id`` now contains the title ID of the selected title. We can now use this title ID to create a functional ``Title`` object::

    selected_title = nx.titles[selected_title_id]

Now we're interested in accessing and backing up the savedata of the title. To do this, we first need to mount the title's savedata. This is done by entering a new context with the title's savedata::

    with selected_title.savedata as savedata:

**Hint**: You can also use ``selected_title.savedata.mount``, ``selected_title.savedata.commit`` and ``selected_title.savedata.unmount``, however, using a with block might save you from a lot of potential headache, and is typically more simple and improves readability.
Now that the savedata filesystem of the title is mounted, you can backup its content simply by calling its ``backup`` method::

    savedata.backup()

This creates a backup of the savedata in ``/backups/savedata/{title_id}/``. You can also provide your own backup path like this::

    savedata.backup('/savedata_backups/{}/'.format(title_names[selected_index]))

When the ``with`` block ends, the savedata filesystem is automatically committed and unmounted.

That's it! Your code should now look like this::

    import nx
    from nx.utils import AnsiMenu


    if __name__ == '__main__':
        # title IDs are hexadecimal numbers
        BOTW_TITLE_ID = 0x01007EF00011E000
        SMO_TITLE_ID = 0x0100000000010000
        title_names = ["The Legend of Zelda - Breath of the Wild", "Super Mario Odyssey"]
        title_ids = [BOTW_TITLE_ID, SMO_TITLE_ID]

        select_title_menu = AnsiMenu(title_names)
        selected_title = select_title_menu.query()

        selected_title = title_ids[selected_title]
        selected_title = nx.titles[selected_title]

        with selected_title.savedata as savedata:
            savedata.backup('/savedata_backups/{}/'.format(title_names[selected_index]))

Congratulations, you have created your first Switch homebrew application in Python!