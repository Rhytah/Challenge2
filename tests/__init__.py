from tracker.mtracker import app
from tracker.models import User, Request, users, requests

import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.user_data = {
            "user_id": 1,
            "name": "Rita",
            
            "userName": "Rhytah",
            "password": "thisisandela"
        }
        self.user_login_data={
            "userName":"Rhytah",
            "password":"thisisandela"
        }
        self.request_data={
            "requestId":'1',
            "employeeName":"Seth",
            "description":"Mouse failed to work properly",
            "category":"Computer-Peripheral",
            "requestDate":"12/07/2018",
            "title": "Replace Mouse",
        }
     
if __name__ == "__main__":
    unittest.main()