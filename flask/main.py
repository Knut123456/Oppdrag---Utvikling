from flask import Flask, render_template, request, redirect, flash
from pathlib import Path

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


from connect_to_database import connect_to_database_def


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/login', methods=['get', "post"])
def login():
    return render_template('login.html')


    
@app.route('/create_account')
def create_account():
    return render_template("create_account.html")  

@app.route('/create_account/form',  methods=["post"])
def create_account_form():
    if request.method == 'POST':
        username = request.form["Username"]
        password = request.form["password"]
        email = request.form["Email"]
        hashed_password = generate_password_hash(password).encode('utf-8')
        if not username or not email or not password:
            flash("all fields is required ")
            redirect("/create_account'")
    return redirect("/")
          




        

if __name__ == '__main__':
    app.run(debug=True)
