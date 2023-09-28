from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# Data sementara sebagai contoh
users = {
    "user1": "password1",
    "user2": "password2"
}

# Fungsi untuk verifikasi username dan password
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Class resource yang memerlukan autentikasi
class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {"message": "Ini adalah resource privat yang memerlukan autentikasi"}

api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)
