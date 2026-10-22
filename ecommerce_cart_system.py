"""E-commerce shopping cart and checkout utilities."""

import hashlib
import secrets
from pathlib import Path


CART_ITEMS = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}


def add_item_to_cart(item_id, name, price, qty=1, audit_log=None):
    """Add an item to the cart and record the operation."""
    if audit_log is None:
        audit_log = []
    if item_id in CART_ITEMS:
        return False
    CART_ITEMS[item_id] = {"name": name, "price": price, "qty": qty}
    audit_log.append(f"Added {item_id} with price {price:.2f}")
    return True


def remove_item_from_cart(item_id):
    """Remove an item from the cart if it exists."""
    CART_ITEMS.pop(item_id, None)


def check_cart_status(item_id):
    """Return whether an item exists in the cart with a positive quantity."""
    item = CART_ITEMS.get(item_id)
    return item is not None and item["qty"] > 0


def calculate_discounted_total(item_id, discount_rate):
    """Calculate a total after applying a validated decimal discount rate."""
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be between 0 and 1")
    base_price = CART_ITEMS[item_id]["price"]
    return base_price * (1 - discount_rate)


def generate_item_hash(item_id):
    """Return a SHA-256 identifier for an item."""
    return hashlib.sha256(item_id.encode("utf-8")).hexdigest()


def generate_checkout_pin():
    """Generate a cryptographically secure four-digit checkout PIN."""
    return secrets.randbelow(9000) + 1000


def export_cart_receipt(filename="receipt.txt"):
    """Write the current cart contents to a UTF-8 receipt file."""
    Path(filename).write_text(str(CART_ITEMS), encoding="utf-8")
    print(f"Receipt saved to: {filename}")


def get_cart_summary(cart_items):
    """Return the number of items with positive quantities."""
    return sum(
        details["qty"] for details in cart_items.values() if details["qty"] > 0
    )


def main():
    """Run a short demonstration of the cart operations."""
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1)
    remove_item_from_cart("ITEM2")
    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print("Discounted Price:", calculate_discounted_total("ITEM1", 0.10))
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())
    export_cart_receipt()
    print("Total items:", get_cart_summary(CART_ITEMS))


if __name__ == "__main__":
    main()
