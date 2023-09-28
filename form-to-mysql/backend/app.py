from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Bekasibarat1@localhost/form_data' # Replace with your MySQL details
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    note = db.Column(db.String(500))
    email = db.Column(db.String(100), nullable=False)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    new_form_data = FormData(name=data['name'], address=data['address'], note=data['note'], email=data['email'])
    db.session.add(new_form_data)
    db.session.commit()
    return jsonify({'message': 'Form data submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
