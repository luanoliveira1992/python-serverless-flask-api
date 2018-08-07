import os
from flask import Flask
from app.routes.apiv1 import api_v1
from flask import redirect
from app.extensions import cors
from app.extensions import restplus


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    register_extensions(app)
    return app


def register_blueprint(application):
    restplus.add_namespace(api_v1, path="/"+os.environ['STAGE']+"/api/v1")

def register_extensions(application):
    restplus.init_app(application)
    cors.init_app(application)
    
appl = create_app()

@appl.route('/'+os.environ['STAGE'])
def redirect_to_default_api():
    return redirect(os.environ['STAGE']+'/api/v1')


if __name__ == '__main__':
    appl.run()
    
