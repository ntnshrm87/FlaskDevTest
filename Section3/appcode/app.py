# Aim1: Sending a GET request using Flask Restful and
#      using POSTMAN to validate the request.
# Aim2: Creating all methods as designed with POSTMAN.
# Aim3: Improving Error correction using filter functions.
# Aim4: Apply authentication and logging with Flask JWT.
#       Adding secret key and security.py
# Aim5: Adding reqparse from flask_restful and optimising
#       final appcode.
# Aim6: Writing stores to database

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from user import UserRegister

from appcode.security import authenticate, identity
from store import Store, StoreList

app = Flask(__name__)
app.secret_key = "q@erTyueywyWqw4yF6yo1qwi23#yoq1o311wreuuewsdjfkafsjkhcxbnzbncm678sdkfjh163sddfd489asdsa02"
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates a new end point /auth


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run("10.154.198.12", port=6777, debug=True)