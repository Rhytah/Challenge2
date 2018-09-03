from flask import Flask,  json, request, jsonify
from .models import Request,requests, User, users
import re


app = Flask(__name__)

app.config['SECRET_KEY'] ='thisissecret'

@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_user_requests():
   
    if len(requests) <1:
        return jsonify({
            'status': 'Fail',
            'message':'You have no requests'}),404
    
    if len(requests)>= 1:
        return jsonify({
            'status': 'Pass',
            'message': 'You have successfully fetched requests.',
            'requests': [
                my_request.__dict__ for my_request in requests
            ]
        }),200
    return jsonify({"message": 'Failed to get any requests'}),400

@app.route('/api/v1/users/requests/<requestId>', methods = ['GET'])
def get_a_request_for_user(requestId):

    if len(requests)<1:
        return jsonify({
            "Status":"Fail",
            "message":"Request not found"
        }), 404

    for my_request in requests:
        if my_request.requestId == requestId:
            return my_request,200

    return jsonify({"input error":"Request not found, check id used"})
   
@app.route('/api/v1/users/requests', methods =['POST'])
def create_a_request():
    request_data = request.get_json()        
    employeeName = request_data.get('employeeName')
    requestId = len (requests) +1
    description = request_data.get('description')
    category = request_data.get('category')
    requestDate = request_data.get('requestDate')

    if not request_data:
        return jsonify({'message':'All feilds are required'}),400

    if not employeeName or employeeName == ' ' or employeeName == type (int):
        return jsonify({'message':'Employee Name is required'}),400

    if not description or description == ' ' :
        return jsonify({'message': 'Resquest description is required'}),400
        
    if not category or category=='':
        return jsonify({'message':'Request Category is required'}),400

    if not requestDate or requestDate =='':
        return jsonify({'message':'When was the request logged?'}),400

    new_request =Request(requestId, description,employeeName, category, requestDate)
    requests.append(new_request)

    return jsonify({'message':f'Hello {employeeName}! Request succesfully created'})

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

@app.route('/auth/register', methods=['POST']) 
def register_user():
    user_data= request.get_json()  #getting user data
    name=user_data.get('name')
    userName =str(user_data.get('userName')).strip()
    department =user_data.get('department')
    password = user_data.get('password')
    userId = len(users) + 1

    if not user_data:
        return jsonify({'message':'All fields are required'})

    if not name or name==" " or name == type(int) or len(name) <3:
        return jsonify({'message': "Incorrect Name"})

   
    if not userName or userName == '' :
        return jsonify({'message':'Invalid Username'})

    if not password or password=='' or len(password) <8:
        return jsonify({'message':"Incorrect Password"})

    new_user =User(userId,userName,department,password)
    users.append(new_user)  

    return jsonify({'message': f'User {userName} has successfully been created'}) 

@app.route('/auth/login', methods=['POST'])
def login_user():
    user_data = request.get_json()
    userName= str(user_data.get('userName')).strip()
    password = user_data.get('password')

    if not user_data:
        return jsonify({"Missing":'All fields are required'}),400

    if not userName :
        return jsonify({'Missing':'User Name is required'}),400
    
    if not password or password =='':
        return jsonify({'Missing':'Password is required to login'}),400
    
    return jsonify({'message':f'Welcome {userName}. You are now logged in'}), 200





#if __name__=='__main__':
 #   app.run(debug=True)

