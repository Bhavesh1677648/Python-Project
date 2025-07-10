# Welcome Everyone to my second python project 

# This is a simple python program that prints a reciept of your order in Mcdonald's.

# This Line of code imports date and time from datetime module
from datetime import datetime

# This function prints the header of the receipt
def print_header():
    print("========================================")
    print("          McDonald's Receipt")
    print("========================================")

# This function prints the footer of the receipt
def print_footer():
    print("========================================")
    print("Thankyou for your order!")

# This function prints the current date and time 

def print_date_time():
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date and Time: {date_time}")

# This function shows you the menu of McDonald's with prices 
def print_menu():
    print("Menu:")
    print("BURGERS 🍔:")
    print("1. McAloo Tikki Burger - $2.50")
    print("2. Chicken McGrill Burger - $3.00")
    print("3. McVeggie Burger - $2.75")
    print("4. McSpicy Paneer Burger - $3.25")
    print("5. McSpicy Chicken Burger - $3.50")
    print("6. Filet-O-Fish burger - $3.75")
    print("7. Veg Maharaja Mac - $4.00")
    print("8. Chicken Maharaja Mac - $4.50")
    print("9. McChicken burger - $3.00")
    print("10. Chesseburger - $2.00")
    print("11. Big Mac - $4.00")
    print("12. Double Cheese Burger - $3.50")
    print("Wraps 🌯:")
    print("1. McSpicy Paneer Wrap - $3.00")
    print("2. McSpicy Chicken Wrap - $3.50")
    print("3. McVeggie Wrap - $2.75")
    print("4. McEgg Wrap - $2.50")
    print("5. McChicken Wrap - $3.00")
    print("Sides and Fries 🍟:")
    print("1. Regular Fries - $1.00")
    print("2. Medium Fries - $2.50")
    print("3. Large Fries - $3.00")
    print("4. Peri Peri Fries - $3.50")
    print("5. Veg Pizza McPuff - $1.50")
    print("6. Chicken McNuggets (4 pcs) - $2.00")
    print("7. Chicken McNuggets (6 pcs) - $4.50")
    print("8. Chicken McNuggets (9 pcs) - $7.00")
    print("9. Chicken McNuggets (20pcs) - $8.00")
    print("10. Garlic Mayo Dip - $0.50")
    print("Beverages 🥤:")
    print("1. Coke Small - $1.00")
    print("2. Coke Medium - $2.50")
    print("3. Coke Large - $3.00")
    print("4. Iced Tea - $2.00")
    print("5. Cold Cofee - $1.50")
    print("6. Lemonade - $1.00")
    print("7. McCafe Cappucino - $2.50")
    print("8. McCafe Latte - $2.65")
    print("9. McCafe Mocha - $2.75")
    print("Desserts 🍰:")
    print("1. Vanila Soft Serve Cone - $1.00")
    print("2. Chocolate Soft Serve Cone - $1.50")
    print("3. Chocolate/Strawberry Sundae - $2.00")
    print("4. McFlurry Oreo/ Chocolate Crunch - $3.00")
    print("5. Chocolate Chip Cookies (2pcs) - $1.50")
    print("6. Apple Pie - $1.00")
    print("Combos and Happy Meals 🍔🍟🥤:")
    print("1. Happy Meal(Veg) (Burger, Fries, Drink) - $4.50")
    print("2. Happy Meal(Non-Veg) (Burger, Fries, Drink) - $5.00")
    print("3. McChicken Meal (Burger, Nuggets, Drink) - $6.00")
    print("4. McSpicy Paneer Meal (Burger, Fries, Drink) - $5.50")
    print("5. Filet-O-Fish Meal (Burger, Fries, Drink) - $6.00")
    print("6. Veg Maharaja Mac Meal (Burger, Fries, Drink) - $7.00")
    print("7. Chicken Maharaja Mac Meal (Burger, Fries, Drink) - $8.00")
    print("8. McAloo Tikki Meal (Burger, Fries, Drink) - $5.00")
    print("9. Happy Meal (Veg Wrap, Fries, Drink) - $4.50")

