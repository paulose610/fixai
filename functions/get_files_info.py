import os

def get_files_info(working_directory,directory='.'):
    d_name='current directory' if directory == '.' else directory 
    contents = []
    return_str = ''

    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.normpath(os.path.join(working_abs, directory))
    
    target_in_work = os.path.commonpath([working_abs,target_abs]) == working_abs

    if not target_in_work:
        return_str = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    elif os.path.isfile(target_abs):
        return_str = f'Error: "{directory}" is not a directory'

    else:
        try:
            for cont in os.listdir(target_abs):
                if cont!='__pycache__':
                    cont = target_abs + f'/{cont}'
                    contents.append(f'{cont.split('/')[-1]}: file_size={os.path.getsize(cont)} bytes, is_dir={os.path.isdir(cont)}')
                    return_str = '\n'.join(contents)
        except Exception as e:
            return_str = f'Error: {e}'
            
    return f"Result for {d_name}\n {return_str}"
