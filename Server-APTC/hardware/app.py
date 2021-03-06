from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from hardware import Status

app = Flask(__name__)
app.secret_key = 'tantoFaz'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Status, '/status')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	app.run(port=8000, debug=True)
	
