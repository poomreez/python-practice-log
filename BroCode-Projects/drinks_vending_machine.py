# Drinks Vending Machines Program

# Create dictionaries of menus and prices
menu = {
    "water" : 1.00,
    "soda" : 1.50,
    "juice" : 1.75,
    "milk" : 2.00,
    "energy" : 2.25,
    "tea" : 2.00,
    "beer" : 3.00,
    "whey" : 3.25
}

# Create empty cart and total
cart = []
total = 0

# Show the menus and prices
print("------------- MENU -------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------------")

# Select System
while True:
    drink = input("Selech an item (q to quit): ").lower()
    if drink == "q":
        break
    elif menu.get(drink) is not None:
        cart.append(drink)

# Crashier System
print("--------- YOUR ORDER -----------")
for drink in cart:
    total += menu.get(drink)
    print(drink, end=" ")

print()
print(f"Total is: ${total:.2f}")
