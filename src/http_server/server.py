from flask import Flask
import os

from .admin_router import admin_router
from .scheduler_router import scheduler_router

def run_server():
    app = Flask(__name__)

    app.register_blueprint(admin_router, url_prefix='/admin')
    app.register_blueprint(scheduler_router, url_prefix='/scheduler')

    app.run(host='127.0.0.1', port=os.getenv("API_PORT"))