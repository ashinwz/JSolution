from flask import Blueprint

blueprint = Blueprint(
    'Doc',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)