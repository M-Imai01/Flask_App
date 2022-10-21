from flaskr import app
from flask import render_template
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()
    
    books = [
        # {'title': 'はらぺこあおむし',
        #  'price': 1200,
        #  'arrival_day': '2020年7月12日'},
        # {'title': 'ぐりとぐら',
        #  'price': 990,
        #  'arrival_day': '2020年7月13日'},
    ]
    for row in db_books:
        books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})
    
    return render_template(
        'index.html',
        books=books
    )
    
@app.route('/form')
def form():
        return render_template(
        'form.html'
    )