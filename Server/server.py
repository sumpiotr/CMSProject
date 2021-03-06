from datetime import datetime

from flask import Flask, request, send_from_directory
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from os.path import exists
import os
from flask import send_file

app = Flask(__name__)

# Add database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

app.config["SECRET_KEY"] = "super secret and unique key"

# initialize db
db = SQLAlchemy(app)

# login system

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# db models

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)

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


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer)
    add_date = db.Column(db.Date, default=datetime.now())
    text = db.Column(db.String(100))
    author = db.Column(db.String(50))


def other_admin_exist(user_id):
    users = Users.query.all()
    for user in users:
        if user.admin and user.id != user_id:
            return True
    return False


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
    f = open("default.json")
    default_data = json.load(f)
    logged = current_user.is_authenticated
    admin = current_user.admin if logged else False
    return json.dumps({"data": default_data, "logged": logged, "admin": admin}, ensure_ascii=False)


@app.route("/savePage", methods=["POST"])
def save_page():
    data = request.json["newData"]

    with open('default.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return json.dumps(data)


@app.route("/register", methods=["POST"])
def register():
    data = request.json

    data["username"] = data["username"].strip()
    data["password"] = data["password"].strip()

    if len(data["username"]) == 0 or len(data["password"]) == 0:
        return json.dumps({"flag": False, "error": "username and password cannot be empty!"})

    user = Users.query.filter_by(username=data["username"]).first()
    if user:
        return json.dumps({"flag": False, "error": "username already taken"})

    user = Users(username=data["username"])
    user.password = data["password"]
    db.session.add(user)
    db.session.commit()

    return json.dumps({"flag": True, "error": "Registered! Now you can log in"})


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if current_user.is_authenticated:
        return json.dumps({"flag": False, "error": "You already are logged!"})
    user = Users.query.filter_by(username=data["username"]).first()
    if user:
        if user.verify_password(data["password"]):
            login_user(user)
            return json.dumps({"flag": True})
    return json.dumps({"flag": False, "error": "Wrong username or password!"})


@app.route("/logOut", methods=["POST"])
def log_out():
    logout_user()
    return json.dumps({})


@app.route("/getUsers", methods=["POST"])
def get_users():
    query = Users.query.all()
    users = []

    for user in query:
        users.append({"username": user.username, "admin": user.admin, "id": user.id, "me": user.id == current_user.id})
    return json.dumps({"users": users})


@app.route("/removeUser", methods=["POST"])
def remove_user():
    data = request.json
    user_id = current_user.id if data["me"] else data["userId"]
    user_to_remove = Users.query.filter_by(id=user_id).first()

    if user_to_remove.admin:
        if not other_admin_exist(user_to_remove.id):
            return json.dumps({"message": "There must be minimum one admin!", "deleted": False})

    if data["me"]:
        logout_user()

    db.session.delete(user_to_remove)
    db.session.commit()
    return json.dumps({"message": "User deleted!", "deleted": True})


@app.route("/changeAdmin", methods=["POST"])
def change_admin():
    data = request.json
    user_id = data["userId"]
    if other_admin_exist(user_id):
        user = Users.query.filter_by(id=user_id).first()
        user.admin = data["value"]
        db.session.commit()
        return json.dumps({"message": "Admin changed", "admin": data["value"]})
    else:
        return json.dumps({"message": "There must be minimum one admin!", "admin": True})


@app.route("/changePassword", methods=["POST"])
def change_password():
    data = request.json
    new_password = data["newPassword"].strip()

    if len(new_password) == 0:
        return json.dumps({"message": "Password can not be empty!"})

    current_user.password = new_password
    db.session.commit()

    return json.dumps({"message": "Password changed!"})


@app.route("/saveImg", methods=["POST"])
def save_img():
    # old_img = request.form["oldImage"]
    #
    # if exists("img/" + old_img):
    #     os.remove("img/" + old_img)


    img = request.files["img"]

    new_filename = img.filename.split(".")[0]
    extension = img.filename.split(".")[1]

    '''
    new_full_filename = new_filename
    new_filename_number = 0
    while exists("img/" + new_full_filename + "." + extension):
        new_full_filename = new_filename + str(new_filename_number)
        new_filename_number += 1


    img.save("img/" + new_full_filename + "." + extension)
    '''
    
    img.save("img/" + new_filename + "." + extension)


    return json.dumps({"image": new_filename + "." + extension})

@app.route("/getImg", methods=["POST"])
def get_img():
    data = request.json
    filename = data["filename"]

    if exists("img/" +filename):
        return send_file("img/" + filename, mimetype='image/gif')

    return send_file("img/none.jpg", mimetype='image/gif')


@app.route("/addComment", methods=["POST"])
def add_comment():
    data = request.json
    new_comment = Comment(article_id=data["articleIndex"], author=current_user.username, text=data["text"])
    db.session.add(new_comment)
    db.session.commit()
    return json.dumps({})


@app.route("/getComments", methods=["POST"])
def get_comments():
    data = request.json
    comments_query = Comment.query.filter_by(article_id=data["index"]).order_by(Comment.add_date.desc())
    comments = []

    for comment in comments_query:
        comments.append({"username": comment.author, "text": comment.text})

    return json.dumps({"comments": comments})



if __name__ == "__main__":
    app.run(debug=True)
