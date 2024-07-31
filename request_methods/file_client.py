def open_file(file_path: str) -> dict:
    with open(file_path) as file:
        file_ext = file_path.rsplit(".", 1)[-1]
        content_type = format_file_ext_to_content_type(file_ext)

        body = file.read().strip()

    return {
        "body": body, "content-type": content_type}


def format_file_ext_to_content_type(file_ext: str) -> str:
    if file_ext == "html":
        return "text/html"
    if file_ext == "json":
        return "application/json"
    else:
        return "text/plain"
