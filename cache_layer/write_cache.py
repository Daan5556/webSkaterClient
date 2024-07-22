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
