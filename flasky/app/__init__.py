from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
moment = Moment()

''''
    basically we will be creating application instance based on the environment
    we pass the environment name when creating the application instance
'''


def create_app(config_name):
    app = Flask(__name__)

    '''
         all the configuration settings stored / defined in the config.py can be imported by using the from_object
         function of the app.config.from_object () and passing the configuration / class name
         since development, production classes are subclass of Config class they inherit all the configuration settings
         defined the in parent class  
         instead of importing each setting one by one -> from_object function can do it behind the scene?
         
        config[config_name] will return the value from the map which is a child or sub-class of Config
        as a result we invoke the init_app function on the parent class name config
    '''
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # now app is configured based on the environment configuration - development, production, or testing
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #  attach routes and custom error pages here

    # registering blueprint with the app
    # The blueprint is registered with the application inside the create_app() factory function,
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #  so, what happens if you register the main_blueprint with the application?

    return app
