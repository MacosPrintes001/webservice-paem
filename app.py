from flask import Flask

application = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello Flask Application on AWS."

if __name__ =="__main__":
    application.run()