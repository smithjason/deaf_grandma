import os
import logging

class Config(object):
    # Controls whether web interfance users are in Flask debug mode
    # (e.g. Werkzeug stack trace console, unminified assets)
    DEBUG = False

    # Manually set version
    VERSION = '1.0'
    APP_NAME = 'webwidget-service'

    # Encryption key used to sign Flask session cookies
    # We generate a random one using os.urandom(24)
    SECRET_KEY = 'cjcijr99afweaZlZt+nHYvGKqEHbTGCA'

    # We pretty much want to see all messages logged by our app handler
    APP_LOG_LEVEL = logging.DEBUG


    # This is more useful than the default format
    STDERR_LOG_FORMAT = ('%(asctime)s %(levelname)s %(message)s', '%m/%d/%Y %I:%M:%S %p')

    # These directories are useful to reference elsewhere
    APP_DIR = os.path.dirname(os.path.abspath(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    STATIC_DIR = os.path.join(APP_DIR, 'static')


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    TESTING = True


class StageConfig(Config):
    ENV = 'stage'


class ProductionConfig(Config):
    ENV = 'prod'

    # Don't need to see debug messages in production
    APP_LOG_LEVEL = logging.INFO



config_dict = {
    'dev': DevelopmentConfig,
    'stage': StageConfig,
    'prod': ProductionConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}

app_config = config_dict[os.getenv('APP_ENV') or 'default']
