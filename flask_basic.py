from flask import Flask

app = Flask(__name__)

@app.route("/listnames")
def listnames():
    return "fred, andy, harry"

@app.route("/")
def hello():
    return "hello"

if __name__ == "__main__":
    app.run()