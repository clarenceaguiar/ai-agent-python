import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f'Error: {e}'
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(MAX_CHARS + 1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Shows file content in a specified directory relative to the working directory, limited a maximum number of characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to access content from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
