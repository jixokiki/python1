from flask import Flask, render_template,request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index4.html')

# Membuat koneksi ke basis data SQLite (bisa diganti dengan MySQL atau yang lainnya)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Membuat tabel pengguna jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        role TEXT
    )
''')

conn.commit()

# Simulasikan basis data pengguna dengan daftar dictionary
# Setiap dictionary mewakili satu pengguna dengan informasi nama pengguna dan peran.
users = [
    {"username": "rizki", "role": "admin"},
    {"username": "user1", "role": "user"},
    {"username": "user2", "role": "user"}
]

# Endpoint untuk otentikasi pengguna
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    
    # Mencari pengguna dalam basis data
    cursor.execute('SELECT role FROM users WHERE username = ?', (username,))
    user_role = cursor.fetchone()
    
    # Jika pengguna ada dalam basis data, gunakan autentikasi basis data
    if user_role:
        return jsonify({"role": user_role[0]})
    else:
        # Jika pengguna tidak ada dalam basis data, gunakan autentikasi simulasi
        user = next((user for user in users if user["username"] == username), None)
        if user:
            return jsonify({"role": user["role"]})
        else:
            return jsonify({"role": "unknown"})

# Endpoint yang hanya dapat diakses oleh admin
@app.route('/admin', methods=['GET'])
def admin_dashboard():
    username = request.args.get('username')
    
    # Mencari pengguna dalam basis data
    cursor.execute('SELECT role FROM users WHERE username = ?', (username,))
    user_role = cursor.fetchone()
    
    # Jika pengguna ada dalam basis data dan berperan sebagai admin, gunakan autentikasi basis data
    if user_role and user_role[0] == "admin":
        return jsonify({"message": "Halo admin, Anda memiliki akses ke fitur admin!"})
    else:
        # Jika pengguna tidak ada dalam basis data atau tidak berperan sebagai admin, gunakan autentikasi simulasi
        user = next((user for user in users if user["username"] == username), None)
        if user and user["role"] == "admin":
            return jsonify({"message": "Halo admin, Anda memiliki akses ke fitur admin!"})
        else:
            return jsonify({"message": "Anda tidak memiliki izin untuk mengakses fitur admin."})

# Endpoint untuk menambahkan pengguna baru dari formulir HTML
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('name')
    role = request.form.get('role')
    
    # Memasukkan pengguna baru ke dalam basis data
    cursor.execute('INSERT INTO users (username, role) VALUES (?, ?)', (username, role))
    conn.commit()
    
    return f'Pengguna {username} dengan peran {role} telah ditambahkan!'

if __name__ == '__main__':
    app.run(debug=True)
