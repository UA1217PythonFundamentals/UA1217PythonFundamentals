from flask import Flask, url_for, request
from models import USERS, User

my_app = Flask(__name__)


@my_app.route("/")
def hello_world():
    return "Hello, World!"


@my_app.route("/users")
def get_all_users():
    return [u.to_dict() for u in USERS]


@my_app.route("/user/<int:user_id>", methods=["GET", "POST"])
def user(user_id):
    # show the user profile for that user
    if request.method == "GET":
        data = {}
        for user in USERS:
            if user.pk == user_id:
                data = user.to_dict()

        return data
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user = User.create(username=username, email=email, password=password)
        print(user)
        USERS.append(user)
        return user.to_dict()

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80)
    with my_app.test_request_context():
        print(url_for("hello_world"))
        print(url_for("get_all_users"))
        print(url_for("user", user_id=9))

    my_app.run(host="0.0.0.0", port=8080)
