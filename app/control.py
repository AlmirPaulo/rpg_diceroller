from flask import Blueprint
from . import views

control = Blueprint('control', __name__)

@control.route('/', methods=['GET', 'POST'])
def index():
    return views.index()

@control.route('/room', methods=['GET', 'POST'])
def room():
    return views.room()

@control.route('/systems')
def systems():
    return views.systems()

@control.route('/about')
def about():
    return views.about()
