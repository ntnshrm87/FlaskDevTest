from appcode.db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    noOfBooks = db.Column(db.Integer)

    def __init__(self, name, noOfBooks):
        self.name = name
        self.noOfBooks = noOfBooks

    def json(self):
        return {"name": self.name, "noOfBooks": self.noOfBooks}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # SELECT * FROM stores WHERE name=name LIMIT 1

    def save_to_db(self):
        # Session contains multiple objects and we are just upserting.
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
