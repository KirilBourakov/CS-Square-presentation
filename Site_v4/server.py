import sqlite3
from flask import Flask 
from flask import render_template 

# use flask --app server run --debug to run in debug mode

# initalize an app
app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, post TEXT)''')
    conn.commit()
    conn.close()

# when the user goes to a the / route, give them index.html
@app.route("/") 
def index(): 
    create_database()
    return render_template('index.html') 


