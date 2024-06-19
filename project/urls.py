import home_page,shop_page
import shop_page

from .settings import project

home_page.home.add_url_rule(rule= "/", view_func= home_page.show_home_page, methods = ["GET", "POST"])

project.register_blueprint(blueprint = home_page.home)

shop_page.shop.add_url_rule(rule = "/shop/", view_func = shop_page.show_shop_page, methods = ['GET', 'POST'])

project.register_blueprint(blueprint = shop_page.shop)
