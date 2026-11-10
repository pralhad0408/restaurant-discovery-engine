import pytest
from restaurant import Restaurant

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
        has_veg_option=False,
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