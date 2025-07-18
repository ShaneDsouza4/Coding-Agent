import os
from pathlib import Path

def get_current_directory(_input=None):
    return os.getcwd()

def change_directory(input):
    path = input.get("path") if isinstance(input, dict) else input
    os.chdir(path)
    return f"Changed directory to {path}"

def list_files_recursive(input):
    directory = input.get("path") if isinstance(input, dict) else input
    return [str(p) for p in Path(directory).rglob('*') if p.is_file()]

def find_files_by_name(input):
    name = input["name"]
    root = input.get("root", ".")
    return [str(p) for p in Path(root).rglob(name)]

def find_files_by_extension(input):
    extension = input["extension"]
    root = input.get("root", ".")
    return [str(p) for p in Path(root).rglob(f'*{extension}')]

def search_in_files(input):
    keyword = input["keyword"]
    root = input.get("root", ".")
    matches = []
    for path in Path(root).rglob('*.*'):
        if not path.is_file():
            continue
        try:
            with path.open(encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if keyword in line:
                        matches.append((str(path), i, line.strip()))
        except Exception:
            continue
    return matches