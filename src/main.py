from csv_loader import csv_loader
from discovery import filter_by_cuisines

def display_menu():
    print("Welcome to Kya Khau RDE!")

    print("1. Discover restaurants")
    print("2. Help me decide")
    print("3. Surprise me")
    print("4. Exit")

def get_menu_choice():
    while True:
        user_choice = input("Choose an option: ").strip()

        if user_choice in ("1", "2", "3", "4"):
            return user_choice
        
        print("Invalid option. Please choose a number between 1 and 4.")

def discover_restaurants(restaurants):
    cuisine = input("What cuisine are you craving? ")

    matches = filter_by_cuisines(restaurants, cuisine)

    print(f"Found {len(matches)} matching restaurants")

def main():
    restaurants = csv_loader()

    display_menu()

    while True:
        user_choice = get_menu_choice()

        if user_choice == "1":
            discover_restaurants(restaurants)
        elif user_choice == "2":
            print("You selected: Help me decide")
        elif user_choice == "3":
            print("You selected: Surprise me")
        elif user_choice == "4":
            print("You selected: Exit")
            break

if __name__ == "__main__":
    main()