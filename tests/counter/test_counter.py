from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "Python"
    count = count_ocurrences(path, word)
    assert count == 1639

    word = "Javascript"
    count = count_ocurrences(path, word)
    assert count == 122
