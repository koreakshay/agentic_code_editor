import os

def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    fullpath = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(fullpath)

    if not abs_file_path.startswith(abs_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'