from flask import flask
from flask_restplus import api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        
        self.api = Api(self.app,
            version="1.0",
            title="Simple book API",
            decription="A simple book API",
            doc="/docs",
        )

    def run(self, ):
        self.app.run(
            debug=True
        )