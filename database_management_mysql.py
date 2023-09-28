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
product_data = [
    ("Product 1", 10.99),
    ("Product 2", 19.99),
    ("Product 3", 25.49)
]
cursor.executemany(insert_query, product_data)
conn.commit()

# Membaca data dari tabel
select_query = "SELECT * FROM product"
cursor.execute(select_query)
products = cursor.fetchall()

for product in products:
    print(f'Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')

# Menutup koneksi
conn.close()
