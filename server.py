import sqlite3
from flask import Flask, request, send_from_directory
import random
import json

app = Flask(__name__)


# Path for our main Svelte page

@app.route("/")
def base():
    print()
    return send_from_directory('client/public', 'index.html')


paths = ["global.css", "build/bundle.css", "build/bundle.js"]
# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    if path in paths:
        return send_from_directory('client/public', path)
    else:
        return send_from_directory('client/public', "index.html")



@app.route("/getPage", methods=["POST"])
def getPage():
    f = open("./default.json")
    defaultData = json.load(f)
    return json.dumps(defaultData);

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    data["username"] = data["username"].strip()
    data["password"] = data["password"].strip()

    myConnection = sqlite3.connect('users.sqlite')
    myCursor = myConnection.cursor()

    if len(data["username"]) == 0 or len(data["password"]) == 0:
        myConnection.close()
        return json.dumps({"flag": False, "error": "username and password cannot be empty!"});

    myCursor.execute("SELECT * FROM users where username=:username", {'username': data["username"]})
    records = myCursor.fetchall()
    if len(records) > 0:
        myConnection.close()
        return json.dumps({"flag": False, "error": "username already taken"});


    myCursor.execute("INSERT INTO users VALUES (:username, :password)",
                        {
                            'username': data["username"],
                            'password': data["password"]
                        })
    myConnection.commit()
    myConnection.close()
    return json.dumps({"flag": True});




if __name__ == "__main__":
    app.run(debug=True)
