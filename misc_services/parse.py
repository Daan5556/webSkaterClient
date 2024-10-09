def url(url_input: str) -> dict:
    parsed_url = {}
    scheme, url_input = url_input.split(":", 1)
    if scheme == "http" or scheme == "https":
        _, url_input = url_input.split("//", 1)
        port = 80 if scheme == "http" else 443

        if "/" not in url_input:
            url_input = url_input + "/"
        host, url_input = url_input.split("/", 1)
        path = "/" + url_input

    elif scheme == "file":
        _, url_input = url_input.split("//", 1)
        host, url_input = url_input.split("/", 1)
        path = "/" + url_input
        port = None

    else:
        raise Exception("Scheme '{}' is not supported!".format(scheme))

    return {
        "scheme": scheme,
        "host": host,
        "path": path,
        "port": port
    }
