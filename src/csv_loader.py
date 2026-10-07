from pathlib import Path
import csv

def csv_loader():
    src_dir = Path(__file__).parent
    csv_path = src_dir.parent / 'data' / 'besteats_restaurants_summary.csv'
    restaurants = []

    with open(csv_path, newline='') as csvfile:
        file_contents = csv.DictReader(csvfile)

        for row in file_contents:
            restaurants.append(row)
        
    return restaurants