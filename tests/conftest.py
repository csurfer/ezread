import pytest


@pytest.fixture
def list_of_dicts_json():
    return """[
        {
            "name": "Tom",
            "age": 30,
            "address": {
                "street": ["124 Lincoln St", "West Village"],
                "city": "New York",
                "state": "NYC"
            }
        },
        {
            "name": "Dick",
            "age": 20,
            "address": {
                "street": ["125 Lincoln St", "West Village"],
                "city": "New York",
                "state": "NYC"
            }
        },
        {
            "name": "Harry",
            "age": 40,
            "address": {
                "street": ["50 Vinci Lane", ""],
                "city": "San Fransisco",
                "state": "CA"
            }
        }
    ]"""


@pytest.fixture
def list_of_lists_json():
    return """[
        [1,2,3,4,5,6,7,8,9,10],
        [2,4,6,8,10,12,14,16,18,20],
        [3,6,9,12,15,18,21,24,27,30]
    ]"""
