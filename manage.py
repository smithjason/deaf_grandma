#!/usr/bin/env python

"""
Usage: ./manage.py [submanager] <command>
Manage script for development.  Type ./manage.py for more info
"""

from flask import render_template
from flask_script import Manager
from flask_script.commands import ShowUrls

from app import create_app
from app.settings import app_config

app = create_app(app_config)
manager = Manager(app)

if __name__ == '__main__':
  manager.run()
