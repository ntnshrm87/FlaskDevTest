from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from appcode.models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("noOfBooks",
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()  # means authenticate before using this method
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "A Store with name '{}' already exists.".format(name)}, 400

        data = Store.parser.parse_args()

        store = StoreModel(name, data['noOfBooks'])

        try:
            store.save_to_db()
        except:
            return {"message": "An error occured while inserting the store."}, 500

        return store.json(), 201


    def put(self, name):
        data = Store.parser.parse_args()

        store = StoreModel.find_by_name(name)
        # updated_store = StoreModel(name, data["noOfBooks"])

        if store is None:
                store = StoreModel.find_by_name(name)
        else:
                store.noOfBooks = data['noOfBooks']

        store.save_to_db()
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {"message": "Store deleted"}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}