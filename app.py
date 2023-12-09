from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Index page

@app.route("/")
def home():

    return render_template("index.html")


# Login page
@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":

        # Storage data of mail and username in a variable

        name = request.form["user"]
        mail = request.form["mail"]

        # Pass this information and storage it in the server "temporarily"

        session["user"] = name
        session["mail"] = mail


        # Flash message saying that the log in was successful
        flash("The login was successful!")
        return redirect(url_for("user"))
    else: 

        # In case that the user is already logged in redirect to user page
        if "user" in session and "mail" in session:

            # Flashing message saying that there's a user in the page
            flash(f"The user {name} is already logged in!")
        return render_template("login.html")
    

# Logout page
@app.route("/logout")
def logout():

    # If there's any user in session the user will be deleted and the page redirected to the index page
    if "user" in session and "mail" in session:

        del session["user"]
        del session["mail"]

        # Flashing message that the user has logged out successfully

        flash("The user logged out successfully")

        # Redirect to home page

        return redirect(url_for("home"))
    
# User page
@app.route("/user")
def user():

    if "user" in session and "mail" in session:

        # Pulling data storaged in the server "temporarily"
        name = session["user"]
        mail = session["mail"]

        return render_template("user.html", name=name, mail=mail)
    
    else:

        # Flash message saying that no user is logged in

        flash("No user found in the server!")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)