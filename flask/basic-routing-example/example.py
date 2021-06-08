from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def root():
    return "<h1> ROOT! </h1>"

@app.route("/hello")
def hello():
    return "<h1> Hello World! </h1>"

# Pass variable
@app.route("/user/<username>")
def user(username):
    return f"<h1> The User name is {username} </h1>"

# Specify variable type with converter
@app.route("/id/<int:user_id>")
def get_user_id(user_id):
    is_int = isinstance(user_id, int)
    return f"<h1> The type of user id is int: {is_int} </h1>"

# Return json type
@app.route("/json")
def get_json():
    user_dict = {
        "1" : "enfow",
        "2" : "curt",
    }
    return jsonify(user_dict)

if __name__ == "__main__":
    host_addr = "0.0.0.0"
    port_num = "8080"
    # run server
    app.run(host=host_addr, port=port_num, debug=True)
