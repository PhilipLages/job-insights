import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "title": "Web developer",
            "min_salary": 600,
            "max_salary": 2900,
            "date_posted": "2023-02-22",
        },
        {
            "title": "Front end developer",
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2023-03-01",
        },
        {
            "title": "Back end developer",
            "min_salary": 1500,
            "max_salary": 3000,
            "date_posted": "2023-02-15",
        },
        {
            "title": "Full stack end developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2023-03-10",
        },
    ]


def jobs_max_salary():
    return [
        {
            "title": "Full stack end developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2023-03-10",
        },
        {
            "title": "Back end developer",
            "min_salary": 1500,
            "max_salary": 3000,
            "date_posted": "2023-02-15",
        },
        {
            "title": "Web developer",
            "min_salary": 600,
            "max_salary": 2900,
            "date_posted": "2023-02-22",
        },
        {
            "title": "Front end developer",
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2023-03-01",
        },
    ]


def jobs_date_posted():
    return [
        {
            "title": "Full stack end developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2023-03-10",
        },
        {
            "title": "Front end developer",
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2023-03-01",
        },
        {
            "title": "Web developer",
            "min_salary": 600,
            "max_salary": 2900,
            "date_posted": "2023-02-22",
        },
        {
            "title": "Back end developer",
            "min_salary": 1500,
            "max_salary": 3000,
            "date_posted": "2023-02-15",
        },
    ]


def jobs_min_salary():
    return [
        {
            "title": "Web developer",
            "min_salary": 600,
            "max_salary": 2900,
            "date_posted": "2023-02-22",
        },
        {
            "title": "Front end developer",
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2023-03-01",
        },
        {
            "title": "Back end developer",
            "min_salary": 1500,
            "max_salary": 3000,
            "date_posted": "2023-02-15",
        },
        {
            "title": "Full stack end developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2023-03-10",
        },
    ]


def test_sort_by_criteria(jobs):

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary()

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_posted()

    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary()
