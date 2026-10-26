from csv_loader import csv_loader
from restaurant import Restaurant

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