from google.genai import types
import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working = os.path.abspath(working_directory)
    fullpath = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(fullpath)

    if not abs_file_path.startswith(abs_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python3", abs_file_path] + args,
            cwd=abs_working,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = ""
        if result.stdout:
            output += "STDOUT:" + result.stdout
        if result.stderr:
            output += "STDERR:" + result.stderr
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
        if not output:
            return "No output produced."
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"