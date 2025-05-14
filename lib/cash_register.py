#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize total to 0
        self.total = 0
        # Set the discount (default is 0 if not provided)
        self.discount = discount
        # Items will hold a list of item titles (e.g., ["apple", "apple", "bread"])
        self.items = []
        # Track the value of the last transaction for voiding
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        # Increase the total based on the item price and quantity
        self.total += price * quantity
        # Add the item title to the items list, repeated `quantity` times
        for _ in range(quantity):
            self.items.append(title)
        # Track the last transaction amount
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            # Calculate the amount to subtract based on the discount
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Print the updated total with discount applied
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            # If there's no discount, print this message
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract the last transaction from the total
        self.total -= self.last_transaction_amount
        # Reset last transaction (optional)
        self.last_transaction_amount = 0

