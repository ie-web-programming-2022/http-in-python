#%%

from flask import Flask, jsonify

app = Flask("server")

@app.route("/")
def index():
    return "this is the index!"

@app.route("/hello", methods=["DELETE"])
def hello():
    return "hello MCSBT!"

@app.route("/users/<username>")
def user(username):
    return "this is " + username + "'s profile!"

@app.route("/api/user/<username>")
def json_user(username):
    return jsonify({"user": username})


app.run()
# %%






