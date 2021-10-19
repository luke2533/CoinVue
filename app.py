import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")

@app.route("/coin_vue")
def coin_vue():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/discover")
def discover():
    return render_template("discover.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #check if username already exists in db
        # existing_user = mongo.db.users.find_one(
        #     {"username": request.form.get("username").lower()})

        # if existing_user:
        #     flash("Username already exists")
        #     return redirect(url_for("signup"))

        # This is where you will put password and email authentication
        password = request.form.get("password")
        check_password = request.form.get("confirm-password")
        email = request.form.get("email")
        check_email = request.form.get("confirm-email")

        if password != check_password:
            flash("Please make sure the passwords match")
            return redirect(url_for("signup"))

        if email != check_email:
            flash("Please make sure the emails match")
            return redirect(url_for("signup"))


        new_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)


        session["user"] = request.form.get("username").lower()
        flash("Register complete")
    return render_template("signup.html")
#  Includes refrences to code instuite flask mini project 2c - Register functionalty 



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

# Credited to the flask mini project code instuitue