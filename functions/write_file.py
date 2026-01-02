import os

def write_file(working_directory, file_path, content):
    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.normpath(os.path.join(working_abs, file_path))

    target_in_work = os.path.commonpath([working_abs,target_abs]) == working_abs

    if not target_in_work:
        return_str = f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    elif os.path.isdir(target_abs):
        return_str = f'Error: Cannot write to "{file_path}" as it is a directory'

    else:
        os.makedirs(working_abs, exist_ok=True)

        with open(target_abs, "w") as f:
            f.write(content)
            return_str = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    return return_str
