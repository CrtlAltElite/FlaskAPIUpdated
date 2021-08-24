from flask import Blueprint

bp = Blueprint('api',__name__, url_prefix='/api')

from .import social_routes, shop_routes, auth_routes, models