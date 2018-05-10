import nx


BOTW_TITLE_ID = 0x01007ef00011e000
SAVEGAME_PATH = '0/save_game.sav'


def main():
    nx.filesystem.SAVEDATA_BASE_PATH = ''
    nx.filesystem.ROMFS_BASE_PATH = ''

    botw = nx.titles[BOTW_TITLE_ID]

    try:
        with botw.savedata.open(SAVEGAME_PATH) as savegame:
            pass  # TODO: Modify the savegame
    except FileNotFoundError:
        print("No such file:", SAVEGAME_PATH)


if __name__ == '__main__':
    main()
