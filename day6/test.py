import pytest

from day6.main import get_marker

packet = 4
message = 14

test1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test3 = 'nppdvjthqldpwncqszvftbrmjlhg'
test4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


def test_get_marker_1():
    assert get_marker(test1, packet) == 7


def test_get_marker_2():
    assert get_marker(test2, packet) == 5


def test_get_marker_3():
    assert get_marker(test3, packet) == 6


def test_get_marker_4():
    assert get_marker(test4, packet) == 10


def test_get_marker_5():
    assert get_marker(test5, packet) == 11

def test_get_message_1():
    assert get_marker(test1, message) == 19


def test_get_message_2():
    assert get_marker(test2, message) == 23


def test_get_message_3():
    assert get_marker(test3, message) == 23


def test_get_message_4():
    assert get_marker(test4, message) == 29


def test_get_message_5():
    assert get_marker(test5, message) == 26

