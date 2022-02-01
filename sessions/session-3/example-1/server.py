#%%

from flask import Flask, send_from_directory

app = Flask("example-1")

@app.route("/images/<image>.png")
def serve_image(image):
    return send_from_directory(
        "example-1/images",
        filename = image + ".png")

app.run()
