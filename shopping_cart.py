# interactive_shopping_cart.py

class Product:
    def __init__(self, name, price):
        """
        Initialize a product with a name and price.
        :param name: str - Name of the product
        :param price: float - Price of the product
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Cart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []

    def add_item(self, product):
        """
        Add a product to the cart.
        :param product: Product - The product to add
        """
        self.items.append(product)
        print(f"===============================\nAdded {product.name} to the cart.")

    def remove_item(self, product_name):
        """
        Remove a product from the cart by name.
        :param product_name: str - The name of the product to remove
        """
        for item in self.items:
            if item.name.lower() == product_name.lower():
                self.items.remove(item)
                print(f"===============================\nRemoved {item.name} from the cart.")
                return
        print(f"Product '{product_name}' not found in the cart.")

    def total_price(self):
        """
        Calculate the total price of all items in the cart.
        :return: float - Total price
        """
        return sum(item.price for item in self.items)

    def show_cart(self):
        """
        Display the items in the cart.
        """
        if not self.items:
            print("===============================\nYour cart is empty.")
        else:
            print("===============================\nItems in your cart:")
            for item in self.items:
                print(f"- {item}")
            print(f"Total: ${self.total_price():.2f}")


def display_menu():
    print("===============================\nPlease choose an option:")
    print("1. Add a product to the cart")
    print("2. Remove a product from the cart")
    print("3. View cart")
    print("4. Checkout and exit")


def main():
    print("Welcome to Salman shop!")
    cart = Cart()

    # Predefined product catalog
    product_catalog = [
        Product("Laptop", 1200.0),
        Product("Headphones", 150.0),
        Product("Smartphone", 800.0),
        Product("Mouse", 25.0),
        Product("Keyboard", 45.0)
    ]

    # Interactive loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Display product catalog
            print("===============================\nAvailable products:")
            for idx, product in enumerate(product_catalog, start=1):
                print(f"{idx}. {product}")

            # Get product choice from user
            try:
                product_choice = int(input("Enter the product number to add to the cart: "))
                if 1 <= product_choice <= len(product_catalog):
                    selected_product = product_catalog[product_choice - 1]
                    cart.add_item(selected_product)
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '2':
            product_name = input("===============================\nEnter the name of the product to remove: ")
            cart.remove_item(product_name)

        elif choice == '3':
            cart.show_cart()

        elif choice == '4':
            print("Checking out... Here is your final cart:")
            cart.show_cart()
            print("Thank you for shopping with us! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
