from flask import Flask, g, flash, redirect, render_template, \
     request, url_for
import sqlite3, json

#Global variable for db
DATABASE = 'safari.db'

app = Flask(__name__)

#need to take in parameter/variable
@app.route('/')
def index():
    #initialize empty data array (local)
    data = []
    for animal in query_db('select * from animals'):
        #print( animal[1], '-', animal[0] )
        data.append({'id': animal[0], 'name': animal[1], 'description': animal[2]})


    #
    return render_template(
        'index.html', data = data)
    #   data=[{'Id':'1', 'name' : 'Bird'}, {'Id':'2', 'name':'Dog'}, {'Id':'3','name':'Cat'}, {'Id':'4','name':'Bear'},
    #     {'Id': '5', 'name': 'Fish'}])     #array of JSON rows

# makes window to print value of select box
@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

#in case of emergency
@app.route("/guide")
def guide():
    return("I'm your guide.")

#Route values to results of query
@app.route('/<animal_id>')
def animal_page(animal_id):
    try:
        int(animal_id)
        animal = query_db('select * from animals WHERE animal_id = ' + animal_id)
        return str(animal)
    except:
        return "Need an INT"

# Returning an array (compendium of animals)
@app.route('/allAnimals')
def allAnimals():
    #initialize empty data array (local)
    data = []
    for animal in query_db('select * from animals'):
        #print( animal[1], '-', animal[0] )
        data.append({'id': animal[0], 'name': animal[1], 'description': animal[2]})
    # convert data (sql result) to JSON
    my_json_string = json.dumps(data)
    return str(my_json_string)

#database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#use get_db to run query
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#close db connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__=='__main__':
    app.run(debug=True)
