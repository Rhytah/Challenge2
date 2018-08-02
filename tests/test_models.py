from tests import BaseTestCase
import json 

from tracker.models import User, Request

class Testmodels(BaseTestCase):
    def test_register_user(self):
        """Endpoint to test registering a user using User class"""
        user = User('Rita', 'rita2@hotmail.com','Rhytah','thisisandela',1)