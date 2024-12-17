from algorithms.sorting.insertion_sort import insertion_sort


def test_general_list():
    actual = [5, 2, 4, 6, 1, 3]
    insertion_sort(actual)
    expected = [1, 2, 3, 4, 5, 6]
    assert actual == expected


def test_empty_list():
    actual = []
    insertion_sort(actual)
    expected = []
    assert actual == expected


def test_single_element_list():
    actual = [1]
    insertion_sort(actual)
    expected = [1]
    assert actual == expected
