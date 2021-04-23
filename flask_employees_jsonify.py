from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import jsonify


class Employees(Resource):
    def get(self):
        db_connect = create_engine("sqlite:///chinook.db")
        conn = db_connect.connect()
        query = conn.execute("select * from employees")
        result = {"employees": [i[0] for i in query.cursor.fetchall()]} # dict where key "employees" has value
        # list of all first column entries(?) in the database
        conn.close()
        db_connect.dispose()
        return jsonify(result)


class Tracks(Resource):
    def get(self):
        db_connect = create_engine("sqlite:///chinook.db")
        conn = db_connect.connect()
        query = conn.execute(
            "select trackid, name, composer, unitprice from tracks;"
        )
        result = {"data": [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        conn.close()
        db_connect.dispose()
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id: int):
        db_connect = create_engine("sqlite:///chinook.db")
        conn = db_connect.connect()
        query = conn.execute(
            "select * from employees where EmployeeId =%d " % int(employee_id)
        )
        result = {"data": [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        conn.close()
        db_connect.dispose()
        return jsonify(result)


def serve_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Employees, "/employees")  # Route_1
    api.add_resource(Tracks, "/tracks")  # Route_2
    api.add_resource(Employees_Name, "/employees/<employee_id>")  # Route_3
    app.run(port="5000")


if __name__ == "__main__":
    serve_app()