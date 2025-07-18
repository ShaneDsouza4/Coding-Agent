import os
import shutil
import re
    
def read_file(input):
    path = input.get("path") if isinstance(input, dict) else input
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(input):
    path = input["path"]
    content = input["content"]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"File written: {path}"

def append_to_file(input):
    path = input["path"]
    content = input["content"]
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)
    return f"Content appended to: {path}"

def update_file(input):
    path = input["path"]
    pattern = input["pattern"]
    replacement = input["replacement"]
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return f"Updated file: {path}"

def delete_file(input):
    path = input.get("path") if isinstance(input, dict) else input
    if os.path.isfile(path):
        os.remove(path)
        return f"File deleted: {path}"
    return f"File not found: {path}"

def file_exists(input):
    path = input.get("path") if isinstance(input, dict) else input
    return os.path.exists(path)

def create_folder(input):
    path = input.get("path") if isinstance(input, dict) else input
    try:
        os.makedirs(path, exist_ok=True)
        return f"Folder created: {path}"
    except Exception as e:
        return f"Error creating folder '{path}': {e}"

def delete_folder(input):
    path = input.get("path") if isinstance(input, dict) else input
    if os.path.isdir(path):
        shutil.rmtree(path)
        return f"Folder deleted: {path}"
    return f"Folder not found: {path}"

def list_files(input):
    directory = input.get("path") if isinstance(input, dict) else input
    if os.path.isdir(directory):
        return os.listdir(directory)
    return f"Directory not found: {directory}"


def search_in_file(input):
    path = input["path"]
    query = input["query"]

    if not os.path.isfile(path):
        return f"File not found: {path}"

    matches = []
    with open(path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if query in line:
                matches.append({"line": idx, "content": line.strip()})
    
    return matches if matches else "No matches found."
