def grocerystore():
    print("Welcome to') the grocery store!")
    items = {
        '1': ('Apple', 0.5),
        '2': ('Banana', 0.3),
        '3': ('Milk', 1.2),
        '4': ('Bread', 2.0),
        '5': ('Eggs', 0.2)
    }
    for key , (name, price) in items.items():
        print (f"{key}. {name} - ${price}")
    cart = []
    while True:
        choice = input("Enter the item number to add to cart (or 'done' to quit): ")
        if choice.lower() == 'done': 
            break
        elif choice in items:
            quantity = int(input(f"How many would you like to add? "))
            cart.append((choice, quantity))
        else:
            print("Invalid choice, please try again.")
    
    print("receipt:")
    total = 0
    for item, quantity in cart:
        name, price = items[item]
        item_total = price * quantity
        total += item_total
        print(f"{name} x{quantity} - ${item_total}")

    print(f"Total: ${total}")
if __name__ == "__main__":    grocerystore()