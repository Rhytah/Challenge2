from tracker.mtracker import app
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.user_data = {
            "user_id": 1,
            "name": "Rita",
            "email":"rita2@hotmail.com",
            "userName": "Rhytah",
            "password": "thisisandela"
        }
        self.user_login_data={
            "userName":"Rhytah",
            "password":"thisisandela"
        }
        self.request_data={
            "requestId":1,
            "employeeName":"Seth",
            "description":"finance",
            "category":"Computer-Peripheral",
            "requestDate":"12/07/2018",
            "title": "Replace Mouse",
        }
    def tearDown(self):
        requests = []
        users = []

if __name__ == "__main__":
    unittest.main()