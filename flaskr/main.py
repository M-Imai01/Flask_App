from flaskr import app
from flask import render_template

@app.route('/')
def index():
    books = [
        {'title': 'はらぺこあおむし',
         'price': 1200,
         'arrival_day': '2020年7月12日'},
        {'title': 'ぐりとぐら',
         'price': 990,
         'arrival_day': '2020年7月13日'},
    ]
    return render_template(
        'index.html',
        books=books
    )