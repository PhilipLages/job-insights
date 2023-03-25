from src.pre_built.brazilian_jobs import read_brazilian_file
from tests.mocks.formated_brazilians_jobs import formated_brazilians_jobs


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    actual_data = read_brazilian_file(path)

    assert actual_data == formated_brazilians_jobs
