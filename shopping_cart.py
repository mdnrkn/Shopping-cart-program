foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    elif food.isdigit():
        print("Please enter a valid food name.")
    else:
        while True:
            # Prompt the user for the price of the item and validate it
            try:
                price = float(input(f"Enter the price of a {food} (in dollars and cents): $"))
                if price <= 0:
                    print("Price must be a positive number.")
                else:
                    break
            except ValueError:
                print("Price must be a number.")

        # Add the item and its price to the lists
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

# Format the total cost as currency
formatted_total = "${:,.2f}".format(total)

print()
print(f"Your total is: {formatted_total}")
