import sqlite3
from flask import Flask, render_template, request

# use flask --app server run --debug to run in debug mode

# initalize an app
app = Flask(__name__)

database = []

# when the user goes to a the / route, give them index.html
@app.route("/", methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
        if request.form['title'] != '' and request.form['content'] != '':
            database.append({
                'title': request.form['title'],
                'content': request.form['content']
            })
        print(database)
    return render_template('index.html', posts=database) 