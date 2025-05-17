def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
        menu (dictionary): A nested dictionary containing the menu items and their
            prices, using the following format:
            {
                "Food category": {
                    "Meal": price
                }
            }

    Returns:
        order (list): A list of dictionaries containing the menu item name, price,
            and quantity ordered.
        order_total (float): The total price of the order.
    """
    order = []  # List of dictionaries for each item ordered
    menu_items = get_menu_items_dict(
        menu
    )  # Dictionary mapping menu numbers to item info
    print("Welcome to the Generic Take Out Restaurant.")

    ordering = True  # Flag to control the ordering loop
    while ordering:  # Loop until the user decides to stop ordering
        # Prompt the user for their order
        print("What would you like to order? ")

        i = 1  # Initialize menu item number
        # Print the menu
        print_menu_heading()
        # menu is a nested dictionary: {category: {meal: price}}
        # Loop through the menu dictionary to print each item with a number
        for food_category, options in menu.items():
            for meal, price in options.items():  # Get the price of each meal
                # Print the menu item with its number, name, and price
                print_menu_line(i, food_category, meal, price)
                i += 1  # Increment the menu item number

        menu_selection = input("Type menu number: ")  # Prompt user for menu selection
        # order is a list of dictionaries, menu_items is a dictionary
        order = update_order(order, menu_selection, menu_items)
        # Ask the user if they want to continue ordering
        # If the user enters 'n', stop ordering
        continue_order = input("Would you like to keep ordering? (N) to quit: ")

        # If the user enters 'n', stop ordering
        if continue_order.lower() == "n":
            # Print the order summary
            print("Thank you for your order.")
            # List comprehension to get total for each item (dictionary)
            prices_list = [item["Price"] * item["Quantity"] for item in order]
            # Calculate the total price of the order
            # round() is used to round the total to 2 decimal places
            order_total = round(sum(prices_list), 2)
            ordering = False  # Set the flag to False to exit the loop

    return order, order_total  # order is a list of dictionaries, order_total is a float


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
        order (list): A list of dictionaries containing the menu item name, price,
            and quantity ordered.
        menu_selection (str): The customer's menu selection.
        menu_items (dictionary): A dictionary mapping menu numbers to item info.

    Returns:
        order (list): The updated list of dictionaries for the order.
    """
    # menu_items is a dictionary: {menu_number: {"Item name": ..., "Price": ...}}
    # Check if the menu selection is a digit
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)  # Convert menu_selection to an integer
        if (
            menu_selection in menu_items.keys()
        ):  # Check if the menu selection is a valid menu item
            item_name = menu_items[menu_selection]["Item name"]
            # Prompt the user for the quantity of the item
            quantity = input(
                f"What quantity of {item_name} would you like? \n"
                + "(This will default to 1 if number is not entered)\n"
            )
            if quantity.isdigit():  # Check if the quantity is a digit
                # Convert quantity to an integer
                quantity = int(quantity)
            else:
                quantity = 1  # Default to 1 if not a digit
            # Append a dictionary for this item to the order list
            order.append(
                {
                    "Item name": item_name,
                    "Price": menu_items[menu_selection]["Price"],
                    "Quantity": quantity,
                }
            )
        else:# If the menu selection is not valid
            # Print an error message
            print("Sorry, that is not a valid menu selection.")
            print(f"Sorry, {menu_selection} is not a valid menu selection.")
            print(f"{menu_selection} was not a menu option.")
    else: # If the menu selection is not a digit
        # Print an error message
        print("Sorry, that is not a valid menu selection.")
        print(f"Sorry, {menu_selection} is not a valid menu selection.")
        print(f"{menu_selection} was not a menu option.")
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
        receipt (list): A list of dictionaries containing the menu item name, price,
            and quantity ordered.
    """
    # receipt is a list of dictionaries
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        print_receipt_line(item_name, price, item["Quantity"]) # Print each item in the receipt


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################


def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
        item_name (str): The name of the meal item.
        price (float): The price of the meal item.
        quantity (int): The quantity of the meal item.
    """
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")


def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")


def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
        total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
        index (int): The menu item number.
        food_category (str): The category of the food item.
        meal (str): The name of the meal item.
        price (float): The price of the meal item.
    """
    # food_category and meal are strings from the nested menu dictionary
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")


def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu
    number.

    Parameters:
        menu (dictionary): A nested dictionary containing the menu items and their
            prices.

    Returns:
        menu_items (dictionary): A dictionary mapping menu numbers to dictionaries
            with "Item name" and "Price" keys.
    """
    # menu is a nested dictionary: {category: {meal: price}}
    menu_items = {}
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            # Each menu item is stored as a dictionary in menu_items
            menu_items[i] = {"Item name": food_category + " - " + meal, "Price": price}
            i += 1
    return menu_items


def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
        meals (dictionary): A nested dictionary containing the menu items and their
            prices in the following format:
            {
                "Food category": {
                    "Meal": price
                }
            }
    """
    # meals is a nested dictionary
    meals = {
        "Burrito": {"Chicken": 4.49, "Beef": 5.49, "Vegetarian": 3.99},
        "Rice Bowl": {"Teriyaki Chicken": 9.99, "Sweet and Sour Pork": 8.99},
        "Sushi": {"California Roll": 7.49, "Spicy Tuna Roll": 8.49},
        "Noodles": {"Pad Thai": 6.99, "Lo Mein": 7.99, "Mee Goreng": 8.99},
        "Pizza": {"Cheese": 8.99, "Pepperoni": 10.99, "Vegetarian": 9.99},
        "Burger": {"Chicken": 7.49, "Beef": 8.49},
    }
    return meals


# Run the program
if __name__ == "__main__":
    meals = get_menu_dictionary()  # meals is a nested dictionary
    receipt, total_price = place_order(meals)  # receipt is a list of dictionaries
    print("This is what we are preparing for you.\n")
    print_receipt_heading()
    print_itemized_receipt(receipt)
    print_receipt_footer(total_price)
