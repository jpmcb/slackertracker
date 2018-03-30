from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def hello():
    return('Hello World!')
