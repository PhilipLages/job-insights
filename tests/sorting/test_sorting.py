from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Web developer",
            "min_salary": "invalid",
            "max_salary": "invalid",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "",
        },
        {
            "title": "Back end developer",
            "min_salary": "",
            "max_salary": "3000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
    ]

    expected = [
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "",
        },
        {
            "title": "Back end developer",
            "min_salary": "",
            "max_salary": "3000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Web developer",
            "min_salary": "invalid",
            "max_salary": "invalid",
        },
    ]

    sort_by(jobs, "min_salary")
    assert jobs == expected

    expected = [
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Back end developer",
            "min_salary": "",
            "max_salary": "3000",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "",
        },
        {
            "title": "Web developer",
            "min_salary": "invalid",
            "max_salary": "invalid",
        },
    ]

    sort_by(jobs, "max_salary")
    assert jobs == expected

    expected = [
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Back end developer",
            "min_salary": "",
            "max_salary": "3000",
        },
        {
            "title": "Web developer",
            "min_salary": "invalid",
            "max_salary": "invalid",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "",
        },
    ]

    sort_by(jobs, "date_posted")
    assert jobs == expected
