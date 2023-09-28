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

# Route untuk mengambil tugas berdasarkan ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Tugas tidak ditemukan'}), 404
    return jsonify(todo)

# Route untuk mengupdate tugas berdasarkan ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Tugas tidak ditemukan'}), 404
    todo['task'] = request.json['task']
    return jsonify(todo)

# Route untuk menghapus tugas berdasarkan ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'message': 'Tugas berhasil dihapus'})

if __name__ == '__main__':
    app.run(debug=True)
