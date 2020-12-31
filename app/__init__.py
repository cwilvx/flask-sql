from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='db.sqlite'
    )

    from . import db
    db.init_app(app)

    from . import add_things
    app.register_blueprint(add_things.bp)

    return app