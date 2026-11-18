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
    while True:
        cuisine = input("What cuisine are you craving? ")
        matches = filter_by_cuisines(restaurants, cuisine)

        if not matches:
            print("No matches found. Would you like to try another cuisine?")
            print("1. Try again")
            print("2. Back to main menu")

            while True:
                retry_cuisine = input("Choose an option: ").strip()

                if retry_cuisine == "1":
                    break
                elif retry_cuisine == "2":
                    return
                else:
                    print("Invalid input. Choose either 1 or 2.")

        else:
            print(f"Found {len(matches)} matching restaurants")
            return

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