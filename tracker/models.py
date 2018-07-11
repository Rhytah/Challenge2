
class User():
    def __init__(self, userId,userName,department,email,password):
        self.userId =userId
        self.userName = userName 
        self.department = department
        self.email= email
        self.password = password

    def get_userId(self):
        return self.userId
        
    def get_userName(self):
        return self.userName

    def get_department(self):
        return self.department

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

users =[]

class Request():
    def __init__(self,requestId,description,requestOrigin,category,requestDate):
        self.requestId= requestId 
        self.description= description
        self.requestOrigin =requestOrigin
        self.category =category
        self.requestDate = requestDate 

    def get_requestId(self):
        return self.requestId

    def get_description(self):
        return self.description

    def get_requestOrigin(self):
        return self.requestOrigin

    def get_category(self):
        return self.category

    def get_requestDate(self):
        return self.requestDate

    def modify_request(self, requestId,description,requestOrigin,category,requestDate):
        requestId =int(requestId)
        new_requestInput = {}
        if len(requests)>0 and requestId<= len(requests):
            new_requestInput = {
                'requestId':requestId,
                'description': self.description,
                'requestOrigin': self.requestOrigin,
                'category': self.category,
                'requestDate':self.requestDate
                
            }
            requests[requestId]=new_requestInput
            return new_requestInput
        return  new_requestInput

    def __repr__(self):
        return repr(self.__dict__)
requests=[]
