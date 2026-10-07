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

            if row["all_cuisines"]:
                cuisines = row["all_cuisines"].split(", ")
            else:
                cuisines = []
            
            restaurant = Restaurant(
                row["restaurant_name"],
                row["city"],
                row["location"],
                cuisines,
                cost_per_head,
                row["what_to_eat"],
                row["has_vegetarian_option"] == "t",
            )

            restaurants.append(restaurant)
        
    return restaurants