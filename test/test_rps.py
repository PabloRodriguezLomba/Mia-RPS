from src.RPS import get_computer_action,past_actions

def test_rps01():
    last_play = {"Victory":0,"rival_action":0,"computer_action":2}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 0

def test_rps02():
    last_play = {"Victory":2,"rival_action":1,"computer_action":0}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 2


def test_rps03():
    last_play = {"Victory":0,"rival_action":1,"computer_action":0}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 1        