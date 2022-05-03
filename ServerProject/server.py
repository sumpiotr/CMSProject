from flask import Flask, request, send_from_directory
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Add database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

# initialize db
db = SQLAlchemy(app)


# db models

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("Problem with password!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Username %r>' % self.username


# Path for our main Svelte page

@app.route("/")
def base():
    print()
    return send_from_directory('../client/public', 'index.html')


paths = ["global.css", "build/bundle.css", "build/bundle.js"]


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    if path in paths:
        return send_from_directory('../client/public', path)
    else:
        return send_from_directory('../client/public', "index.html")


@app.route("/getPage", methods=["POST"])
def get_page():
    f = open("../default.json")
    default_data = json.load(f)
    return json.dumps(default_data)


@app.route("/register", methods=["POST"])
def register():
    data = request.json

    data["username"] = data["username"].strip()
    data["password"] = data["password"].strip()

    if len(data["username"]) == 0 or len(data["password"]) == 0:
        return json.dumps({"flag": False, "error": "username and password cannot be empty!"})

    user = Users.query.filter_by(username=data["username"]).first()
    if user is not None:
        return json.dumps({"flag": False, "error": "username already taken"})

    user = Users(username=data["username"])
    user.password = data["password"]
    db.session.add(user)
    db.session.commit()

    return json.dumps({"flag": True, "password": user.password_hash})


if __name__ == "__main__":
    app.run(debug=True)
