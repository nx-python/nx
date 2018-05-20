.. _getting_started-tutorial:

==================
Tutorial
==================

This quick tutorial will explain how you can use the nx package. We will start with a simple homebrew app that allows the user to backup the savedata of a selection of games.

Pre-requisites
------------------
* A Switch device or Switch Emulator
* PyNX installed on said device

The Code
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