from discovery import filter_by_cuisines, filter_by_cost, filter_by_vegetarian_option
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