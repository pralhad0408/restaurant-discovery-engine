from pathlib import Path
import csv
from restaurant import Restaurant

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

            cuisines = []

            if row["all_cuisines"]:
                all_cuisines = row["all_cuisines"].split(",")
                for cuisine in all_cuisines:
                    cleaned_cuisine = cuisine.strip()

                    if cleaned_cuisine:
                        cuisines.append(cleaned_cuisine)

            must_try_dishes = []
            
            raw_value = row["what_to_eat"]

            curator_recommendations = raw_value.split("|")

            for recommendation in curator_recommendations:
                dishes = recommendation.split(",")

                for dish in dishes:
                    cleaned_dish = dish.strip()

                    if cleaned_dish:
                        must_try_dishes.append(cleaned_dish)
            
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