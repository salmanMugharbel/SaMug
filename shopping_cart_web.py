from flask import Flask, render_template, request, redirect, url_for
from shopping_cart import Product, Cart

app = Flask(__name__)
cart = Cart()

# Predefined product catalog
product_catalog = [
    Product("Laptop", 1200.0),
    Product("Headphones", 150.0),
    Product("Smartphone", 800.0),
    Product("Mouse", 25.0),
    Product("Keyboard", 45.0)
]

@app.route('/')
def home():
    return render_template('index.html', products=product_catalog)

@app.route('/add/<product_name>')
def add_to_cart(product_name):
    for product in product_catalog:
        if product.name == product_name:
            cart.add_item(product)
            break
    return redirect(url_for('view_cart'))

@app.route('/view-cart')
def view_cart():
    items = cart.items
    total = cart.total_price()
    return render_template('cart.html', items=items, total=total)

@app.route('/remove/<product_name>')
def remove_from_cart(product_name):
    cart.remove_item(product_name)
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
