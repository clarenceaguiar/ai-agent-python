import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_dir.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
    except Exception as e:
        return f'Error: {e}'
    try:
        command = ["python", target_dir]
        if args != None and len(args) != 0:
            command.extend(args)
        comp_process = subprocess.run(command, capture_output=True, timeout=30000, text=True)
        output_string = ''
        if comp_process.returncode != 0:
            output_string = f'Process exited with code {comp_process.returncode}'
        elif comp_process.stdout == '' and comp_process.stderr == '':
            output_string = "No output produced"
        else:
            output_string = f'STDOUT: {comp_process.stdout}\nSTDERR: {comp_process.stderr}'
        return output_string
    except Exception as e:
        return f'Error: executing Python file: {e}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute (run) a python file in a specified directory relative to the working directory, giving its return",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to access content from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of args to execute with the run command of python file"
                }
            },
            "required": ["file_path"],
        },
    },
}
