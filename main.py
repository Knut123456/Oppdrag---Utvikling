from flask import Flask, render_template, request, redirect
from flask_bcrypt import Bcrypt


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

        

if __name__ == '__main__':
    app.run(debug=True)
