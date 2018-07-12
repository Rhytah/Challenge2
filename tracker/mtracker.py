from flask import Flask,  json, request, jsonify
from models import Request,requests, User, users
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] ='thisissecret'

@app.route('/api/v1/users', methods=['GET'])
def get_all_user():
    return ''

@app.route('/api/v1/users/<userId>', methods=['GET'])
def get_one_user():
    return ''

@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_user_requests():
    if len(requests) >0:
        return jsonify({'messgae': requests})
    else:
        return jsonify({
            'status': 'Fail',
            'message': 'There are no requests found in the system'
        })

@app.route('/api/v1/users/requests/<requestId>', methods = ['GET'])
def get_a_request_for_user(requestId):
    for single_request in requests:
        if single_request.get(id) == requestId:
            return jsonify({'request': single_request})

    return jsonify({
        'status': 'Fail',
        'message': 'That request doesn\'t exist'
    })

@app.route('/api/v1/users/requests', methods =['POST'])
def create_a_request():
    
    return ''

@app.route('/api/v1/users/requests/<requestId>', methods =['PUT'])
def modify_a_request():
    return ''

if __name__=='__main__':
    app.run(debug=True)
