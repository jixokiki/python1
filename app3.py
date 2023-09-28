from flask import Flask, request, jsonify

app = Flask(__name__)

# Data sementara sebagai contoh
todos = [
    {'id': 1, 'task': 'Belajar Flask'},
    {'id': 2, 'task': 'Buat aplikasi web'}
]

# Route untuk mengambil daftar tugas
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

# Route untuk menambah tugas baru
@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = {'id': len(todos) + 1, 'task': request.json['task']}
    todos.append(new_todo)
    return jsonify(new_todo), 201

if __name__ == '__main__':
    app.run(debug=True)
