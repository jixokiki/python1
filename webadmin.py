from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

# Simulasikan basis data pengguna dengan daftar dictionary
# Setiap dictionary mewakili satu pengguna dengan informasi nama pengguna dan peran.
# users = [
#     {"username": "rizki", "role": "admin"},
#     {"username": "user1", "role": "user"},
#     {"username": "user2", "role": "user"}
# ]

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f'Hello, {name}!'

# Endpoint untuk otentikasi pengguna
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # username = data.get('username')
    # username = data.get('name') 
    name = request.form.get('name')   
    
    # Mencari pengguna dengan nama pengguna yang diberikan
    # user = next((user for user in users if user["username"] == username), None)
    user = next((user for user in submit if user["name"] == name), None)
    
    if user:
        return jsonify({"role": user["role"]})
    else:
        return jsonify({"role": "unknown"})

# Endpoint yang hanya dapat diakses oleh admin
@app.route('/admin', methods=['GET'])
def admin_dashboard():
    # username = request.args.get('username')
    # username = request.args.get('name')
    name = request.form.get('name')    
    # Mencari pengguna dengan nama pengguna yang diberikan
    # user = next((user for user in users if user["username"] == username), None)
    user = next((user for user in submit if user["name"] == name), None)
    
    if user and user["role"] == "admin":
        return jsonify({"message": "Halo admin, Anda memiliki akses ke fitur admin!"})
    else:
        return jsonify({"message": "Anda tidak memiliki izin untuk mengakses fitur admin."})

if __name__ == '__main__':
    app.run(debug=True)
