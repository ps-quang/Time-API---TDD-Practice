# time_api/tests.py
from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from unittest.mock import patch

class TimeApiTestCase(TestCase):

    def test_time_url_is_status_okay(self):
        response = self.client.get('/api/time/')
        self.assertEqual(200, response.status_code)

    def test_time_api_should_return_json(self):
        response = self.client.get('/api/time/')
        self.assertEqual('application/json', response['Content-Type'])

    def test_time_api_should_include_current_time_key(self):
        response = self.client.get('/api/time/')
        self.assertTrue('current_time' in response.json())

    def test_time_api_should_return_valid_iso8601_format(self):
        response = self.client.get('/api/time/')
        current_time = response.json()['current_time']
        dt = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%SZ')
        self.assertTrue(isinstance(dt, datetime))

    def test_time_api_should_return_current_utc_time(self):
        with patch('django.utils.timezone.now') as mock_tz_now:
            expected_datetime = datetime(2018, 1, 1, 10, 10, tzinfo=timezone.utc)
            mock_tz_now.return_value = expected_datetime

            response = self.client.get('/api/time/')
            current_time = response.json()['current_time']
            parsed_time = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%S%z')

            self.assertEqual(parsed_time, expected_datetime)