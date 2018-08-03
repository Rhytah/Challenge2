from tests import BaseTestCase
import json

class RequestTestCase(BaseTestCase):

    def test_create_request(self):
        response = self.test_client.post(
            '/api/v1/users/requests', data=json.dumps(self.request_data),content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn(
            "Hello Seth! Request succesfully created", str(response.data)
        )
    def test_get_all_requests(self):
        response = self.test_client.post(
            '/api/v1/users/requests', data =json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status_code,200)
    
    def test_get_single_request(self):
        response = self.test_client.get(
            '/api/v1/users/requests/1', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code,200)