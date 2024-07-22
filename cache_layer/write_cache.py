import io
import json
import time


def check_response_headers_for_max_age(headers: dict) -> str:
    cache_control_header: str = headers.get("cache-control")
    if not cache_control_header: return ""

    try:
        controls = cache_control_header.split(",")
    except ValueError:
        controls = [cache_control_header]

    for control in controls:
        if control.startswith("max-age"):
            _, max_age_value = control.split("=")
            try:
                int(max_age_value)
                return max_age_value
            except ValueError:
                return ""

    return ""


def GenerateCacheDict(cache_data: dict, response_headers: dict, body: bytes) -> dict:
    max_age = check_response_headers_for_max_age(response_headers)
    if not max_age: return

    cache_valid_till = time.time() + int(max_age)

    cache_response = {
        "cache_valid_till": cache_valid_till,
        "body": body.decode("utf8")
    }

    return cache_response



