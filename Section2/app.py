# Aim1: Sending a GET request using Flask Restful and
#      using POSTMAN to validate the request.
# Aim2: Creating all methods as designed with POSTMAN.
# Aim3: Improving Error correction using filter functions.
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

stores = []


class Store(Resource):
    def get(self, name):
        # for store in stores:
        #   if store['name'] == name:
        #       return store"""
        store = next(filter(lambda x: x["name"] == name, stores), None)

        return {"store": None}, 200 if store else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, stores), None) is not None:
            return {"message": "An item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        store = {"name": name, "noOfBooks": data['noOfBooks']}
        stores.append(store)
        return store, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass

class StoreList(Resource):
    def get(self):
        return {"stores": stores}



api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')

app.run("10.154.198.12", port=6777, debug=True)