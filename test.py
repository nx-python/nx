import nx


BOTW_TITLE_ID = 0x01007ef00011e000
SAVEGAME_PATH = '0/save_game.sav'


def main():
    botw = nx.titles[BOTW_TITLE_ID]

    if not nx.p1.any_pressed():
        print("no button pressed")

    try:
        with botw.savedata.open(SAVEGAME_PATH) as savegame:
            pass
    except FileNotFoundError:
        print("No such file:", SAVEGAME_PATH)


if __name__ == '__main__':
    main()
