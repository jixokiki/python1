from flask import Flask, request, jsonify

app = Flask(__name__)

# Contoh data sementara untuk penyimpanan
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json['description']
    }
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
