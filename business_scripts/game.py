# welcome to the business game
from business import Business as _business_
from business_flags import flags
import time


# flags.IS_MODIFIED = True
players_list = []
# print(flags.PLAYERS_NOT_MODIFIED)


def modify(IS_MODIFIED):
    while flags.IS_MODIFIED:
        add_delete_choice = input("Select 'add' to add the players, 'del' to delete the players and 'fin' to finalize "
                                  "the players : ").lower()
        if add_delete_choice == "add":
            _business_.add_players(players_list)
            flags.PLAYERS_NOT_MODIFIED = False
            print(f"The players are {players_list}")
        elif add_delete_choice == "del":
            _business_.del_players(players_list)
            print(f"The players are {players_list}")
        elif add_delete_choice == "fin":
            flags.IS_MODIFIED = False
            # print(f"flags.IS_MODIFIED flag is {flags.IS_MODIFIED}")
            break
        else:
            print("please check the option you've entered")


def player_finalization():
    while flags.PLAYERS_NOT_MODIFIED:
        modify_players = input("Do you want to modify players [y/n] :  ").lower()
        if modify_players == "y":

            while flags.IS_MODIFIED:
                # print(f"flags.IS_MODIFIED flag is {flags.IS_MODIFIED}")
                modify(flags.IS_MODIFIED)
                if flags.IS_MODIFIED:
                    flags.IS_MODIFIED = False
            flags.PLAYERS_NOT_MODIFIED = False
        elif modify_players == "n":
            flags.PLAYERS_NOT_MODIFIED = False
        else:
            print("please check the option you've entered")
    return players_list


while flags.GAME_STARTED:
    players_list = input("Enter the name of players who wants to play the game separated by comma ',' :").split(",")
    player_finalization()
    print(f"The final players are {players_list}")
    time.sleep(3)
    _business_.roll_dice()

    flags.GAME_STARTED = False
