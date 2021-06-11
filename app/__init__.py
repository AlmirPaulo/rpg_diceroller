from flask import Flask

app = Flask(__name__)

#Factory
def create_app():
    #imports
    from . import views, control
    from .control import control
    
    #configurations
    app.config['SECRET_KEY'] = '...'
    
    #register Blueprints
    app.register_blueprint(control, url_prefix='/') 

    return app
