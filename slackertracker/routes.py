from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/api/slack')
def show():
    return("Hello!")