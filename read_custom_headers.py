import json


def read_headers_return_formatted(headers: str) -> str:
    if not len(headers) > 0: return "\r\n"
    try:
        headers = json.loads(headers)
    except:
        return "\r\n"
    headers_formatted = ""
    for header in headers:
        value = headers[header]
        formatted_str = f"{header}: {value}\r\n"
        headers_formatted += formatted_str
    print(headers_formatted)
    if headers_formatted: return headers_formatted
    return "\r\n"



