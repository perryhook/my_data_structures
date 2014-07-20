import quick_sort2 as quick_sort
from random import random, randint


def test_empty_list():
    empty = []
    quick_sort.sort(empty)
    assert empty == []


def test_sorted_list():
    sorted_list = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    quick_sort.sort(sorted_list)
    assert sorted_list == [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]


def test_unsorted_list():
    unsorted_list = [6, 2, 8, 4, 5, 3, 3, 4, 88, 2, 99, -43, 0]
    quick_sort.sort(unsorted_list)
    assert unsorted_list == [-43, 0, 2, 2, 3, 3, 4, 4, 5, 6, 8, 88, 99]


def test_large_unsorted_int_list():
    unsorted_list = [randint(-100, 100) for num in xrange(0, 500)]
    sorted_list = sorted(unsorted_list)
    quick_sort.sort(unsorted_list)
    assert unsorted_list == sorted_list


def test_large_unsorted_float_list():
    unsorted_list = [random() * 1000 for num in xrange(0, 500)]
    sorted_list = sorted(unsorted_list)
    quick_sort.sort(unsorted_list)
    assert unsorted_list == sorted_list
