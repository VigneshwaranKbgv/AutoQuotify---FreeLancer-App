from django.test import TestCase, Client
from django.urls import reverse
import json

class QuoteAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_quote')

    def test_get_quote_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

    def test_get_quote_post_request(self):
        payload = {
            "service_type": "plumbing",
            "demand_factor": 1.2,
            "urgency": 2.0,
            "location_adjustment": 1.1
        }
        response = self.client.post(
            self.url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('price', response.json())
