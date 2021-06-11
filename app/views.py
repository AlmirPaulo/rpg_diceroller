from flask import render_template

def index():
   return  render_template('index.html')
   
def room():
    return render_template('room.html')
