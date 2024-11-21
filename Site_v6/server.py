import sqlite3
from flask import Flask, render_template, request, jsonify

# use flask --app server run --debug to run in debug mode

# initalize an app
app = Flask(__name__)

database = []

# when the user goes to a the / route, give them index.html
@app.route("/", methods=['GET', 'POST']) 
def index(): 
    # if the method is POST
    if request.method == 'POST':
        # get the JSON sent in the request
        json = request.get_json()
        # if the title and content are not empty
        if json['title'] != '' and json['content'] != '':
            # add the content to the database 
            database.append({
                'title': json['title'],
                'content': json['content']
            })
        # return the database, as JSON
        return jsonify(database)
    # if the request is GET
    else:
        # preprocess and return the index page
        return render_template('index.html', posts=database) 