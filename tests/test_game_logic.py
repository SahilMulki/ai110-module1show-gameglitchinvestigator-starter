from streamlit.testing.v1 import AppTest
from logic_utils import check_guess


def test_new_game_resets_state():
    at = AppTest.from_file("app.py").run()

    # Simulate some game progress
    at.session_state["attempts"] = 5
    at.session_state["history"] = [10, 20, 30]
    at.session_state["status"] = "lost"
    at.session_state["game_count"] = 0
    at.run()

    # Click "New Game"
    at.button[1].click().run()

    assert at.session_state["attempts"] == 1
    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []
    assert at.session_state["game_count"] == 1


def test_new_game_generates_valid_secret():
    at = AppTest.from_file("app.py").run()
    at.button[1].click().run()

    secret = at.session_state["secret"]
    assert isinstance(secret, int)
    assert 1 <= secret <= 100


def test_new_game_after_win_allows_playing():
    at = AppTest.from_file("app.py").run()

    at.session_state["status"] = "won"
    at.run()

    at.button[1].click().run()

    assert at.session_state["status"] == "playing"


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)  #FIX: Was asserting result == "Win" but check_guess returns a tuple; unpacked outcome to compare correctly
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)  #FIX: Was asserting result == "Too High" but check_guess returns a tuple; unpacked outcome to compare correctly
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)  #FIX: Was asserting result == "Too Low" but check_guess returns a tuple; unpacked outcome to compare correctly
    assert outcome == "Too Low"
