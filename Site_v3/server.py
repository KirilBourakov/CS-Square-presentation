from flask import Flask 
from flask import render_template 

# use flask --app server run --debug to run in debug mode

# initalize an app
app = Flask(__name__)

# when the user goes to a the / route, give them index.html
@app.route("/") 
def index(): 
    return render_template('index.html') 