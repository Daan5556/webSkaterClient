import io
import json
import time


def load_cache_file(file: str) -> dict:
    try:
        with open(file) as file:
            try:
                return json.loads(file.read())
            except json.decoder.JSONDecodeError:
                return {}
    except FileNotFoundError:
        with open(file, "w"):
            return {}


def find_cache_file_return_body(cache_file, host, path) -> str:
    if host not in cache_file:
        return ""
    if path not in cache_file[host]:
        return ""

    if time.time() > cache_file[host][path]["cache_valid_till"]:
        return ""

    return cache_file[host][path]["body"]
