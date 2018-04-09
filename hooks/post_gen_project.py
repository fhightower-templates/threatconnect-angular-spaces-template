# #!/usr/bin/env python
# import os

# PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


# def rename_dir(old_filepath, new_file_path):
#     os.rename(old_filepath, new_file_path)


# if __name__ == '__main__':
#     # add the prefix to the directory
#     if '{{ cookiecutter.runtime_context }}' == 'Standard':
#         rename_dir('{{ cookiecutter.project_slug }}', '%s_-_{{ cookiecutter.project_slug }}' % 'TCS')
#     elif '{{ cookiecutter.runtime_context }}' == 'Context':
#         rename_dir('{{ cookiecutter.project_slug }}', '%s_-_{{ cookiecutter.project_slug }}' % 'TCX')
#     elif '{{ cookiecutter.runtime_context }}' == 'Menu':
#         rename_dir('{{ cookiecutter.project_slug }}', '%s_-_{{ cookiecutter.project_slug }}' % 'TCM')
#     else:
#         # not sure what to do here... just going to add the standard prefix
#         rename_dir('{{ cookiecutter.project_slug }}', '%s_-_{{ cookiecutter.project_slug }}' % 'TCS')
