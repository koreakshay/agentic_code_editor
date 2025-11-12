import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.function_schemas import schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    sys.exit(1)

# Declare user prompt
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Declare system prompt
system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# Declare available tools
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}


def call_function(function_call_part, verbose=False):
    func_name = function_call_part.name
    args = function_call_part.args or {}
    args["working_directory"] = "./calculator"
    if func_name not in function_map:
        error_msg = f"Function '{func_name}' is not supported."
        return types.Content(role="tool", parts=[types.Part(text=error_msg)])
    func = function_map[func_name]
    function_result = func(**args)
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=func_name,
            response={"result": function_result},
        )
    ],
)

response = None
# create client and generate content with full messages list up to 20 times max
for _ in range(20):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt,
                                               tools=[available_functions]),
        )

        if hasattr(response, 'function_calls') and response.function_calls:
            for function_call_part in response.function_calls:
                print(f" - Calling function: {function_call_part.name}")
                function_call_result = call_function(function_call_part, verbose=True)
                messages.append(types.Content(role="user", parts=function_call_result.parts))
            continue

        if hasattr(response, "text") and response.text:
            print("Final response:")
            print(response.text)
            break        

    except Exception as e:
        print(f"Error during generate_content: {e}")
        break




# if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
#     print(f"User prompt: {user_prompt}")
#     print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
#     print(f'Response tokens: {response.usage_metadata.candidates_token_count}')