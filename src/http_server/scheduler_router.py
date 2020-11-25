from flask import Blueprint

scheduler_router = Blueprint('scheduler', __name__)

@scheduler_router.route('/', methods=['GET'])
def show():
    return 'scheduler'