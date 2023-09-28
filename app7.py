from flask import Flask, jsonify, request

app = Flask(__name__)

# Data sementara
tasks = [
    {
        'id': 1,
        'title': 'Belajar Python',
        'done': False
    },
    {
        'id': 2,
        'title': 'Membuat RESTful API',
        'done': False
    }
]

# Mendapatkan daftar tugas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Mendapatkan tugas berdasarkan ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Tidak ditemukan'}), 404
    return jsonify({'task': task[0]})

# Menambahkan tugas baru
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Format data salah'}), 400
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Mengubah status tugas (selesai/belum selesai)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Tidak ditemukan'}), 404
    if not request.json:
        return jsonify({'error': 'Format data salah'}), 400
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# Menghapus tugas berdasarkan ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Tidak ditemukan'}), 404
    tasks.remove(task[0])
    return jsonify({'result': 'Tugas dihapus'})

if __name__ == '__main__':
    app.run(debug=True)
