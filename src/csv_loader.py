from pathlib import Path
import csv

def csv_loader():
    src_dir = Path(__file__).parent
    csv_path = src_dir.parent / 'data' / 'besteats_restaurants_summary.csv'

    with open(csv_path, newline='') as csvfile:
        file_contents = csv.reader(csvfile)

        next(file_contents)

        row_count = 0 

        for row in file_contents:
            row_count += 1
    
    return row_count