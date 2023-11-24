from flask import Flask
from app.middleware import PrefixMiddleware

application = Flask(__name__)

# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)
application.config['SECRET_KEY'] = b'DTPGROUP5!!!'

from app import routes