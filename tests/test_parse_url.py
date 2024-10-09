import unittest
from misc_services import parse


class TestParseUrl(unittest.TestCase):
    def test_url_should_return_all_values(self):
        parsed_url = parse.url("http://www.example.com")

        self.assertEqual("http", parsed_url["scheme"])
        self.assertEqual("www.example.com", parsed_url["host"])
        self.assertEqual("/", parsed_url["path"])
        self.assertEqual("80", parsed_url["port"])

    def test_missing_keys_should_return_None(self):
        parsed_url = parse.url("file://C:/Users/egdaa/index.html")

        self.assertEqual(None, parsed_url["port"])