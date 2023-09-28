import sqlite3

# Menghubungkan ke database (jika tidak ada, akan dibuat)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Membuat tabel
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
''')

# Menambahkan data ke tabel
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Product 1', 10.99))
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Product 2', 19.99))
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Product 3', 25.49))

# Menyimpan perubahan ke database
conn.commit()

# Membaca data dari tabel
cursor.execute('SELECT * FROM products')
products = cursor.fetchall()

for product in products:
    print(f'Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}')

# Menutup koneksi
conn.close()
