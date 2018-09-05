from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from appcode.resources.store import Store, StoreList
from appcode.resources.user import UserRegister
from appcode.security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "q@erTyueywyWqw4yF6yo1qwi23#yoq1o311wreuuewsdjfkafsjkhcxbnzbncm678sdkfjh163sddfd489asdsa02"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity) # creates a new end point /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from appcode.db import db
    db.init_app(app)
    app.run("10.154.198.12", port=6777, debug=True)