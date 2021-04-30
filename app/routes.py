from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world():
    my_reponse = "Hello, World!"
    return my_reponse

@hello_world_bp.route('/hello-world/JSON', methods=["GET"])
def say_hello_json():
    return {
        "name": "chilicious!",
        "message": "HELLO!",
        "hobbies": ["Dancing", "Exploring food", "Coffee"]
    }, 200

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"] + [new_hobby] 
    return response_body
