import os


def convert_path(path: str) -> str:
    if path == "index":
        return "/"
    return "/" + path.replace(os.sep, "/").replace("[", "{").replace("]", "}")

def extract_tag(relative_path: str) -> str:
    parts = relative_path.split(os.sep)
    return parts[0] if parts[0] not in (".", "") else "root"
