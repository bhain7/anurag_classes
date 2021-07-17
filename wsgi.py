from flask import Flask, render_template, request, redirect
from model.db import init_db, register_user
from model.ease import UserValidator


# we will create an instance of Flask

app = Flask(__name__)

init_db()

# https://example.com/search
@app.route('/') # registering a route to our flask app
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    try:
        name = request.form.get('username') # accessing the user's name
        email = request.form.get("email") # accessing the user's email
        password = request.form.get("password")
        validate = UserValidator(name, email, password)
        print("I am here in the code")
        print(validate.name)
        if validate.valid:
            print("running validating")
            return str(register_user(validate.data()))
        else:
            print("User not registered")
            return validate.msg
            

    except Exception as e:
        print(e)
        return "error occured"


@app.route("/registered")
def registered():
    return f"registered successfully. <a href='{request.host_url}'>Click Here</a>"

if __name__ == "__main__":
    app.run(debug=True)

# we have to push this on server and then deploy it and then use it from there