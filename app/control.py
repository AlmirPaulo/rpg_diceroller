from flask import Blueprint
from . import views

control = Blueprint('control', __name__)

@control.route('/', methods=['GET', 'POST'])
def index():
    return views.index()

#@control.route('/room')
#def room():
#    return views.room()
