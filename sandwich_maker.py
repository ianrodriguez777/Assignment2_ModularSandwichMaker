
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                return False
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Subtract the amount of resources used from total resources"""
        if self.check_resources(order_ingredients):
            for item in order_ingredients:
                self.machine_resources[item] -= order_ingredients[item]
            return f"We made a {sandwich_size} sandwich"
        else:
            return f"Sorry! There are not enough resources to make a {sandwich_size} sandwich"