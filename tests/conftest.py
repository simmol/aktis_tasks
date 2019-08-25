import sys


def get_real_path(rel_path):
    import os
    script_dir = os.path.abspath(os.curdir) # <-- absolute dir the script is in
    return os.path.join(script_dir, rel_path)


def assert_files_have_same_content(file_name_one, file_name_two):
    """Simple compare of two files lines to be the same
    filecmp.cmp -> does not work with the captured stdout output on Windows machine( it return False because different
     line end)
    """
    with open(file_name_one, "r") as file_one:
        with open(file_name_two, "r") as file_two:
            file_1_lines = file_one.readlines()
            file_2_lines = file_two.readlines()
            assert file_1_lines == file_2_lines
