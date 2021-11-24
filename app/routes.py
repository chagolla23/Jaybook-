from app import app
from flask import render_template
from datetime import date, datetime
from app.models import Post

@app.route('/')
def home():
    context = {
        'first_name': 'Jon',
        'last_name': 'Chagolla',
        'email': 'chagolla2345@gmail.com',
        'posts': Post.query.all()       
    }
    return render_template('index.html', **context)

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/register')
def register():
    return render_template('register.html')


        

