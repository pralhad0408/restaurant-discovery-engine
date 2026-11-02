from discovery import filter_by_cuisines
from restaurant import Restaurant
import pytest

@pytest.fixture
def sample_restaurants():
    r1 = Restaurant(
        name="Mario's", 
        city="Mumbai",
        location="Andheri",
        cuisines=["Italian", "Continental"],
        cost_per_head=800,
        must_try_dishes=["Pizza"],
        has_veg_option=True,
    )
    
    r2 = Restaurant(
        name="Sakura",
        city="Mumbai",
        location="Bandra",
        cuisines=["Japanese", "Korean"],
        cost_per_head= 750,
        must_try_dishes=["Sushi"],
        has_veg_option=True,
    )

    r3 = Restaurant(
        name="Luigi's",
        city="Mumbai",
        location="Colaba",
        cuisines=["Italian", "Pizza"],
        cost_per_head=1000,
        must_try_dishes=["Spaghetti"],
        has_veg_option=True,
    )

    return [r1, r2, r3]

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