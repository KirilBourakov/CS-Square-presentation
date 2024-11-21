import sqlite3
from flask import Flask, render_template, request, jsonify

# use flask --app server run --debug to run in debug mode

# initalize an app
app = Flask(__name__)

database = []

# when the user goes to a the / route, give them index.html
@app.route("/", methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
        json = request.get_json()
        if json['title'] != '' and json['content'] != '':
            database.append({
                'title': json['title'],
                'content': json['content']
            })
        return jsonify(database)
    else:
        return render_template('index.html', posts=database) 

app.run(host='0.0.0.0')