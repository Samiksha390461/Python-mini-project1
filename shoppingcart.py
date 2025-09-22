def display_cart(cart):
    if not cart:
        print("your cart is emptty")
    else:
        print("shopping cart")
    total_price=0
    for item in cart:
        print(f"{item['name']}: ${item['price']}")
        total_price += item['price']
    print(f"Total: ${total_price:.2f}")
def main():
    cart= []
    while True:
        print("\nShopping cart Application")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter the price: "))
            item = {"name": item_name, "price": item_price}
            cart.append(item)
            print("Item added to cart!")
        elif choice == '2':
            display_cart(cart)
        elif choice == '3':
            if not cart:
                print("your cart is already empty")
            else:
                display_cart(cart)
                item_index = int(input("Enter the item number to input: ")) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"Removed item: {removed_item['name']}")
                else:
                    print("Invalid item number")
        elif choice == '4':
            print("Exit the application")
            break
        else:
            print("Invalid choice. Please the valid option")
if __name__ == "__main__":
    main()


