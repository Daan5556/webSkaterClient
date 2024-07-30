import socket
import gzip
import json
import ssl

import read_custom_headers

def GET_request_to_server(scheme, host, port, path, ADDITIONAL_HEADERS):
    s = socket.socket(
                family=socket.AF_INET,
                type=socket.SOCK_STREAM,
                proto=socket.IPPROTO_TCP
            )

    s.connect((host, port))
    if scheme == "https":
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(s, server_hostname=host)

    # HEADERS
    request = "GET {} HTTP/1.0\r\n".format(path)
    request += "Host: {}\r\n".format(host)
    try:
        with open(ADDITIONAL_HEADERS, "r") as file:
            custom_headers = file.read()
            formatted_headers = read_custom_headers.read_headers_return_formatted(custom_headers)
    except FileNotFoundError:
        pass

    request += formatted_headers
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

    return body.decode("utf8")