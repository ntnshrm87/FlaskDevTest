"Aim: To check if the Flask is running fine post installation."

from flask import Flask

app = Flask(__name__)

# this is the end point url location. if '/' means the home page of app.
@app.route('/')
def home():
    return "hello world...!!!"


app.run("10.154.198.12", port=6776, debug=True)