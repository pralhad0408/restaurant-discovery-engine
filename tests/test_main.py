from main import get_menu_choice, main, discover_restaurants
from restaurant import Restaurant

def test_get_menu_choice_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "2")

    result = get_menu_choice()

    assert result == "2"

def test_get_menu_choice_retries_invalid_input(monkeypatch):
    responses = iter(["hello", "7", "3"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(responses)
    )

    result = get_menu_choice()

    assert result == "3"

def test_main_multiple_selections(monkeypatch, capsys):
    responses = iter(["2", "3", "4"])
    expected_messages = [
        "You selected: Help me decide",
        "You selected: Surprise me",
        "You selected: Exit",
    ]

    monkeypatch.setattr(
        "builtins.input", 
        lambda prompt: next(responses)
    )

    monkeypatch.setattr(
        "main.csv_loader",
        lambda: []
    )

    main()

    captured = capsys.readouterr()

    for message in expected_messages:
        assert message in captured.out

    assert captured.out.count("Welcome to Kya Khau RDE!") == 1

def test_discover_restaurants_by_cuisine(monkeypatch, capsys, sample_restaurants):

    expected_messages = "Found 2 matching restaurants"

    monkeypatch.setattr("builtins.input", lambda prompt: "Italian")

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr()

    assert expected_messages in captured.out

def test_discover_restaurants_by_cuisine_no_matches(monkeypatch, capsys, sample_restaurants):
    expected_message = "Found 0 matching restaurants"

    monkeypatch.setattr("builtins.input", lambda prompt: "Mexican")

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr()

    assert expected_message in captured.out