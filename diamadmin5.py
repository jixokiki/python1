import mysql.connector

# Membuat koneksi
conn = mysql.connector.connect(
    host='localhost',
    user='root',          # Ganti dengan nama pengguna MySQL Anda
    password='Bekasibarat1',      # Ganti dengan kata sandi MySQL Anda
    database='statusph'  # Ganti dengan nama database Anda
)

# Membuat cursor
cursor = conn.cursor()

# Mendefinisikan tabel pengguna
cursor.execute('''
    CREATE TABLE IF NOT EXISTS phd (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE,
        status VARCHAR(255)
    )
''')

# Mendefinisikan tabel tugas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS phdtask (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        task_name VARCHAR(255),
        status VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Menambahkan beberapa data awal
# cursor.execute('INSERT IGNORE INTO users (username, status) VALUES (%s, %s)', ('admin', 'admin'))
# cursor.execute('INSERT IGNORE INTO users (username, status) VALUES (%s, %s)', ('user1', 'active'))
# cursor.execute('INSERT IGNORE INTO users (username, status) VALUES (%s, %s)', ('user2', 'active'))
# cursor.execute('INSERT IGNORE INTO tasks (user_id, task_name, status) VALUES (%s, %s, %s)', (2, 'Tugas 1', 'belum dikerjakan'))
# cursor.execute('INSERT IGNORE INTO tasks (user_id, task_name, status) VALUES (%s, %s, %s)', (3, 'Tugas 2', 'belum dikerjakan'))
# conn.commit()
cursor.execute('INSERT IGNORE INTO phd (username, status) VALUES (%s, %s)', ('admin', 'admin'))
cursor.execute('INSERT IGNORE INTO phd (username, status) VALUES (%s, %s)', ('user1', 'active'))
cursor.execute('INSERT IGNORE INTO phd (username, status) VALUES (%s, %s)', ('user2', 'active'))
cursor.execute('INSERT IGNORE INTO phdtask (user_id, task_name, status) VALUES (%s, %s, %s)', (2, 'Tugas 1', 'belum dikerjakan'))
cursor.execute('INSERT IGNORE INTO phdtask (user_id, task_name, status) VALUES (%s, %s, %s)', (3, 'Tugas 2', 'belum dikerjakan'))
conn.commit()


# Fungsi untuk melihat pengguna dan tugasnya
# def view_users_and_tasks(admin_username=None):
#     cursor.execute('SELECT users.username, users.status, tasks.task_name, tasks.status FROM users LEFT JOIN tasks ON users.id = tasks.user_id')
#     results = cursor.fetchall()
    
#     for row in results:
#         username, user_status, task_name, task_status = row
#         print(f'Username: {username}, Status: {user_status}, Tugas: {task_name}, Status Tugas: {task_status}')

def view_users_and_tasks(admin_username=None):
    cursor.execute('SELECT phd.username, phd.status, phdtask.task_name, phdtask.status FROM phd LEFT JOIN phdtask ON phd.id = phdtask.user_id')
    results = cursor.fetchall()
    
    for row in results:
        username, user_status, task_name, task_status = row
        print(f'Username: {username}, Status: {user_status}, Tugas: {task_name}, Status Tugas: {task_status}')

# Fungsi autentikasi untuk memeriksa apakah pengguna adalah administrator
# def is_admin(username):
#     cursor.execute('SELECT status FROM users WHERE username = %s', (username,))
#     user_status = cursor.fetchone()
#     return user_status[0] == 'admin'

def is_admin(username):
    cursor.execute('SELECT status FROM phd WHERE username = %s', (username,))
    user_status = cursor.fetchone()
    return user_status[0] == 'admin'


# Fungsi untuk mengubah status pengguna (memeriksa autentikasi admin terlebih dahulu)
# def change_user_status(username, new_status, admin_username):
#     if is_admin(admin_username):
#         cursor.execute('UPDATE users SET status = %s WHERE username = %s', (new_status, username))
#         conn.commit()
#         print(f'Status pengguna {username} telah diubah menjadi {new_status} oleh admin {admin_username}')
#     else:
#         print(f'Anda tidak memiliki izin untuk mengubah status pengguna.')

def change_user_status(username, new_status, admin_username):
    if is_admin(admin_username):
        cursor.execute('UPDATE phd SET status = %s WHERE username = %s', (new_status, username))
        conn.commit()
        print(f'Status pengguna {username} telah diubah menjadi {new_status} oleh admin {admin_username}')
    else:
        print(f'Anda tidak memiliki izin untuk mengubah status pengguna.')

# Fungsi untuk menandai tugas sebagai selesai (memeriksa autentikasi admin terlebih dahulu)
# def mark_task_done(username, task_name, admin_username):
#     if is_admin(admin_username):
#         cursor.execute('UPDATE tasks SET status = %s WHERE user_id = (SELECT id FROM users WHERE username = %s) AND task_name = %s', ('selesai', username, task_name))
#         conn.commit()
#         print(f'Tugas {task_name} milik pengguna {username} telah ditandai sebagai selesai oleh admin {admin_username}')
#     else:
#         print(f'Anda tidak memiliki izin untuk menandai tugas sebagai selesai.')

def mark_task_done(username, task_name, admin_username):
    if is_admin(admin_username):
        cursor.execute('UPDATE phdtask SET status = %s WHERE user_id = (SELECT id FROM phd WHERE username = %s) AND task_name = %s', ('selesai', username, task_name))
        conn.commit()
        print(f'Tugas {task_name} milik pengguna {username} telah ditandai sebagai selesai oleh admin {admin_username}')
    else:
        print(f'Anda tidak memiliki izin untuk menandai tugas sebagai selesai.')

# Melihat pengguna dan tugas mereka
# view_users_and_tasks()

# Mengubah status pengguna (autentikasi sebagai admin)
# admin_username = 'admin'  # Ganti dengan nama admin yang sesuai
# user_to_change = 'user2'  # Ganti dengan nama pengguna yang akan diubah statusnya
# new_user_status = 'tidak aktif'  # Ganti dengan status yang sesuai

admin_username = 'admin'  # Ganti dengan nama admin yang sesuai
user_to_change = 'user2'  # Ganti dengan nama pengguna yang akan diubah statusnya
new_user_status = 'tidak aktif'  # Ganti dengan status yang sesuai

# change_user_status(user_to_change, new_user_status, admin_username)
# view_users_and_tasks()

change_user_status(user_to_change, new_user_status, admin_username)
# view_users_and_tasks()

# Menandai tugas sebagai selesai (autentikasi sebagai admin)
# admin_username = 'admin'  # Ganti dengan nama admin yang sesuai
# user_to_mark_task = 'user1'  # Ganti dengan nama pengguna yang akan diubah status tugasnya
# task_to_mark = 'Tugas 1'  # Ganti dengan nama tugas yang akan ditandai selesai
# new_task_status = 'selesai'  # Ganti dengan status yang sesuai

admin_username = 'admin'  # Ganti dengan nama admin yang sesuai
user_to_mark_task = 'user1'  # Ganti dengan nama pengguna yang akan diubah status tugasnya
task_to_mark = 'Tugas 1'  # Ganti dengan nama tugas yang akan ditandai selesai
new_task_status = 'selesai'  # Ganti dengan status yang sesuai

# mark_task_done(user_to_mark_task, task_to_mark, admin_username)
# view_users_and_tasks()

mark_task_done(user_to_mark_task, task_to_mark, admin_username)
view_users_and_tasks()
# Menutup koneksi
cursor.close()
conn.close()
