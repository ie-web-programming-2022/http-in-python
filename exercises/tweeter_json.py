# Create an HTTP server that, depending on the path which represents the username,
# returns a list of tweets as JSON
#%%
from flask import Flask, jsonify

database = {
    "jack": ["just setting up my twttr", "just selling my tweet as an NFT"],
    "pepe": ["hello y'all!"]
}

server = Flask("tweeter")

@server.route("/users/<username>")
def handle_user(username):
    if username in database:
        return jsonify(database[username]), 200
    else:
        return "user doesn't exist", 404


server.run()
# %%
