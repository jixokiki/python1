from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/login', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
