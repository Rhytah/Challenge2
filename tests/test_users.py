from tests import BaseTestCase
import json

class UserTestCase(BaseTestCase):
    def test_register_user(self):
        response = self.test_client.post(
            '/auth/register', data=json.dumps(self.user_data), content_type= 'application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn("User Rhytah has successfully been created", str(response.data))
