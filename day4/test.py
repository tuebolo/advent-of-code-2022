import pytest

from day4.main import open_assignments, convert_to_range, check_fully_overlap, check_overlap

assignments = [{2, 3, 4},
               {8, 6, 7},
               {2, 3},
               {4, 5},
               {5, 6, 7},
               {8, 9, 7},
               {2, 3, 4, 5, 6, 7, 8},
               {3, 4, 5, 6, 7},
               {6},
               {4, 5, 6},
               {2, 3, 4, 5, 6},
               {4, 5, 6, 7, 8}]

def test_open_assignments():
    assert open_assignments('test.txt') == assignments


def test_convert_to_range():
    section = '2-4'
    assert convert_to_range(section) == {2, 3, 4}


def test_check_fully_overlap():
    assert check_fully_overlap(assignments) == 2


def test_check_overlap():
    assert check_overlap(assignments) == 4