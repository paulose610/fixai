import os
from config import MAX_CHARS

def get_file_content(working_directory,file_path):
    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.normpath(os.path.join(working_abs, file_path))

    target_in_work = os.path.commonpath([working_abs,target_abs]) == working_abs 

    if not target_in_work:
        return_str = f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    elif not os.path.isfile(target_abs):
        return_str = f'Error: File not found or is not a regular file: "{file_path}"'

    else:
        with open(target_abs, "r") as f:
            return_str = f.read(MAX_CHARS)
            if f.read(1):
                return_str += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return return_str

            