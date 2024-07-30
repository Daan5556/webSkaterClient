import argparse

from http_handler import http_client

class URL:
    CACHE_FILE = "cache.json"
    ADDITIONAL_HEADERS = "additional_headers.json"

    def __init__(self, url):
        self.scheme, url = url.split("://", 1)
        assert self.scheme in ["http", "https"]
        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443

        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" + url

        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)

    def request(self):
        if self.scheme == "http" or self.scheme == "https":
            return http_client.GET_request_to_server(
                self.scheme,
                self.host,
                self.port,
                self.path,
                self.ADDITIONAL_HEADERS
            )


def show(body):
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            print(c, end="")
            pass


def load(url):
    body = url.request()
    show(body)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Loads an url")
    parser.add_argument("url", help="The url you want to load", default="http://example.com", nargs="?")
    args = parser.parse_args()

    load(URL(args.url))