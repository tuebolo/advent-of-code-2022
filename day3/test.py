import pytest

from day3.main import open_rucksacks, split_compartments, locate_items, get_priorities, find_badge_priorities

rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                 'PmmdzqPrVvPwwTWBwg',
                 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                 'ttgJtRGJQctTZtZT',
                 'CrZsJsPPZsGzwwsLwLmpwMDw']


def test_open_rucksacks():
    assert open_rucksacks('test.txt') == rucksacks


def test_split_compartments():
    compartments = 'vJrwpWtwJgWrhcsFMMfFFhFp'
    assert split_compartments(compartments) == ('vJrwpWtwJgWr', 'hcsFMMfFFhFp')


def test_locate_items():
    comp_1 = 'vJrwpWtwJgWr'
    comp_2 = 'hcsFMMfFFhFp'
    assert locate_items(comp_1, comp_2) == 'p'


def test_get_priorities():
    assert get_priorities(rucksacks) == [16, 38, 42, 22, 20, 19]


def test_find_badge_priorities():
    assert find_badge_priorities(rucksacks) == [18, 52]
