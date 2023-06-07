from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello world"

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"Message": "Hello World"})