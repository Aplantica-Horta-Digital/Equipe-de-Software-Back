import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Status(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('time',
		type=str,
		required=True,
		help="Cannot be left blank!"
	)
	parser.add_argument('temp',
		type=int,
		required=True,
		help="Cannot be left blank!"
	)

	@jwt_required()
	def post(self):
		data = Status.parser.parse_args()

		status = {'time': data['time'], 'temp': data['temp']}

		try:
			connection = sqlite3.connect('data.db')
			cursor = connection.cursor()

			query = "INSERT INTO status VALUES (?, ?)"
			cursor.execute(query, (status['time'], status['temp']))

			connection.commit()
			connection.close()
		except:
			return {"msesage": "An error has ocurred inserting"}, 500

		return status, 201
