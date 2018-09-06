from appcode.db import db


class MallModel(db.Model):
    __tablename__ = 'malls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    stores = db.relationship("StoreModel", lazy="dynamic")

    def __init__(self, name):
        self.name = name


    def json(self):
        return {"name": self.name, "stores": [store.json() for store in self.stores.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # SELECT * FROM malls WHERE name=name LIMIT 1

    def save_to_db(self):
        # Session contains multiple objects and we are just upserting.
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
