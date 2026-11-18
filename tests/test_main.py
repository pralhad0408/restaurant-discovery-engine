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
    expected_message = "No matches found. Would you like to try another cuisine?"

    responses = iter(["Mexican", "2"])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr()

    assert expected_message in captured.out

def test_discover_restaurants_by_cuisine_retry_loop(monkeypatch, capsys, sample_restaurants):
    responses = iter(["Mexican", "1", "Italian"])
    
    expected_messages = [
        "No matches found. Would you like to try another cuisine?",
        "Found 2 matching restaurants",
    ]

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr()

    for message in expected_messages:
        assert message in captured.out

def test_discover_restaurants_invalid_retry_choice(monkeypatch, capsys, sample_restaurants):
    responses = iter(["Mexican", "7", "1", "Italian"])
    prompts = []

    def mock_input(prompt):
        prompts.append(prompt)
        return next(responses)

    monkeypatch.setattr("builtins.input", mock_input)

    expected_messages = [
        "No matches found. Would you like to try another cuisine?",
        "Invalid input. Choose either 1 or 2.",
        "Found 2 matching restaurants",
    ]

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr()

    for message in expected_messages:
        assert message in captured.out

    assert prompts == [
        "What cuisine are you craving? ",
        "Choose an option: ",
        "Choose an option: ",
        "What cuisine are you craving? ",
    ]