from flask import Flask, request, send_from_directory
import random
import json

app = Flask(__name__)


# Path for our main Svelte page
@app.route("/")
def base():
    print()
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)



@app.route("/rand", methods=["POST"])
def hello():
    f = open("./default.json")

    defaultData = json.load(f)
    return json.dumps(defaultData);


if __name__ == "__main__":
    app.run(debug=True)
