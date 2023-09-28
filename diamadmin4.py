import sqlite3

# Koneksi ke database (Anda harus menyesuaikan dengan jenis database yang Anda gunakan)
conn = sqlite3.connect('database4.db')
cursor = conn.cursor()

# Mendefinisikan tabel pengguna
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        status TEXT
    )
''')

# Mendefinisikan tabel tugas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_name TEXT,
        status TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Menambahkan beberapa data awal
cursor.execute('INSERT OR IGNORE INTO users (username, status) VALUES (?, ?)', ('admin', 'admin'))
cursor.execute('INSERT OR IGNORE INTO users (username, status) VALUES (?, ?)', ('user1', 'active'))
cursor.execute('INSERT OR IGNORE INTO users (username, status) VALUES (?, ?)', ('user2', 'active'))
cursor.execute('INSERT OR IGNORE INTO tasks (user_id, task_name, status) VALUES (?, ?, ?)', (2, 'Tugas 1', 'belum dikerjakan'))
cursor.execute('INSERT OR IGNORE INTO tasks (user_id, task_name, status) VALUES (?, ?, ?)', (3, 'Tugas 2', 'belum dikerjakan'))
conn.commit()

# Fungsi untuk melihat pengguna dan tugasnya
def view_users_and_tasks(admin_username=None):
    cursor.execute('SELECT users.username, users.status, tasks.task_name, tasks.status FROM users LEFT JOIN tasks ON users.id = tasks.user_id')
    results = cursor.fetchall()
    
    for row in results:
        username, user_status, task_name, task_status = row
        print(f'Username: {username}, Status: {user_status}, Tugas: {task_name}, Status Tugas: {task_status}')

# Fungsi autentikasi untuk memeriksa apakah pengguna adalah administrator
def is_admin(username):
    cursor.execute('SELECT status FROM users WHERE username = ?', (username,))
    user_status = cursor.fetchone()
    return user_status[0] == 'admin'

# Fungsi untuk mengubah status pengguna (memeriksa autentikasi admin terlebih dahulu)
def change_user_status(username, new_status, admin_username):
    if is_admin(admin_username):
        cursor.execute('UPDATE users SET status = ? WHERE username = ?', (new_status, username))
        conn.commit()
        print(f'Status pengguna {username} telah diubah menjadi {new_status} oleh admin {admin_username}')
    else:
        print(f'Anda tidak memiliki izin untuk mengubah status pengguna.')

# Fungsi untuk menandai tugas sebagai selesai (memeriksa autentikasi admin terlebih dahulu)
def mark_task_done(username, task_name, admin_username):
    if is_admin(admin_username):
        cursor.execute('UPDATE tasks SET status = ? WHERE user_id = (SELECT id FROM users WHERE username = ?) AND task_name = ?', ('selesai', username, task_name))
        conn.commit()
        print(f'Tugas {task_name} milik pengguna {username} telah ditandai sebagai selesai oleh admin {admin_username}')
    else:
        print(f'Anda tidak memiliki izin untuk menandai tugas sebagai selesai.')

# Fungsi untuk memvalidasi status pengguna
def validate_user_status(new_status):
    if new_status not in ('active', 'tidak aktif'):
        print("Status pengguna tidak valid. Harap gunakan 'active' atau 'tidak aktif'.")
        return False
    return True

# Fungsi untuk memvalidasi status tugas
def validate_task_status(new_status):
    if new_status not in ('belum dikerjakan', 'selesai'):
        print("Status tugas tidak valid. Harap gunakan 'belum dikerjakan' atau 'selesai'.")
        return False
    return True

# Mengubah status pengguna (autentikasi sebagai admin)
admin_username = 'user1'  # Ganti dengan nama admin yang sesuai
user_to_change = 'user2'  # Ganti dengan nama pengguna yang akan diubah statusnya
new_user_status = 'tidak aktif'  # Ganti dengan status yang sesuai

if validate_user_status(new_user_status):
    change_user_status(user_to_change, new_user_status, admin_username)

# Menandai tugas sebagai selesai (autentikasi sebagai admin)
admin_username = 'admin'  # Ganti dengan nama admin yang sesuai
user_to_mark_task = 'user1'  # Ganti dengan nama pengguna yang akan diubah status tugasnya
task_to_mark = 'Tugas 1'  # Ganti dengan nama tugas yang akan ditandai selesai
new_task_status = 'selesai'  # Ganti dengan status yang sesuai

if validate_task_status(new_task_status):
    mark_task_done(user_to_mark_task, task_to_mark, admin_username)

# Melihat pengguna dan tugas mereka
view_users_and_tasks()

# Menutup koneksi
conn.close()
