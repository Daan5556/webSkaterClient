import argparse

from clients import http_client
from clients import file_client

from misc_services import render
from misc_services import parse



class URL:
    ADDITIONAL_HEADERS = "conf/additional_headers.json"

    def __init__(self, url):
        self.parsed_url = parse.url(url)
    def request(self):
        if self.parsed_url["scheme"] == "http" or self.parsed_url["scheme"] == "https":
            return http_client.GET_request_to_server(
                self.parsed_url,
                self.ADDITIONAL_HEADERS
            )
        elif self.parsed_url["scheme"] == "file":
            return file_client.open_file(self.parsed_url["host"] + self.parsed_url["path"])

def load(url):
    response = url.request()
    content_type = response["content-type"]
    body = response["body"]

    if content_type == "text/html":
        render.html_page(body)
    elif content_type == "text/plain":
        print(body)
    else:
        raise Exception("Content not supported for render")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Loads an url")
    parser.add_argument("url", help="The url you want to load", default="file://./templates/index.html", nargs="?")
    args = parser.parse_args()

    load(URL(args.url))
