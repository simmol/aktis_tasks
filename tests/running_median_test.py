from contextlib import redirect_stdout
from os import makedirs

import pytest

from running_median import calculate_median, calculate_median_from_file
from tests.conftest import get_real_path, assert_files_have_same_content


def test_calculate_median_of_sorted_list():
    assert 1 == calculate_median([1])

    assert 1.5 == calculate_median([1, 2])

    assert 2 == calculate_median([1, 2, 3])

    assert 5.5 == calculate_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@pytest.mark.parametrize('test_index', ['00', '01', '02', '03', '04'])
def test_calculate_running_median_from_file(test_index):
    makedirs(get_real_path('tests/test_files/output/running-median'), exist_ok=True)
    with open(get_real_path(f'tests/test_files/output/running-median/output{test_index}.txt'), 'w') as out:
        with redirect_stdout(out):
            calculate_median_from_file(get_real_path(f'tests/test_files/running-median/input{test_index}.txt'))

    assert_files_have_same_content(f'tests/test_files/output/running-median/output{test_index}.txt',
                                   f'tests/test_files/running-median/output{test_index}.txt')
