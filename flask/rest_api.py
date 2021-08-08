from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def get_root():
    return "<h1> RESTAPI EXAMPLE </h1>"

@app.route("/json")
def get_json():
    user_dict = {
        "1" : "enfow",
        "2" : "curt",
    }
    return jsonify(user_dict)

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port ="8080")
