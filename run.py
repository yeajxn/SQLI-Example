from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

#Renna bb
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        name = request.form['name']
        insert_user(name)
        return render_template('registered.html', name=name)

@app.route('/users')
def get_users():
    conn = None
    try:
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        rows = cur.execute('SELECT name from users')
        names = rows.fetchall()
        print(names)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            return render_template('users.html', names=names)


def insert_user(name):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        #Create Table
        #cur.execute('CREATE TABLE users (id int, name text)')
        cur.executescript(f"INSERT INTO users (name) VALUES('{name}')")
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

app.run(debug=True)