from google.genai import types

from config import WORKING_DIR
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file

from dummy_ai import *

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns file content as Text for the specified File path relative to the Working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to retrieve contents from, relative to the working directory",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the specified content to the specified File path relative to the Working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write contents, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the specified file path",
            )
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified File path relative to the Working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to be run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="optional arguments to be passed to the function",
                items=types.Schema(
                    type = types.Type.STRING,
                )
            )
        },
    ),
)


available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
)

func_dict = {
    "get_files_info": get_files_info,
    "write_file": write_file,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file
}

def call_function(function_call,verbose=False):
    function_name = function_call.name or ""
    if not function_name:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call.args) if function_call.args else {}
    args['working_directory']=WORKING_DIR
    if verbose:
        print(f'''args: {function_call.args}
        function: {function_call.name}         
        ''')
    func_call_res = func_dict[function_name](**args)
    if verbose:
        print(f"-> {func_call_res}")
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": func_call_res},
            )
        ],
    )


ai_res_dum = DummyAIResponse(
    text="listing directory",
    function_calls=[
        DummyFunctionCall(
            name="get_file_content",
            args={
                "file_path": "lorum.txt",
                #"args": ["3 + 5"],
                #'content': 'ggggggggg'
            }
        )
    ]
)
