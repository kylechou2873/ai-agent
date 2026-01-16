import os
def get_files_info(working_directory, directory = '.'):
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not valid_target_dir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            return (f'Error: "{directory}" is not a directory')
        dir_cont = os.listdir(target_dir)
        dir_string = []
        for d in dir_cont:
            full_path = os.path.join(target_dir, d)
            dir_string.append(f'- {d}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}')
        return("\n".join(dir_string))
    except Exception as e:
        return f"Error: {e}"
    
