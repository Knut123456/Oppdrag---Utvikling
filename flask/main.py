from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from connect_to_database import connect_to_database_def

from flask_session import Session

from secret import SECRET_KEY

secret_key = SECRET_KEY
conn = connect_to_database_def()

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
        kunde = session.get("name")
        print(kunde)
        conn = connect_to_database_def() # gir meg connection basert på koden i functionen
        cur = conn.cursor() 
        
        query = f'INSERT INTO book (Kildespråk, oversettelse, Bok, kunde) VALUES ("{Kildespråk}", "{oversettelse}", "{Bok}", "{kunde}")'
        cur.execute(query)
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
        session["name"] = username

        hashed_password = generate_password_hash(password).encode('utf-8') # hashed databasen
        conn = connect_to_database_def() # gir meg connection basert på koden i functionen
        cur = conn.cursor() # gjør slik at jeg can fetchall
        
        try:
            Select_query = f"SELECT * FROM users WHERE username = '{username}'"
            
            cur.execute(Select_query)
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                #print(f"{row}")
                password_database = row[3]
                print(password_database)
                print(password)
                if password_database != hashed_password:
                    print("kan ikke logge sin inn")
                    flash("username eller passord er feil")
                    return redirect("/login") 
            if rows is []:
                print("No user found with that username.")
            #password = rows[3]
            print(password)

            
                
        finally:
            cur.close() # lokker det
            conn.close()

        print("kan logge seg inn") # greide å logge inn
        return redirect("/")    
    
@app.route('/create_account')
def create_account():
    return render_template("create_account.html")  

@app.route('/create_account/form',  methods=["post"])
def create_account_form():
    if request.method == 'POST': # tar inn username, password og email
        username = request.form["Username"]
        
        password = request.form["password"]
        email = request.form["Email"]
        hashed_password = generate_password_hash(password).encode('utf-8') #kryptere passord
        conn = connect_to_database_def()
        cur = conn.cursor()
        Select_query = f"SELECT username FROM users WHERE username = '{username}'"
        cur.execute(Select_query) 
        username_databases = cur.fetchall()
        print(username_databases)
        if username_databases == []: # skjekker om det ikke er noe med denne username
            query = f'INSERT INTO users (username, password, email) VALUES ("{username}", "{hashed_password}", "{email}")'
            print(query)
            session["name"] = username
            cur.execute(query)
            conn.commit()

            cur.close()
            conn.close()
        if username_databases  != []:# vis det er allerede en username så skal de lage en nye bruker
            flash("Det er allerede et username")
            return redirect("/create_account") 


            
        return redirect("/")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
