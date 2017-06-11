from flask import Flask
from flask import render_template

# Initialize the app
app = Flask(__name__)
app.debug = True

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run()