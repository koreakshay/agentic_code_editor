from config import CHARACTER_LIMIT
import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    fullpath = os.path.join(working_directory, file_path)
    abs_filepath = os.path.abspath(fullpath)

    if not abs_filepath.startswith(abs_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        return f'Error: Cannot read file "{file_path}": {e}'

    if len(content) > CHARACTER_LIMIT:
        truncated = content[:CHARACTER_LIMIT]
        notice = f'\n[...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]\n'
        return truncated + notice

    return content