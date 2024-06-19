import flask, os, flask_migrate, flask_sqlalchemy

project = flask.Flask(
    import_name= "project",
    instance_path= os.path.abspath(__file__ + "/.."),
    template_folder= "template"
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(
    app = project
)
migrate = flask_migrate.Migrate(app= project, db = DATABASE)