import gzip
import json
import socket
import ssl

import cache_layer.write_cache
import cache_layer.load_cache


class URL:
    CACHE_FILE = "cache.json"

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

    def request(self, user_agent=None, encoded_response=True):
        cache_data: dict = cache_layer.load_cache.load_cache_file(self.CACHE_FILE)

        cached_response = cache_layer.load_cache.find_cache_file_return_body(
            cache_data, self.host, self.path
        )
        if cached_response:
            return cached_response

        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )

        s.connect((self.host, self.port))
        if self.scheme == "https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=self.host)

        # HEADERS
        request = "GET {} HTTP/1.0\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
        if user_agent:
            request += "User-Agent: {}\r\n".format(user_agent)
        if encoded_response:
            request += "Accept-Encoding: gzip\r\n"
        request += "\r\n"

        s.send(request.encode("utf8"))

        response = s.makefile("rb").read()
        header_data, _, body = response.partition(b"\r\n\r\n")

        headers = header_data.decode().split("\r\n")
        status_line = headers[0]
        response_headers = {}
        for header in headers[1:]:
            key, value = header.split(":", 1)
            response_headers[key.casefold()] = value.strip()
        if "content-encoding" in response_headers and response_headers["content-encoding"] == "gzip":
            body = gzip.decompress(body)

        if "200 OK" in status_line:
            cached_response = cache_layer.write_cache.GenerateCacheDict(
                cache_data,
                response_headers,
                body
            )
            if self.host not in cache_data: cache_data[self.host] = {}
            if self.path not in cache_data[self.host]: cache_data[self.host][self.path] = {}

            if cached_response:
                cache_data[self.host][self.path] = cached_response

                with open(self.CACHE_FILE, "w") as file:
                    file.write(json.dumps(cache_data))

        return body.decode("utf8")


def show(body):
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            print(c, end="")


def load(url, user_agent=None):
    body = url.request(user_agent)
    show(body)


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"

if __name__ == "__main__":
    import sys

    load(URL(sys.argv[1]), user_agent)
