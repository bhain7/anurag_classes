from flask import Flask, render_template, request, redirect

# we will create an instance of Flask

app = Flask(__name__)

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

        print(f"Name: {name}, Email: {email}, Password: {password}")
        return redirect("/registered")
    except:
        return "error occured"


@app.route("/registered")
def registered():
    return f"registered successfully. <a href='{request.host_url}'>Click Here</a>"

if __name__ == "__main__":
    app.run(debug=True)

# we have to push this on server and then deploy it and then use it from there