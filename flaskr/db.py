import sqlite3

DATABASE='database.db'

def create_quizs_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS quizs (content, URL)")
    con.close()