# This function takes the user's order and calculates the total price 
def take_order():
    menu = {
        1: ("McAloo Tikki Burger", 2.50),
        2: ("Chicken McGrill Burger", 3.00),
        3: ("McVeggie Burger", 2.75),
        4: ("McSpicy Paneer Burger", 3.25),
        5: ("McSpicy Chicken Burger", 3.50),
        6: ("Filet-O-Fish burger", 3.75),
        7: ("Veg Maharaja Mac", 4.00),
        8: ("Chicken Maharaja Mac", 4.50),
        9: ("McChicken burger", 3.00),
        10: ("Chesseburger", 2.00),
        11: ("Big Mac", 4.00),
        12: ("Double Cheese Burger", 3.50),
        13: ("McSpicy Paneer Wrap", 3.00),
        14: ("McSpicy Chicken Wrap", 3.50),
        15: ("McVeggie Wrap", 2.75),
        16: ("McEgg Wrap", 2.50),
        17: ("McChicken Wrap", 3.00),
        18: ("Regular Fries", 1.00),
        19: ("Medium Fries", 2.50),
        20: ("Large Fries", 3.00),
        21: ("Peri Peri Fries", 3.50),
        22: ("Veg Pizza McPuff", 1.50),
        23: ("Chicken McNuggets (4 pcs)", 2.00),
        24: ("Chicken McNuggets (6 pcs)", 4.50),
        25: ("Chicken McNuggets (9 pcs)", 7.00),
        26: ("Chicken McNuggets (20pcs)", 8.00),
        27: ("Garlic Mayo Dip", 0.50),
        28: ("Coke Small", 1.00),
        29: ("Coke Medium", 2.50),
        30: ("Coke Large", 3.00),
        31: ("Iced Tea", 2.00),
        32: ("Cold Cofee", 1.50),
        33: ("Lemonade", 1.00),
        34: ("McCafe Cappucino", 2.50),
        35: ("McCafe Latte", 2.65),
        36: ("McCafe Mocha", 2.75),
        37: ("Vanila Soft Serve Cone", 1.00),
        38: ("Chocolate Soft Serve Cone", 1.50),
        39: ("Chocolate/Strawberry Sundae", 2.00),
        40: ("McFlurry Oreo/ Chocolate Crunch", 3.00),
        41: ("Chocolate Chip Cookies (2pcs)", 1.50),
        42: ("Apple Pie", 1.00),
        43: ("Happy Meal(Veg) (Burger, Fries, Drink)", 4.50),
        44: ("Happy Meal(Non-Veg) (Burger, Fries, Drink)", 5.00),
        45: ("McChicken Meal (Burger, Nuggets, Drink)", 6.00),
        46: ("McSpicy Paneer Meal (Burger, Fries, Drink)", 5.50),
        47: ("Filet-O-Fish Meal (Burger, Fries, Drink)", 6.00),
        48: ("Veg Maharaja Mac Meal (Burger, Fries, Drink)", 7.00),
        49: ("Chicken Maharaja Mac Meal (Burger, Fries, Drink)", 8.00),
        50: ("McAloo Tikki Meal (Burger, Fries, Drink)", 5.00),
        51: ("Happy Meal (Veg Wrap, Fries, Drink)", 4.50)
    }
    order = []
    total_price = 0.0
    while True:
        item = input("Enter the item number you want to order (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        try:
            item_number = int(item)
            if item_number not in menu:
                print("Invalid item number. Please try again.")
                continue
            item_name, price = menu[item_number]
            order.append((item_name, price))
            total_price += price
            print(f"Added {item_name} - ${price:.2f} to your order.")
        except ValueError:
            print("Please enter a valid item number or 'done'.")
            continue
    return order, total_price

# This function prints the receipt of the order
def print_receipt(order, total_price):
    print_header()
    print_date_time()
    print_menu()
    print("\nYour Order:")
    for item_name, price in order:
        print(f"{item_name} - ${price:.2f}")
    print(f"\nTotal Price: ${total_price:.2f}")
    print_footer()
def main():
    print_header()
    print_date_time()
    print_menu()
    order, total_price = take_order()
    if order:
        print_receipt(order, total_price)
    else:
        print("No items ordered.")
    print_footer()
if __name__ == "__main__":
    main()

# This is the main function that runs the program
# It prints the header, date and time, menu, takes the order, and prints the receipt
# It also prints the footer
# The program will run until the user enters 'done' to finish the order
# The program is a simple McDonald's receipt generator
# It is a simple program that can be used to order food from McDonald's