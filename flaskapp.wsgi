#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/vagrant/")

from app import app as application
application.secret_key = 'disel'
