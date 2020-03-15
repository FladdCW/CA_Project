REQUIREMENTS:
=================
Dynamically loaded web-page with select box
    Ten selections of animals, printed desc.

Database of animals
    Animals represented as array of objects
    Query one or all animals from database
    Display result in web-page



Setup
=================
Download code from Github

Install python v3.x from https://www.python.org/downloads/

Install packages Flask and SQLite
    pip install flask
    pip install sqlite3


Usage/Running it
=================
1. cd to dir

2. run: python Hello_flask.py

    example path from my machine

        C:\Users\Chris\PycharmProjects\animal_proj>python Hello_flask.py
         * Serving Flask app "Hello_flask" (lazy loading)
         * Environment: production
           WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: on
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 855-132-751
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

3. open browser to http://127.0.0.1:5000/
    (note, port may be different, note what script prints on your machine)

4. for JSON output of animal #1 (or others) redirect to :
    http://127.0.0.1:5000/1

5. for all animals redirect to:
    http://127.0.0.1:5000/allAnimals

6. To add/edit/delete animals from database modify pop_db.py (lines 29-38)

