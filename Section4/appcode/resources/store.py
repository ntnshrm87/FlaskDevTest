import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("noOfBooks",
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM stores WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"store": {"name": row[0], "noOfBooks": row[1]}}

    @jwt_required()  # means authenticate before using this method
    def get(self, name):
        store = self.find_by_name(name)
        if store:
            return store
        return {"message": "Store not found"}, 404

    @classmethod
    def insert(cls, store):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO stores VALUES (?,?)"
        cursor.execute(query, (store["name"], store["noOfBooks"]))

        connection.commit()
        connection.close()

    def post(self, name):
        if self.find_by_name(name):
            return {"message": "A Store with name '{}' already exists.".format(name)}, 400

        data = Store.parser.parse_args()

        store = {"name": name, "noOfBooks": data['noOfBooks']}

        try:
            self.insert(store)
        except:
            return {"message": "An error occured while inserting the store."}, 500

        return store, 201

    @classmethod
    def update(cls, store):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "UPDATE stores SET noOfBooks=? WHERE name=?"
        cursor.execute(query, (store["noOfBooks"]), store["name"], )

        connection.commit()
        connection.close()

    def put(self, name):
        data = Store.parser.parse_args()

        store = self.find_by_name(name)
        updated_store = {"name": name, "noOfBooks": data["noOfBooks"]}

        if store is None:
            try:
                self.insert(updated_store)
            except:
                return {"message": "An error occured inserting store."}, 500
        else:
            try:
                self.update(updated_store)
            except:
                return {"message": "An error occured updating store."}, 500
        return updated_store

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM stores WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {"message": "Store deleted"}


class StoreList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM stores"
        result = cursor.execute(query)
        stores = []

        for row in result:
            stores.append({"name": row[0], "noOfBooks": row[1]})

        connection.close()

        return {"store": stores}