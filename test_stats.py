from stats import average, median


def test_average():
    assert average([2, 4, 6]) == 4


def test_median_odd():
    assert median([3, 1, 2]) == 2
