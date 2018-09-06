from flask_restful import Resource
from appcode.models.mall import MallModel


class Mall(Resource):
    def get(self, name):
        mall = MallModel.find_by_name(name)
        if mall:
            return mall.json()
        return {"message": "Mall not found..."}, 404

    def post(self, name):
        if MallModel.find_by_name(name):
            return {"message": "A mall with name '{}' already exists.".format(name)},400

        mall = MallModel(name)
        try:
            mall.save_to_db()
        except:
            return {"message": "An error occurred while creating the mall."}, 500

        return mall.json(), 201

    def delete(self, name):
        mall = MallModel.find_by_name(name)
        if mall:
            mall.delete_from_db()

        return {"message": "Mall deleted."}


class MallList(Resource):
    def get(self):
        return {"malls": [mall.json() for mall in MallModel.query.all()]}