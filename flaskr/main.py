from flaskr import app
from flask import render_template
import sqlite3
from flask import request,redirect,url_for
DATABASE='database.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    con = sqlite3.connect(DATABASE)
    db_quizs = con.execute('SELECT * FROM quizs').fetchall()
    con.close

    quizs=[]
    for row in db_quizs:
        quizs.append({'content':row[0], 'URL':row[1]})
    return render_template('form.html',quizs=quizs)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/register', methods=['POST'])
def register():
    content=request.form['content']
    URL=request.form['URL']

    con=sqlite3.connect(DATABASE)
    con.execute('INSERT INTO quizs VALUES(?, ?)',[content, URL])
    con.commit()
    con.close()
    return redirect(url_for('form'))

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/deleteit', methods=['POST'])
def deleteit():
    con=sqlite3.connect(DATABASE)
    con.execute('DELETE FROM quizs WHERE content="";')
    con.commit()
    con.close()
    return redirect(url_for('form'))


