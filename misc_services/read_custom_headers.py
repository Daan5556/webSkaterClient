import json


def read_headers_return_formatted(headers: str) -> str:
    if not len(headers) > 0: return ""
    try:
        headers = json.loads(headers)
    except:
        return ""
    headers_formatted = ""
    for header in headers:
        value = headers[header]
        formatted_str = f"{header}: {value}\r\n"
        headers_formatted += formatted_str
    if headers_formatted: return headers_formatted
    return ""



