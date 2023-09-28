from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99},
    {'id': 2, 'name': 'Product 2', 'price': 19.99},
    {'id': 3, 'name': 'Product 3', 'price': 25.49}
]

@app.route('/')
def home():
    return render_template('index2.html', products=products)

@app.route('/checkout', methods=['POST'])
def checkout():
    total = 0
    for product in products:
        product_id = str(product['id'])
        quantity = int(request.form.get(product_id, 0))
        total += quantity * product['price']
    return f'Total: ${total:.2f}'

if __name__ == '__main__':
    app.run(debug=True)
