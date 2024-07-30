import unittest

from Tests.cache_layer.mock_data import read_header_mockdata
import read_custom_headers


class TestReadHeaders(unittest.TestCase):
    def test_headers_string_should_be_formatted(self):
        headers = read_header_mockdata.headers

        result = read_custom_headers.read_headers_return_formatted(headers)
        print(result)

        self.assertTrue(result)

    def test_no_headers_should_return_new_line(self):
        headers = ""

        result = read_custom_headers.read_headers_return_formatted(headers)

        self.assertEqual("\r\n", result)
