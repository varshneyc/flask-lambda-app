from flask import Flask
from aws_lambda_wsgi import response  

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on Lambda!"

def handler(event,context):
    return response(app, event, context)
