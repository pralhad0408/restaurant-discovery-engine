from csv_loader import csv_loader, normalize_cuisines, normalize_dishes
from restaurant import Restaurant
import pytest

def test_csv_loader_returns_restaurants():
    result = csv_loader()
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], Restaurant)

def test_vegetarian_option_is_boolean():
    result = csv_loader()

    for restaurant in result:
        assert isinstance(restaurant.has_veg_option, bool)

def test_cost_per_head_normalization():
    result = csv_loader()

    for restaurant in result:
        assert isinstance(restaurant.cost_per_head, int) or restaurant.cost_per_head is None

def test_cost_per_head_values():
    result = csv_loader()

    amber_found = False
    araku_found = False

    for restaurant in result:
        if restaurant.name == "Amber Sweets":
            amber_found = True
            assert restaurant.cost_per_head == 500

        if restaurant.name == "ARAKU Coffee":
            araku_found = True
            assert restaurant.cost_per_head is None

    assert amber_found
    assert araku_found

def test_cuisine_normalization():
    result = csv_loader()

    for restaurant in result:
        assert isinstance(restaurant.cuisines, list)

        for cuisine in restaurant.cuisines:
            assert isinstance(cuisine, str)
            assert cuisine
            assert cuisine == cuisine.strip()

def test_must_try_dishes_normalization():
    result = csv_loader()

    for restaurant in result:
        assert isinstance(restaurant.must_try_dishes, list)

        for dish in restaurant.must_try_dishes:
            assert isinstance(dish, str)
            assert dish
            assert dish == dish.strip()

@pytest.mark.parametrize(
        "raw_cuisines, expected",
        [
            ("Japanese, Korean", ["Japanese", "Korean"]),
            ("Italian", ["Italian"]),
            ("", []),
            ("Indian , Chinese ", ["Indian", "Chinese"]),
            ("Italian, , Continental", ["Italian", "Continental"]),
        ],
)
def test_normalize_cuisines_split_values(raw_cuisines, expected):
    result = normalize_cuisines(raw_cuisines)
    assert result == expected

@pytest.mark.parametrize(
    "raw_dishes, expected",
    [
        ("Biryani, Kebab", ["Biryani", "Kebab"]),
        ("Pizza | Pasta", ["Pizza", "Pasta"]),
        ("Chicken Pizza | Motichur Ladoo, Masala Milk", ["Chicken Pizza", "Motichur Ladoo", "Masala Milk"]),
        ("", []),
        ("Biryani, , Kebab | ", ["Biryani", "Kebab"]),
    ],
)
def test_normalize_dishes_split_values(raw_dishes, expected):
    result = normalize_dishes(raw_dishes)
    assert result == expected