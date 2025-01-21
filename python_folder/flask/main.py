from flask import Flask, render_template, request, redirect
from flask_bcrypt import Bcrypt
from ..connect_to_database import connect_to_database_def


app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form["Username"]
        password = request.form["password"]
        hashed_password = Bcrypt.check_password_hash(password).decode('utf-8')
        if username in users and users[username] == hashed_password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

        

if __name__ == '__main__':
    app.run(debug=True)
