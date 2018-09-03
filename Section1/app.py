# Aim:
# 1. Using HTTP verbs and REST principles in Flask
# 2. Declaring end point functions for a book store app

# POST - used to receive data
# GET - used to send data back only

# Note: This server perspective and the browser perspective is just reverse.


from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': "NS Book Store",
        'items': [
            {
                'name': "Gray Hat Hacking",
                'price': 37.67
            }
        ]
    }
]


# POST /store data:{name}
@app.route("/store", methods=["POST"])
def create_store():
    pass


# GET /store/<string:name>
@app.route("/store/<string:name>") # http://10.154.198.12:6776/store/store_name>
def get_store(name):
    pass


# GET /store
@app.route("/store")
def get_stores():
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    pass


app.run("10.154.198.12", port=6776, debug=True)