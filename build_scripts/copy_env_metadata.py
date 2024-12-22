import os
import shutil

ENV_FILE_NAME : str = '.env'

# Set the folder path
src_folder_path = "..\\env\\"
dst_folder_path : str = ".\\"

env_files_copy_from : list = []
env_files_copy_to : list = []
# Walk through the folder and its subdirectories
for root, dirs, files in os.walk(src_folder_path):
    
    # Print the paths of all files in the current directory
    for file in files:
        if ".env" in file:
            file_path : str = os.path.join(root, file)
            print(f"  File: {file_path}")
            env_files_copy_from.append(file_path.strip())

#sets the destrnation file paths
for file_path in env_files_copy_from:
    env_files_copy_to.append(file_path.strip().replace('..\\env\\backend',dst_folder_path))


# Copy each file to the destination directory
for i in range(len(env_files_copy_from)):
    try:
        # Check if the source file exists before copying
        if not os.path.exists(env_files_copy_from[i]):
            print(f"Source file does not exist: {env_files_copy_from[i]}")
        else:
            shutil.copy(env_files_copy_from[i], env_files_copy_to[i])
            print(f"Copied: {env_files_copy_from[i]} to {env_files_copy_to[i]}")
    except FileNotFoundError:
        print(f"File not found: {env_files_copy_from[i]}")
    except Exception as e:
        print(f"Error copying {env_files_copy_from[i]}: {e}")