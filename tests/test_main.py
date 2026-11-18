from main import get_menu_choice, main, discover_restaurants, display_restaurants
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

    responses = iter(["1", "Italian", "4", "5"])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out

    assert "2 matching restaurants." in captured
    assert "1. Mario's" in captured
    assert "2. Luigi's" in captured
    assert "Sakura" not in captured

def test_discover_restaurants_by_cuisine_no_matches(monkeypatch, capsys, sample_restaurants):

    responses = iter(["1", "Mexican", "4", "5"])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out

    assert "Cuisine: Mexican" in captured
    assert "0 matching restaurants." in captured
    assert "No matching restaurants found. Try changing your filters." in captured

def test_discover_restaurants_change_cuisine(monkeypatch, capsys, sample_restaurants):
    responses = iter(["1", "Mexican", "1", "Italian", "4", "5"])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out

    assert "0 matching restaurants." in captured
    assert "Cuisine: Italian" in captured
    assert "2 matching restaurants." in captured
    assert "1. Mario's" in captured
    assert "2. Luigi's" in captured

def test_discover_restaurants_invalid_menu_choice(monkeypatch, capsys, sample_restaurants):
    responses = iter(["7", "1", "Italian", "4", "5"])
    prompts = []

    def mock_input(prompt):
        prompts.append(prompt)
        return next(responses)

    monkeypatch.setattr("builtins.input", mock_input)

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out

    assert "Invalid option. Please choose a number between 1 and 5." in captured
    assert "2 matching restaurants." in captured
    assert "1. Mario's" in captured
    assert "2. Luigi's" in captured

    assert prompts == [
        "Choose an option: ",
        "Choose an option: ",
        "Enter cuisine (0 to clear): ",
        "Choose an option: ",
        "Choose an option: ",
    ]

def test_display_restaurants(capsys, sample_restaurants):
    display_restaurants(sample_restaurants)

    captured = capsys.readouterr().out

    assert "1. Mario's" in captured
    assert "2. Sakura" in captured
    assert "3. Luigi's" in captured
    assert "Cuisines: Italian, Continental" in captured
    assert "Cost per head: ₹800" in captured

def test_display_restaurants_empty(capsys):
    display_restaurants([])

    captured = capsys.readouterr().out

    assert "No matching restaurants found. Try changing your filters." in captured

def test_display_restaurants_unknown_cost(capsys):
    sample = Restaurant(
        name="Test_rest", 
        city="Mumbai",
        location="Andheri",
        cuisines=["Italian", "Continental"],
        cost_per_head=None,
        must_try_dishes=["Pizza"],
        has_veg_option=True,
    )

    display_restaurants([sample])

    captured = capsys.readouterr().out

    assert "Cost per head: Not available" in captured