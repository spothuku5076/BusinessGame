# test_business.py
from unittest import mock

import pytest
from unittest.mock import patch
from business_scripts.business import Business


def test_add_players():
    players_list = []
    # Patching input to provide predefined values
    with patch('builtins.input', side_effect=['Naveen,Pavan']):
        Business.add_players(players_list)
    assert players_list == ['Naveen', 'Pavan']

def test_del_players():
    players_list = ['Naveen', 'Lalitesh', 'Pavan']
    # Patching input to provide predefined values
    with patch('builtins.input', side_effect=['Lalitesh']):
        Business.del_players(players_list)
    assert players_list == ['Naveen', 'Pavan']

@patch('random.randint')
def test_roll_dice(mock_randint):
    mock_randint.side_effect = [3, 4]  # Mocking random.randint to return predefined values
    assert Business.roll_dice() == 7
