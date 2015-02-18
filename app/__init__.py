from flask import Flask, jsonify

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)
    register_errorhandlers(app)
    return app

def register_blueprints(app):
    """ Register routes to app """
    from .grandma import blueprint as grandma_blueprint
    app.register_blueprint(grandma_blueprint)

def register_errorhandlers(app):
    """ Custom Error Pages """
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return jsonify({ 'error': error_code}), error_code

    for errcode in [401, 403, 404, 500]:
        app.errorhandler(errcode)(render_error)

