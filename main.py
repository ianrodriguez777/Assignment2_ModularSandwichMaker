import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        customer_order = input("What size sandwich would you like? (Options: Small, Medium, Large): ").lower()
        if customer_order in recipes:
            cost = recipes[customer_order]["Cost"]
            ingredients = recipes[customer_order]["Ingredients"]

            if sandwich_maker_instance.check_resources(ingredients):
                print(f"Your total is ${cost}")

if __name__=="__main__":
    main()