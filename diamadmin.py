import sqlite3

# Koneksi ke database (Anda harus menyesuaikan dengan jenis database yang Anda gunakan)
conn = sqlite3.connect('database.db')
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
def view_users_and_tasks():
    cursor.execute('SELECT users.username, users.status, tasks.task_name, tasks.status FROM users LEFT JOIN tasks ON users.id = tasks.user_id')
    results = cursor.fetchall()
    
    for row in results:
        username, user_status, task_name, task_status = row
        print(f'Username: {username}, Status: {user_status}, Tugas: {task_name}, Status Tugas: {task_status}')

# Fungsi untuk mengubah status pengguna
def change_user_status(username, new_status):
    cursor.execute('UPDATE users SET status = ? WHERE username = ?', (new_status, username))
    conn.commit()

# Fungsi untuk menandai tugas sebagai selesai
def mark_task_done(username, task_name):
    cursor.execute('UPDATE tasks SET status = ? WHERE user_id = (SELECT id FROM users WHERE username = ?) AND task_name = ?', ('selesai', username, task_name))
    conn.commit()

# Melihat pengguna dan tugas mereka
view_users_and_tasks()

# Mengubah status pengguna
change_user_status('admin', 'tidak aktif')
view_users_and_tasks()

# Menandai tugas sebagai selesai
mark_task_done('user1', 'Tugas 1')
view_users_and_tasks()

# Menutup koneksi
conn.close()
