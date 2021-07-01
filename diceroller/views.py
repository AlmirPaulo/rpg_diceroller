from flask import render_template, Blueprint

views = Blueprint('views', __name__)

def index():
   return  render_template('index.html')
   
def room():
    return render_template('room.html')

@views.route('/systems')
def systems():
    return render_template('systems.html')

@views.route('/about')
def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')
