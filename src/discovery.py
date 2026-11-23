def filter_by_cuisines(restaurants, cuisine):
    matches = []
    search_term = cuisine.strip().lower()

    for restaurant in restaurants:
        for searched_cuisine in restaurant.cuisines:
            if searched_cuisine.lower() == search_term:
                matches.append(restaurant)
                break

    return matches

def filter_by_cost(restaurants, max_cost):
    matches = []

    for restaurant in restaurants:
        if restaurant.cost_per_head is not None and restaurant.cost_per_head <= max_cost:
            matches.append(restaurant)

    return matches

def filter_by_vegetarian_option(restaurants):
    matches = []

    for restaurant in restaurants:
        if restaurant.has_veg_option:
            matches.append(restaurant)

    return matches

def apply_filters(restaurants, selected_cuisine, selected_budget, vegetarian_only):
    matches = restaurants.copy()

    if selected_cuisine is not None:
        matches = filter_by_cuisines(matches, selected_cuisine)

    if selected_budget is not None:
        matches = filter_by_cost(matches, selected_budget)

    if vegetarian_only:
        matches = filter_by_vegetarian_option(matches)

    return matches