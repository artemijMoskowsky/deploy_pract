import flask

from project.settings import DATABASE
from shop_page.models import Product
import os

def show_home_page():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        new_product = Product(
            name = name
        )
        image = flask.request.files['img']
        image.save(os.path.abspath(__file__ + f'/../../shop_page/static/images/{name}.png'))
        DATABASE.session.add(new_product)
        DATABASE.session.commit()
        

    return flask.render_template("home.html")