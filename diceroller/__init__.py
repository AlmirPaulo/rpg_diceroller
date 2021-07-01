from flask import Flask
from flask_sock import Sock
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO()


#Factory
def create_app():
    #imports
    from . import views, rooms
    from .rooms import room_bp 
    from .views import views 

    #configurations
    app.config['SECRET_KEY'] = '...'
    
    #initializations
    socket.init_app(app)

    #register Blueprints
    app.register_blueprint(room_bp, url_prefix='/') 
    app.register_blueprint(views, url_prefix='/') 

    return app
