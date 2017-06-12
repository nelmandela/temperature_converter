from flask import Flask
from flask import render_template, request

# Initialize the app
app = Flask(__name__)
app.debug = True

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        return render_template("signup.html")
    else:
        return render_template("signup.html")

if __name__ == '__main__':
    app.run()