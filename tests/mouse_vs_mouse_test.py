from contextlib import redirect_stdout
from os import makedirs

import pytest

from mouse_vs_mouse import mouse_vs_mouse_from_file
from tests.conftest import get_real_path, assert_files_have_same_content


@pytest.mark.parametrize('test_index', ['00', '01'])
def test_calculate_running_median_from_file(test_index):
    makedirs(get_real_path('tests/test_files/output/mouse-vs-mouse'), exist_ok=True)
    with open(get_real_path(f'tests/test_files/output/mouse-vs-mouse/output{test_index}.txt'), 'w') as out:
        with redirect_stdout(out):
            mouse_vs_mouse_from_file(get_real_path(f'tests/test_files/mouse-vs-mouse/input{test_index}.txt'))

    assert_files_have_same_content(f'tests/test_files/output/mouse-vs-mouse/output{test_index}.txt',
                                   f'tests/test_files/mouse-vs-mouse/output{test_index}.txt')