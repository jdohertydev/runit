import os

def find_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

# Change 'your_project_directory' to the path of your Django project
project_directory = '.'
py_files = find_py_files(project_directory)

print("List of py files in the project:")
for file in py_files:
    print(file)