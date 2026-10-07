class Restaurant:
    def __init__(
            self,
            name,
            city,
            location,
            cuisines,
            cost_per_head,
            must_try_dishes,
            has_veg_option,
        ):

            self.name = name
            self.city = city
            self.location = location
            self.cuisines = cuisines
            self.cost_per_head = cost_per_head
            self.must_try_dishes = must_try_dishes
            self.has_veg_option = has_veg_option