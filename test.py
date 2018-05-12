import nx
import shutil


BOTW_TITLE_ID = 0x01007ef00011e000
SAVEGAME_PATH = '0/game_data.sav'
OUTPUT_PATH = 'botw_0_game_data.sav'


def main():
    nx.filesystem.SAVEDATA_BASE_PATH = ''
    nx.filesystem.ROMFS_BASE_PATH = ''

    botw = nx.titles[BOTW_TITLE_ID]  # get botw Title object

    try:
        with botw.savedata as savedata:  # mount BotW savedata partition
            with savedata.open(SAVEGAME_PATH) as savegame_file:  # open save game file
                with open(OUTPUT_PATH, 'w') as destination_file:  # open destination file on SD card
                    shutil.copyfileobj(savegame_file, destination_file)  # copy file from savedata to SD card
    except FileNotFoundError:
        print("No such file:", SAVEGAME_PATH)


if __name__ == '__main__':
    main()
