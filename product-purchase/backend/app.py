from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Bekasibarat1@localhost/products' # Replace with your MySQL details
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return jsonify(product_list)

@app.route('/purchase', methods=['POST'])
def purchase():
    data = request.get_json()
    total_price = 0

    for product in data['products']:
        product_id = product['id']
        quantity = product['quantity']
        db_product = Product.query.get(product_id)
        total_price += db_product.price * quantity

    # Logic to save purchase data to database
    # ...

    return jsonify({'total_price': total_price})

if __name__ == '__main__':
    app.run(debug=True)
