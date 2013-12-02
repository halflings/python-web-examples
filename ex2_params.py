from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    if 'name' in request.args:
        return "Hello {}!".format(request.args['name'])
    else:
        return "Missing 'name' argument !"

if __name__ == "__main__":
    app.run()
