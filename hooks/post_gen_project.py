#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace escaped jinja formatting."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def replace_escaped_formatting(file_path):
    """Replace escaped jinja formatting in the given file."""
    full_path = os.path.join(PROJECT_DIRECTORY, file_path)

    with open(full_path, 'r') as f:
        file_text = f.read()
        file_text = file_text.replace("\{", "{")
        file_text = file_text.replace("\}", "}")
        file_text = file_text.replace("\%", "%")

    with open(full_path, 'w') as f:
        f.write(file_text)


if __name__ == '__main__':
    for path, dirs, files in os.walk("../{{cookiecutter.runtime_prefix}}_-_{{ cookiecutter.project_slug }}/src/app/"):
        for file_ in files:
            if file_.endswith('.html'):
                replace_escaped_formatting(os.path.join(path, file_))
