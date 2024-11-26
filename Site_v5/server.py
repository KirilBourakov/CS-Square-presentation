from flask import Flask, render_template, request

# initalize an app
app = Flask(__name__)

database = []

# when the user goes to a the / route, give them index.html
@app.route("/", methods=['GET', 'POST']) 
def index(): 
    # if the method is POST
    if request.method == 'POST':
        # get the JSON
        json = request.get_json()
        # if the title and content are not empty
        if json['title'] != '' and json['content'] != '':
            # add the content to the database 
            database.append({
                'title': json['title'],
                'content': json['content']
            })
        print(database)
    # preprocess and return the index page
    return render_template('index.html', posts=database) 

app.run()