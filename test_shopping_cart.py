import pytest
from shopping_cart import Product, Cart

def test_add_item():
    cart = Cart()
    product = Product("Laptop", 1200.0)
    cart.add_item(product)
    assert len(cart.items) == 1
    assert cart.items[0].name == "Laptop"

def test_remove_item():
    cart = Cart()
    product = Product("Mouse", 25.0)
    cart.add_item(product)
    cart.remove_item("Mouse")
    assert len(cart.items) == 0

def test_total_price():
    cart = Cart()
    cart.add_item(Product("Laptop", 1200.0))
    cart.add_item(Product("Keyboard", 45.0))
    assert cart.total_price() == 1245.0

def test_show_cart_empty():
    cart = Cart()
    assert cart.items == []

def test_show_cart():
    cart = Cart()
    cart.add_item(Product("Headphones", 150.0))
    assert str(cart.items[0]) == "Headphones: $150.00"
