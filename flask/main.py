from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from connect_to_database import connect_to_database_def
from waitress import serve
from flask_session import Session

from secret import SECRET_KEY

secret_key = SECRET_KEY

app = Flask(__name__) 
app.secret_key = f'{secret_key}'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    if not session.get("name"):
        flash("du må logge inn")
        return redirect("/login")
    return render_template('index.html') 

@app.route('/index/form',  methods=["post"])
def index_form():
    if request.method == 'POST': # tar inn username, password og email
        Kildespråk = request.form["Kildespråk"] 
        oversettelse = request.form["oversettelse"]
        Bok = request.form["Bok"]
        kunde_id = session.get("id")
        conn = connect_to_database_def() # gir meg connection basert på koden i functionen
        cur = conn.cursor() 
        
        query = (
            "INSERT INTO book "
            "(`Kildespråk`, `oversettelse`, `Bok`, `kunde_id`) "
            "VALUES (%s, %s, %s, %s)"
        )
        val = (Kildespråk, oversettelse, Bok, kunde_id)

        cur.execute(query, val) 
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/")  

@app.route('/login', methods=['get', "post"])
def login():
    return render_template('login.html')


# tar inn login form med username og password 
@app.route('/login/form',  methods=["post"])
def login_form():
    if request.method == 'POST': 
        username = request.form["username"] 
        password = request.form["password"]

        conn = connect_to_database_def() # gir meg connection basert på koden i functionen
        cur = conn.cursor() # gjør slik at jeg can fetchall
        
        try:
            query = "SELECT * FROM users WHERE username = %s"
            val = (username,)
            cur.execute(query, val)
            logins = cur.fetchall()
            if not logins: ## skjekker om det er noe i varibelen
                print("No user found with that username.")
            for login in logins:
                password_database = login[3]
                if check_password_hash (password_database, password):
                    print("kan logge seg inn")
                    username_database = login[1]
                    role = login[4]
                    id = login[0]
                    session["name"] = username_database
                    session["id"] = id
                    print(role)
                    return redirect("/")   
                else:
                    print("kan ikke logge sin inn")
                    flash("username eller passord er feil")
                    return redirect("/login")    
        finally:
            cur.close() # lokker det
            conn.close()
            
        
        
@app.route('/create_account')
def create_account():
    return render_template("create_account.html")  

@app.route('/create_account/form',  methods=["post"])
def create_account_form():
    if request.method == 'POST': # tar inn username, password og email
        username = request.form["Username"]
        
        password = request.form["password"]
        email = request.form["Email"]
        hashed_password = generate_password_hash(password) #kryptere passord
        print(hashed_password)
        conn = connect_to_database_def()
        cur = conn.cursor()
        Select_query = f"SELECT username FROM users WHERE username = '{username}'"
        cur.execute(Select_query) 
        username_databases = cur.fetchall()
        if username_databases == []: # skjekker om username er likt og vis det ikke er noe sånn er at den er tom så insert then
            query = (
            "INSERT INTO users"
            "(`username`, `password`, `email`) "
            "VALUES (%s, %s, %s)"
            )
            val = (username, hashed_password, email)

            cur.execute(query, val) 
            print(query)
            conn.commit()
            cur.close()
            conn.close()
        if username_databases  != []:# vis det er allerede en username så skal de lage en nye bruker
            flash("Det finnes allerede")
            return redirect("/create_account") 
        return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)