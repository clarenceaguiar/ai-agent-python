import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f'Error: {e}'
    try:
        list_dir: list[str] = os.listdir(target_dir)
        result: list[str] = []
        for item in list_dir:
            item_path: str = os.path.join(target_dir, item)
            result.append(f"  - {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}")
        return "\n".join(result)
    except Exception as e:
        return f'Error: {e}'
