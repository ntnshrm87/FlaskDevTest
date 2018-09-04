# Aim: Sending a GET request using Flask Restful and
#      using POSTMAN to validate the request.
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Store(Resource):
    def get(self, name):
        return {"Store": name}

api.add_resource(Store, '/store/<string:name>')

app.run("10.154.198.12", port=6777, debug=True)