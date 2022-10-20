from flaskr import app
from flask import render_template

@app.route('/')
def index():
    book = {
        'title': 'はらぺこあおむし',
        'price': 1200,
        'arrival_day': '2020年7月12日'
    }
    return render_template(
        'index.html',
        book=book
    )