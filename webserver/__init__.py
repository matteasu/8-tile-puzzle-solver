import os
from flask import Flask
from flask_bootstrap import Bootstrap5
from . import home


def create_app(test_config=None):
    """
    Function responsible for creating and initializing the Flask Web-Server
    :param test_config:
    :return: Instance to the flask app
    """
    # actual initialization
    app = Flask(__name__, instance_relative_config=True)
    # loading Bootstrap 5 dependencies inside the application
    bootstrap = Bootstrap5(app)
    app.config.from_mapping(SECRET_KEY="dev")
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # adding the Home blueprint that defines the application logic
    app.register_blueprint(home.bp)

    return app


if __name__ == "__main__":
    # loads the app if this module is executed as main
    create_app()
