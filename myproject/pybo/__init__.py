from flask import Flask
# --------------------------------- [edit] ---------------------------------- #
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
import config

db = SQLAlchemy()
migrate = Migrate()
# --------------------------------------------------------------------------- #
# --------------------------------- [edit] ---------------------------------- #
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    #ORM

    db.init_app(app)
    migrate.init_app(app,db)
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    from . import models

    #blueprint

    from .views import main_views, question_views, answer_views
    
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app
# --------------------------------------------------------------------------- #
