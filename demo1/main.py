from flask import Flask, render_template, request
from flask_bcrypt import generate_password_hash

app = Flask(__name__)

@app.route('/')
def homepage():
    #return "Hello World"
    return render_template("demo.html")

@app.route('/easy', methods = ["POST", "GET"])
def secondPage():
    if request.method == "POST":
        name = request.form.get("firstName")
        password = request.form.get("password")
        print(name, password, generate_password_hash(password))
    return render_template("demopage2.html")

if __name__ == '__main__':
    app.run(debug=True)