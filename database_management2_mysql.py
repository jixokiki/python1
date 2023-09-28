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


import mysql.connector

# Menghubungkan ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bekasibarat1",
    database="products"
)
cursor = conn.cursor()

# # Membuat tabel (jika belum ada)
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10, 2)
#     )
# ''')

# Menambahkan data ke tabel
insert_query = "INSERT INTO product (name, price) VALUES (%s, %s)"
# product_data = [
#     ("Product 1", 10.99),
#     ("Product 2", 19.99),
#     ("Product 3", 25.49)
# ]
cursor.executemany(insert_query, products)
conn.commit()

# Membaca data dari tabel
select_query = "SELECT * FROM product"
cursor.execute(select_query)
productss = cursor.fetchall()

for product in productss:
    print(f'Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')

# Menutup koneksi
conn.close()
