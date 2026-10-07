class Restaurant:
    def __init__(
            self,
            name,
            city,
            location,
            cuisine,
            cost_per_head,
            must_try_dishes,
            has_veg_option,
        ):

            self.name = name
            self.city = city
            self.location = location
            self.cuisine = cuisine
            self.cost_per_head = cost_per_head
            self.must_try_dishes = must_try_dishes
            self.has_veg_option = has_veg_option