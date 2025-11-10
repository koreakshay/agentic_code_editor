import os

def get_files_info(working_directory, directory="."):
    fullpath = os.path.join(working_directory, directory)

    abs_working = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(fullpath)

    if not abs_directory.startswith(abs_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    try:
        entries = os.listdir(abs_directory)
    except FileNotFoundError:
        return f'Error: "{directory}" is not a directory'
    
    descriptions = []
    for entry in entries:
        filepath = os.path.join(abs_directory, entry)
        is_dir = os.path.isdir(filepath)
        file_size = os.path.getsize(filepath)
        descriptions.append(f"- {entry}: file_size={file_size}, is_dir={is_dir}")
    
    return "\n".join(descriptions)