from flask import render_template

def index():
   return  render_template('index.html')
   
def room():
    return render_template('room.html')

def systems():
    return render_template('systems.html')

def about():
    return render_template('about.html')
