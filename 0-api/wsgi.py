from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data["email"]
    password = data["password"]

    result = False
    if email == "ruben.cadenas@hotmail.com" and password == "admin":
        result = True
    
    rtn = {
        'ok': True,
        'result': result
    }

    return jsonify(rtn), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
