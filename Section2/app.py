# Aim1: Sending a GET request using Flask Restful and
#      using POSTMAN to validate the request.
# Aim2: Creating all methods as designed with POSTMAN.
# Aim3: Improving Error correction using filter functions.
# Aim4: Apply authentication and logging with Flask JWT.
#       Adding secret key and security.py

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "qwerty"
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates a new end point /auth

stores = []


class Store(Resource):
    @jwt_required()  # means authenticate before using this method
    def get(self, name):
        # for store in stores:
        #   if store['name'] == name:
        #       return store"""
        store = next(filter(lambda x: x["name"] == name, stores), None)

        return {"store": store}, 200 if store else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, stores), None) is not None:
            return {"message": "An item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        store = {"name": name, "noOfBooks": data['noOfBooks']}
        stores.append(store)
        return store, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("noOfBooks",
                            type=int,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        data = parser.parse_args()

        # data = request.get_json()
        store = next(filter(lambda x: x["name"] == name, stores), None)
        if store is None:
            store = {"name": name, "noOfBooks": data['noOfBooks']}
            stores.append(store)
        else:
            store.update(data)
        return store

    def delete(self, name):
        global stores
        stores = list(filter(lambda x: x["name"] != name, stores))
        return {"message": "Item deleted"}


class StoreList(Resource):
    def get(self):
        return {"stores": stores}


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')

app.run("10.154.198.12", port=6777, debug=True)