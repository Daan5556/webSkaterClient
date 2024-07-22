import io
import unittest
from Tests.cache_layer.mock_data import cache_layer_mock_data

from cache_layer import write_cache

class WriteCache(unittest.TestCase):
    # check_response_headers_for_max_age()
    def test_should_return_max_age(self):
        mock_response_headers = cache_layer_mock_data.mock_max_age

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual("604800", max_age)
    def test_no_max_age_should_return_empty(self):
        mock_response_headers = cache_layer_mock_data.mock_max_age_empty

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual("", max_age)
    def test_no_control_should_return_empty(self):
        mock_response_headers = cache_layer_mock_data.mock_no_control

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual("", max_age)

    def test_max_age_not_int_should_return_empty(self):
        mock_response_headers = cache_layer_mock_data.mock_max_age_not_int

        max_age = write_cache.check_response_headers_for_max_age(mock_response_headers)

        self.assertEqual("", max_age)

    #write_body_in_cache
    def test_valid_cache_should_write(self):
        cache_data = {}
        response_headers = cache_layer_mock_data.cache_item.get("response_headers")
        body = cache_layer_mock_data.cache_item.get("body")

        result = write_cache.GenerateCacheDict(cache_data, response_headers, body)

        self.assertTrue(result["cache_valid_till"], "1722259047.3748975")
        self.assertTrue(result.get("body"))
