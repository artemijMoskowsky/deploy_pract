import flask
import os

from project.settings import DATABASE
from .models import Product
def show_shop_page():
    # if flask.request.method == "POST" and len(list)
    
    return flask.render_template(template_name_or_list= "shop.html", products = Product.query.all())