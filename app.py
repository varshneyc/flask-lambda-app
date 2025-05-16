from flask import Flask
from mangum import Mangum  

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on Lambda!"

handler = Mangum(app)
