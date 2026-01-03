import os
import subprocess

def run_python_file(working_directory, file_path, args = None):
    return_str = ''
    
    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.normpath(os.path.join(working_abs, file_path))
    
    target_in_work = os.path.commonpath([working_abs,target_abs]) == working_abs

    if not target_in_work:
        return_str = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    elif not os.path.isfile(target_abs):
        return_str = f'Error: "{file_path}" does not exist or is not a regular file'
    
    elif file_path.split('.')[-1]!='py':
        return_str = f'Error: "{file_path}" is not a Python file'

    else:
        try:
            command = ["python",target_abs]
            if args:
                command.extend(args)
            res = subprocess.run(args=command, capture_output=True, text=True, check=True, timeout=30, cwd=working_abs)
        
            if res.returncode>0:
                return_str = f'Process exited with code {res.returncode}'
            elif res.stderr:
                return_str+=f'STDERR: {res.stderr}'
            elif res.stdout:
                return_str+=f'STDOUT: {res.stdout}'    
            else:    
                return_str='No output produced'

        except subprocess.CalledProcessError as e:
            return_str = f"Error: executing Python file: {e}"


    return return_str



        
    
