from flask import Flask

from http_server.admin_router import admin_router
from http_server.scheduler_router import scheduler_router

def run_server():
    app = Flask(__name__)

    app.register_blueprint(admin_router, url_prefix='/admin')
    app.register_blueprint(scheduler_router, url_prefix='/scheduler')

    app.run(host='127.0.0.1', port=3000)