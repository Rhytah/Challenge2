from flask import Flask,  json, request, jsonify
from .models import Request,requests, User, users
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
        'message': 'That request doesnot exist'
    })

@app.route('/api/v1/users/requests', methods =['POST'])
def create_a_request():
    request_data = request.get_json()
    employeeName = request_data.get('employeeName')
    requestId = len (requests) +1
    description = request_data.get('description')
    category = request_data.get('category')
    requestDate = request_data.get('requestDate')


    if not employeeName or employeeName == "" or employeeName == type (int):
        return jsonify({'message':'Employee Name is required'})

    if not description or description ==" ":
        return jsonify({'message': 'Resquest description is required'})
        
    if not category or category=='':
        return jsonify({'message':'Request Category is required'})

    if not requestDate or requestDate =='':
        return jsonify({'message':'When was the request logged?'})

    new_request =Request(requestId, description,employeeName, category, requestDate)
    requests.append(new_request)

    return jsonify({'message':'Hello {employeeName}! Request succesfully created'})


@app.route('/api/v1/users/requests/<requestId>', methods =['PUT'])
def modify_a_request(requestId):
    if len(requests)<1:
        return jsonify({
            'status':'Fail',
            'Sorry':"No rquests to modify"
        })
    if len(requests)>=1:
        request_data=request.get_json()
        employeeName=request_data.get('employeeName')
        description=request_data.get('description')
        category= request_data.get('category')
        requestDate= request_data.get('requestDate')

        for my_request in requests:
            if my_request.requestId==int(requestId):
                my_request.employeeName= employeeName
                my_request.description= description
                my_request.category= category
                my_request.requestDate= requestDate
            return jsonify({
                'request':my_request.__dict__,
                'status': 'OK',
                'Congratulations': 'You have completed modification',
            })
        

if __name__=='__main__':
    app.run(debug=True)

