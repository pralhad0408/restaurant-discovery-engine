from csv_loader import csv_loader
from discovery import apply_filters

def display_menu():
    print("\n1. Discover restaurants")
    print("2. Help me decide")
    print("3. Surprise me")
    print("4. Exit")

def get_menu_choice():
    while True:
        user_choice = input("Choose an option: ").strip()

        if user_choice in ("1", "2", "3", "4"):
            return user_choice
        
        print("Invalid option. Please choose a number between 1 and 4.")

def display_discovery_menu(selected_cuisine, selected_budget, vegetarian_only, match_count):
    cuisine_display = selected_cuisine if selected_cuisine is not None else "Any"
    budget_display = f"₹{selected_budget}" if selected_budget is not None else "Any"
    vegetarian_display = "Yes" if vegetarian_only else "Any"

    print("\n========== DISCOVER RESTAURANTS ==========")

    print("\nCurrent filters:")
    print(f"Cuisine: {cuisine_display}")
    print(f"Maximum cost per head: {budget_display}")
    print(f"Vegetarian options: {vegetarian_display}")

    print(f"\n{match_count} matching restaurants.")

    print("\n1. Choose/change cuisine")
    print("2. Set/change budget")
    print("3. Toggle vegetarian options")
    print("4. Show matching restaurants")
    print("5. Back to main menu")

def discover_restaurants(restaurants):
    selected_cuisine = None
    selected_budget = None
    vegetarian_only = False

    while True:
        matches = apply_filters(restaurants, selected_cuisine, selected_budget, vegetarian_only)
        
        display_discovery_menu(selected_cuisine, selected_budget, vegetarian_only, len(matches))

        user_choice = input("Choose an option: ").strip()

        if user_choice == "1":
            cuisine = input("Enter cuisine (0 to clear): ").strip()

            if cuisine == "":
                print("No input given. Please enter a valid cuisine.")
            elif cuisine == "0":
                selected_cuisine = None
            else:
                selected_cuisine = cuisine
        
        elif user_choice == "2":
            try:
                budget = int(input("Enter budget (0 to clear): ").strip())

                if budget < 0:
                    raise ValueError("Input cannot be negative.")

                if budget == 0:
                    selected_budget = None
                else:
                    selected_budget = budget

            except ValueError:
                print("Invalid budget. Enter a non-negative whole number.")

        elif user_choice == "3":
            vegetarian_only = not vegetarian_only

            if vegetarian_only:
                print("Vegetarian options filter enabled.")
            else:
                print("Vegetarian options filter disabled.")

        elif user_choice == "4":
            if selected_cuisine is not None or selected_budget is not None or vegetarian_only:
                display_restaurants(matches)
            else:
                print("Please select at least one filter before viewing restaurants.")

        elif user_choice == "5":
            return
        
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

def display_restaurants(matches):
    if not matches:
        print("No matching restaurants found. Try changing your filters.")
        return
    
    print("========== MATCHING RESTAURANTS ==========")

    for index, restaurant in enumerate(matches, start=1):
        print(f"\n{index}. {restaurant.name}")
        print(f"   Location: {restaurant.location}")
        print(f"   Cuisines: {', '.join(restaurant.cuisines)}")
        cost_display = (
            f"₹{restaurant.cost_per_head}"
            if restaurant.cost_per_head is not None
            else "Not available"
        )
        print(f"   Cost per head: {cost_display}")

def main():
    restaurants = csv_loader()

    print("Welcome to Kya Khau RDE!")

    while True:
        display_menu()
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