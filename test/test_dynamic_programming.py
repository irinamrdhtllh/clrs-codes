from algorithms.dynamic_programming import memoized_cut_rod, bottom_up_cut_rod


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def test_memoized_cut_rod():
    actual = memoized_cut_rod(p, 4)
    expected = 10
    assert actual == expected


def test_bottom_up_cut_rod():
    actual = bottom_up_cut_rod(p, 4)
    expected = 10
    assert actual == expected
