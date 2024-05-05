# This program is for Business Game, How we can create an environment virtually like on board, pieces and dice
import random

class Business():
    def __init__(self):
        print("Welcome to Virtual Business game by Python, PVM hopes that you enjoy this game")

    def add_players(players_list):
        players_to_be_added = input("Enter the players, you want to add separated by comma ',' :").split(",")
        players_list.extend(players_to_be_added)
        return players_list

    def del_players(players_list):
        players_to_be_del = input("Enter the players, you want to delete separated by comma ',' : ").split(",")
        for player in players_to_be_del:
            if player not in players_list:
                print("Check the option you entered")
            else:
                players_list.remove(player)
        return players_list

    def roll_dice():
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        print(f"dice 1 rolled {dice_1}\n dice 2 rolled {dice_2}")
        total = dice_2 + dice_1
        return total





