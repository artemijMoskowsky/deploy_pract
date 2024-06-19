import flask

home = flask.Blueprint(
    name = "home",
    import_name = "home_page",
    template_folder = "template",
    static_folder = "static/home"
)