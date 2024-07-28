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
        customer_order = input("What size sandwich would you like? (Options: small, medium, large): ").lower()
        if customer_order in recipes:
            cost = recipes[customer_order]["Cost"]
            ingredients = recipes[customer_order]["Ingredients"]

            if sandwich_maker_instance.check_resources(ingredients):
                print(f"Your total is ${cost}")
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    print(sandwich_maker_instance.make_sandwich(customer_order, ingredients))
                else:
                    print("The transaction has failed. You may try again.")
            else:
                print("There are not enough ingredients to make your sandwich.")
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()