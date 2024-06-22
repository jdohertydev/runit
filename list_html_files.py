import os

def find_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

# Change 'your_project_directory' to the path of your Django project
project_directory = '.'
html_files = find_html_files(project_directory)

print("List of HTML files in the project:")
for file in html_files:
    print(file)