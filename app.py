from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World from Flask and Lambda!"

def lambda_handler(event, context):
    from mangum import Mangum
    handler = Mangum(app)
    return handler(event, context)
