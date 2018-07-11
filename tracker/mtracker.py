from flask import Flask,json, jsonify
from .models import Request, User

app = Flask(__name__)

app.config['SECRET_KEY'] ='thisissecret'

@app.route('/users', methods=['GET'])
def get_all_user():
    return ''

@app.route('/users/<userId>', methods=['GET'])
def get_one_user():
    return ''

@app.route('/users/requests', methods=['GET'])
def get_all_user_requests():
    return ''

@app.route('/users/requests/<requestId>', methods = ['GET'])
def get_a_request_for_user():
    return ''

@app.route('users/requests', methods =['POST'])
def create_a_request():
    
    return ''

@app.route('users/requests/<requestId>', methods =['PUT'])
def modify_a_request():
    return ''

if __name__=='__main__':
    app.run(debug=True)
