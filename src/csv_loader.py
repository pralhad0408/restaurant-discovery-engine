from pathlib import Path
import csv
from restaurant import Restaurant

def normalize_cuisines(raw_cuisines):
    cuisines = []

    if raw_cuisines:
        all_cuisines = raw_cuisines.split(",")
        for cuisine in all_cuisines:
            cleaned_cuisine = cuisine.strip()

            if cleaned_cuisine:
                cuisines.append(cleaned_cuisine)

    return cuisines

def normalize_dishes(raw_dishes):
    must_try_dishes = []

    curator_recommendations = raw_dishes.split("|")

    for recommendation in curator_recommendations:
        dishes = recommendation.split(",")

        for dish in dishes:
            cleaned_dish = dish.strip()

            if cleaned_dish:
                must_try_dishes.append(cleaned_dish)

    return must_try_dishes


def csv_loader():
    src_dir = Path(__file__).parent
    csv_path = src_dir.parent / 'data' / 'besteats_restaurants_summary.csv'
    restaurants = []

    with open(csv_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            if row["avg_cost_per_head"]:
                cost_per_head = int(row["avg_cost_per_head"])
            else:
                cost_per_head = None

            cuisines = normalize_cuisines(row["all_cuisines"])

            must_try_dishes = normalize_dishes(row["what_to_eat"])
            
            restaurant = Restaurant(
                row["restaurant_name"],
                row["city"],
                row["location"],
                cuisines,
                cost_per_head,
                must_try_dishes,
                row["has_vegetarian_option"] == "t",
            )

            restaurants.append(restaurant)
        
    return restaurants