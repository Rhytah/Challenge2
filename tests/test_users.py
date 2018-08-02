from tests import BaseTestCase
import json

class UserTestCase(BaseTestCase):
    def test_register_user(self):
        response = self.test_client.post()