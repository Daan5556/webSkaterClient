import unittest
from clients import file_client


class TestFileClient(unittest.TestCase):
    def test_path_returns_file_ext(self):
        val = file_client.open_file("C:/Users/egdaa/index.html")
        result = val["content-type"]

        self.assertEqual("text/html", result)

    def test_json_should_return_file_ext(self):
        val = file_client.open_file("C:/Users/egdaa/data.json")
        result = val["content-type"]

        self.assertEqual("application/json", result)

    def test_path_should_return_content(self):
        val = file_client.open_file("C:/Users/egdaa/index.html")
        result = val["body"]

        self.assertEqual("<h1>Hello World</h1>", result)

    def test_path_should_return_content_text_file(self):
        val = file_client.open_file("C:/Users/egdaa/text.txt")
        result = val["body"]

        self.assertEqual("<h1>Hello World</h1>", result)

    def test_relative_path_should_return_data(self):
        val = file_client.open_file("./mock/index.html")
        content_type = val["content-type"]
        body = val["body"]

        self.assertEqual("text/html", content_type)
        self.assertEqual("<h1>Hello World</h1>", body)


