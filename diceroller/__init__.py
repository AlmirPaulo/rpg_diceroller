from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
socket = Sock()


#Factory
def create_app():
    #imports
    from . import views, control
    from .control import control
    
    #configurations
    app.config['SECRET_KEY'] = '...'
    
    #initializations
    socket.init_app(app)

    #register Blueprints
    app.register_blueprint(control, url_prefix='/') 

    return app
