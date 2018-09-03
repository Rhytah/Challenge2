from tests import BaseTestCase

import json 

from tracker.models import User, Request,users,requests

class Testmodels(BaseTestCase):
    def test_register_user(self):
        """Endpoint to test registering a user using User class"""
        user = User('Rita','Rhytah','thisisandela',1)