from flask import Flask
from flask_restful import Resource, Api


class Employees(Resource):
    def get(self):
        return "you got me"


class Tracks(Resource):
    def get(self):
        return {'data': {'xxx': 'yyyyyyyy'}}


def serve_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Employees, "/")  # Route_1
    api.add_resource(Tracks, "/tracks")  # Route_2
    app.run(port="5000")


if __name__ == "__main__":
    serve_app()