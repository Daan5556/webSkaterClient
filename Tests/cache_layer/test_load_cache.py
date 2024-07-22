import unittest

from cache_layer import load_cache
from mock_data import load_cache_mock_data


class TestLoadCache(unittest.TestCase):

    def test_path_should_return_body(self):
        cache_file = load_cache_mock_data.cache
        host = "www.example.com"
        path = "/"

        result = load_cache.find_cache_file_return_body(cache_file, host, path)
        self.assertTrue(result)
    def test_not_cached_should_return_false(self):
        cache_file = load_cache_mock_data.cache
        host = "www.google.com"
        path = "/"

        result = load_cache.find_cache_file_return_body(cache_file, host, path)
        self.assertFalse(result)

    def test_host_found_not_path_should_return_false(self):
        cache_file = load_cache_mock_data.cache
        host = "www.example.com"
        path = "green"

        result = load_cache.find_cache_file_return_body(cache_file, host, path)
        self.assertFalse(result)
