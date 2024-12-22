set deps_file_folder_path="metadata"
set deps_file_name="deps.txt"

set deps_file_path="%deps_file_folder_path%/%deps_file_name%"

pip install -r %deps_file_path%


::  pip freeze > {deps.txt}      exports all dependencies to dpes.txt file
::  pip install -r {deps.txt}    installs all dependecnies from deps.txt file