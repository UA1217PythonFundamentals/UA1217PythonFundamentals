from flask import Flask, url_for, request, render_template, redirect
from models import USERS, User

app = Flask(__name__)


@app.route("/")
@app.route("/users")
def get_all_users():

    return render_template('user_list.html', users_data=USERS)


@app.route("/user/", methods=["GET", "POST"])
def user():
    # show the user profile for that user
    if request.method == "GET":
         return render_template('create_user.html')
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user = User.create(username=username, email=email, password=password)

        USERS.append(user)
        return redirect(url_for("get_all_users"))


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80)
    app.run(host="0.0.0.0", port=8080)
