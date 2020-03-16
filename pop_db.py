#must run first to populate database

import sqlite3

#connect to db
conn = sqlite3.connect('safari.db')

#cursor Object to execute individual statements
cursor = conn.cursor()

#run SQL to create the table, use IF NOT EXISTS so when rerunning it doesn't throw 'already exists' error
cursor.execute('''
CREATE TABLE IF NOT EXISTS animals (
    animal_id   INTEGER PRIMARY KEY,
    animal      TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL
);
''')

# Wipe out records cause we reload them next
cursor.execute('''
DELETE FROM animals;
''')

# Insert records following the column names and datatypes specified in table above
cursor.execute('''
INSERT INTO animals (animal_id,animal,description)
VALUES
   (1,  'Bird' , 'Feathery, loud'),
   (2,  'Dog' ,'Furry, loud'),
   (3,  'Cat' ,'Furry, quiet'),
   (4,  'Bear' ,'Furry, very loud'),
   (5,  'Fish' ,'Slimy, quiet'),
   (6,  'Salamander' ,'Slimy, quiet'),
   (7,  'Sugar Glider' ,'Airborne, skreetchy'),
   (8,  'Squirrel' ,'Furry, quiet'),
   (9,  'Plant' ,'No data, quiet'),
   (10,  'Dinosaur' ,'No data, not found');

''')

conn.commit()    # COMMIT the data inserted 


conn.close()

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('safari.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from animals"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")

        for row in records:
            print(row[0],'-', row[1], '-', row[2])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()
