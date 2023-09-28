# import mysql.connector

# # Membuat koneksi
# conn = mysql.connector.connect(
#     host='localhost',
#     user='username',
#     password='password',
#     database='nama_database'
# )

# # Membuat cursor
# cursor = conn.cursor()

# # Fungsi untuk mengubah data berdasarkan ID
# def update_data_by_id(id, new_username, new_password):
#     query = "UPDATE nama_tabel SET username = %s, password = %s WHERE id = %s"
#     cursor.execute(query, (new_username, new_password, id))
#     conn.commit()
#     print(f"Data dengan ID {id} berhasil diubah")

# # Fungsi untuk menghapus data berdasarkan ID
# def delete_data_by_id(id):
#     query = "DELETE FROM nama_tabel WHERE id = %s"
#     cursor.execute(query, (id,))
#     conn.commit()
#     print(f"Data dengan ID {id} berhasil dihapus")

# # Contoh penggunaan
# try:
#     # Mengubah data dengan ID tertentu
#     update_data_by_id(1, "new_username", "new_password")

#     # Menghapus data dengan ID tertentu
#     delete_data_by_id(2)

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# # Menutup kursor dan koneksi
# cursor.close()
# conn.close()



import mysql.connector

# Membuat koneksi
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bekasibarat1',
    database='diam'
)

# Membuat cursor
cursor = conn.cursor()

# Membaca data dari tabel
def read_data():
    cursor.execute("SELECT * FROM diam_it")
    result = cursor.fetchall()

    for row in result:
        print(row)

# Menambahkan data ke tabel
def insert_data(data):
    query = "INSERT INTO diam_it (username, password) VALUES (%s, %s)"
    cursor.execute(query, data)
    conn.commit()
    print("Data berhasil ditambahkan")
    
def delete_data_by_username(username):
    query = "DELETE FROM diam_it WHERE username = %s"
    cursor.execute(query, (username,))
    conn.commit()
    print(f"Data dengan username {username} berhasil dihapus")


# Mengubah data dalam tabel
# def update_data(data, id):
#     query = "UPDATE diam_it SET username = %s, password = %s WHERE id = %s"
#     cursor.execute(query, (*data, id))
#     conn.commit()
#     print("Data berhasil diubah")

# Menghapus data dari tabel
# def delete_data(id):
#     query = "DELETE FROM diam_it WHERE id = %s"
#     cursor.execute(query, (id,))
#     conn.commit()
#     print("Data berhasil dihapus")


# # Fungsi untuk mengubah data berdasarkan ID
# def update_data_by_id(username, password):
#     query = "UPDATE diam_it SET password = %s WHERE username = %s"
#     cursor.execute(query, (username, password))
#     conn.commit()
#     print(f"Data dengan Username {username} berhasil diubah")

# # Fungsi untuk menghapus data berdasarkan ID
# def delete_data_by_id(username):
#     query = "DELETE FROM diam_it WHERE username = %s"
#     cursor.execute(query, (username,))
#     conn.commit()
#     print(f"Data dengan Username {username} berhasil dihapus")

# # Contoh penggunaan
# try:
#     # Mengubah data dengan ID tertentu
#     update_data_by_id("new_username", "new_password")

#     # Menghapus data dengan ID tertentu
#     delete_data_by_id("Nilai3","Nilai4")

# except mysql.connector.Error as err:
#     print(f"Error: {err}")


# Contoh penggunaan
# read_data()

# Tambahkan data
# insert_data(("Nilai3", "Nilai4"))

# Mengubah data dengan ID tertentu
# update_data(("Nilai3", "Nilai4"), 1)

# Menghapus data dengan ID tertentu
# delete_data(1)
delete_data_by_username("Nilai1","Nilai2")
# Membaca data setelah operasi
read_data()

# Menutup kursor dan koneksi
cursor.close()
conn.close()



