import argparse

from request_methods import http_client
from request_methods import file_client

from misc_services import render


class URL:
    ADDITIONAL_HEADERS = "conf/additional_headers.json"

    def __init__(self, url):
        self.scheme, url = url.split("://", 1)
        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443

        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" + url

        if ":" in self.host and self.scheme == "http" or self.scheme == "https":
            self.host, self.port = self.host.split(":", 1)

    def request(self):
        if self.scheme == "http" or self.scheme == "https":
            return http_client.GET_request_to_server(
                self.scheme,
                self.host,
                self.port,
                self.path,
                self.ADDITIONAL_HEADERS
            )
        if self.scheme == "file":
            return file_client.open_file(self.host + self.path)

        else:
            raise Exception("Scheme {} is not supported".format(self.scheme))

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
