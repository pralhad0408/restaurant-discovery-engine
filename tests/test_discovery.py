from discovery import filter_by_cuisines, filter_by_cost, filter_by_vegetarian_option, apply_filters
from main import discover_restaurants
from restaurant import Restaurant
import pytest

def test_filter_by_cuisines_empty_list():
    result = filter_by_cuisines([], "Italian")
    assert result == []

@pytest.mark.parametrize("search_term", [
    "Italian",
    "italian",
    "ITALIAN",
    " Italian ",
])
def test_filter_by_cuisines_variations(sample_restaurants, search_term):
    result = filter_by_cuisines(sample_restaurants, search_term)

    assert [r.name for r in sample_restaurants] == [
        "Mario's", "Sakura", "Luigi's"
    ]

    names = [r.name for r in result]
    assert names == ["Mario's", "Luigi's"]

@pytest.mark.parametrize("max_cost, expected", [
    (799, ["Sakura"]),
    (800, ["Mario's", "Sakura"]),
    (801, ["Mario's", "Sakura"]),
])
def test_filter_by_cost(sample_restaurants, max_cost, expected):
    result = filter_by_cost(sample_restaurants, max_cost)

    assert [r.name for r in result] == expected

def test_filter_by_cost_excludes_none(sample_restaurants):
    mystery_cafe = Restaurant(
        name="Mystery Cafe",
        city="Mumbai",
        location="Dadar",
        cuisines=["Continental", "Cafe"],
        cost_per_head=None,
        must_try_dishes=["Americano"],
        has_veg_option=True,
    )

    restaurants = [sample_restaurants[0], mystery_cafe]

    result = filter_by_cost(restaurants, 800)

    assert [r.name for r in result] == ["Mario's"]

def test_filter_by_vegetarian_option(sample_restaurants):
    original = sample_restaurants.copy()

    result = filter_by_vegetarian_option(sample_restaurants)

    assert [r.name for r in result] == ["Mario's", "Luigi's"]
    assert sample_restaurants == original

def test_filter_by_vegetarian_option_no_matches(sample_restaurants):
    sakura = sample_restaurants[1]

    result = filter_by_vegetarian_option([sakura])

    assert result == []

def test_combined_filters(sample_restaurants):
    result_1 = filter_by_cuisines(sample_restaurants, "Italian")
    result_2 = filter_by_cost(result_1, 800)
    result_3 = filter_by_vegetarian_option(result_2)

    assert [r.name for r in result_3] == ["Mario's"]

def test_combined_filters_no_matches(sample_restaurants):
    result_1 = filter_by_cuisines(sample_restaurants, "Japanese")
    result_2 = filter_by_cost(result_1, 1000)
    result_3 = filter_by_vegetarian_option(result_2)

    assert result_3 == []

@pytest.mark.parametrize("selected_cuisine, selected_budget, vegetarian_only, expected_names", [
    (None, None, False, ["Mario's", "Sakura", "Luigi's"]),
    ("Italian", None, False, ["Mario's", "Luigi's"]),
    ("Italian", 800, False, ["Mario's"]),
    ("Italian", 800, True, ["Mario's"]),
    ("Japanese", 800, True, []),
    (None, None, True, ["Mario's", "Luigi's"]),
])
def test_apply_filters(sample_restaurants, selected_cuisine, selected_budget, vegetarian_only, expected_names):
    original = sample_restaurants.copy()
    matches = apply_filters(sample_restaurants, selected_cuisine, selected_budget, vegetarian_only)
    actual_names = [restaurant.name for restaurant in matches]

    assert actual_names == expected_names
    assert sample_restaurants == original
    assert matches is not sample_restaurants

def test_discover_restaurants_clear_budget(monkeypatch, capsys, sample_restaurants):
    responses = iter([
        "1", "Italian",
        "2", "800",
        "4",
        "2", "0",
        "4",
        "5",
    ])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out
    sections = captured.split("========== MATCHING RESTAURANTS ==========")

    assert len(sections) == 3
    
    assert "1. Mario's" in sections[1]
    assert "Luigi's" not in sections[1]

    assert "1. Mario's" in sections[2]
    assert "2. Luigi's" in sections[2]

def test_discover_restaurants_invalid_budget_preserves_selection(
        monkeypatch, capsys, sample_restaurants,
):
    responses = iter([
        "1", "Italian",
        "2", "800",
        "2", "abc",
        "4",
        "5",
    ])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out
    dashboard = captured.rsplit(
        "========== DISCOVER RESTAURANTS ==========",
        maxsplit=1
    )[-1]

    assert "Invalid budget. Enter a non-negative whole number." in captured
    assert "Mario's" in captured
    assert "Luigi's" not in captured
    assert "Maximum cost per head: ₹800" in dashboard

def test_discover_restaurants_vegetarian_toggle(monkeypatch, capsys, sample_restaurants):
    responses = iter([
        "3",
        "4",
        "3",
        "1", "Japanese",
        "4",
        "5",
    ])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out
    sections = captured.split("========== MATCHING RESTAURANTS ==========")

    assert len(sections) == 3
    
    assert "Mario's" in sections[1]
    assert "Luigi's" in sections[1]
    assert "Sakura" not in sections[1]

    assert "Sakura" in sections[2]
    assert "Mario's" not in sections[2]
    assert "Luigi's" not in sections[2]

def test_discover_restaurants_no_filters(monkeypatch, capsys, sample_restaurants):
    responses = iter([
        "4",
        "5",
    ])

    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))

    discover_restaurants(sample_restaurants)

    captured = capsys.readouterr().out

    assert "Please select at least one filter before viewing restaurants." in captured
    assert "========== MATCHING RESTAURANTS ==========" not in captured