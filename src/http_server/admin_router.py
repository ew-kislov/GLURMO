from flask import Blueprint

admin_router = Blueprint('admin', __name__)

@admin_router.route('/')
def show():
    return 'admin'