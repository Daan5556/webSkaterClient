import unittest
import cache_layer_mock_data

from cache_layer import write_cache

class WriteCache(unittest.TestCase):
    def test_should_return_max_age(self):
        mock_response_headers = cache_layer_mock_data.mock_max_age

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual(max_age, "604800")
    def test_no_max_age_should_return_empty(self):
        mock_response_headers = cache_layer_mock_data.mock_max_age_empty

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual(max_age, "")
    def test_no_control_should_return_empty(self):
        mock_response_headers = cache_layer_mock_data.mock_no_control

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual(max_age, "")

    def test_max_age_not_int_should_return_empty(self):
        mock_response_headers = cache_layer_mock_data.mock_max_age_not_int

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual(max_age, "")
