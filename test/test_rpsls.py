from src.RPSLS import get_computer_action,past_actions

def test_rpsls01():
    last_play = {"Victory":0,"rival_action":3,"computer_action":4}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 3

def test_rpsls02():
    last_play = {"Victory":2,"rival_action":4,"computer_action":3}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 2    

def test_rpsls03():
    last_play = {"Victory":0,"rival_action":1,"computer_action":5}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 1

def test_rpsls04():
    last_play = {"Victory":2 ,"rival_action":0,"computer_action":4}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 3  

def test_rpsls05():
    last_play = {"Victory":0,"rival_action":3,"computer_action":1}
    past_actions.append(last_play)
    computer_action = get_computer_action()
    assert computer_action == 3    