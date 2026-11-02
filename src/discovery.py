def filter_by_cuisines(restaurants, cuisine):
    matches = []
    search_term = cuisine.strip().lower()

    for restaurant in restaurants:
        for searched_cuisine in restaurant.cuisines:
            if searched_cuisine.lower() == search_term:
                matches.append(restaurant)
                break

    return matches