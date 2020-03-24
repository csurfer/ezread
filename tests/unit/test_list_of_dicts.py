import pytest
from ezread import EzReader


@pytest.mark.parametrize(
    "template, expected_rows",
    [
        ("""["name"]""", [["Tom"], ["Dick"], ["Harry"]]),
        ("""["name", "age"]""", [["Tom", 30], ["Dick", 20], ["Harry", 40]]),
        (
            """["name", "age", ["address", "street", 0]]""",
            [
                ["Tom", 30, "124 Lincoln St"],
                ["Dick", 20, "125 Lincoln St"],
                ["Harry", 40, "50 Vinci Lane"],
            ],
        ),
    ],
)
def test_read(list_of_dicts_json, template, expected_rows):
    er = EzReader(template)
    assert expected_rows == er.read(list_of_dicts_json)


@pytest.mark.parametrize(
    "template",
    [
        """["name", "age", ["address", "zip"]]""",  # zip being the missing key.
        """["name", "profession"]""",  # profession being the missing key.
    ],
)
def test_missingkeys_strict_read(list_of_dicts_json, template):
    er = EzReader(template)
    with pytest.raises(KeyError):
        er.read(list_of_dicts_json)


@pytest.mark.parametrize(
    "template, expected_rows",
    [
        (
            """["name", "age", ["address", "zip"]]""",  # zip being the missing key.
            [["Tom", 30, None], ["Dick", 20, None], ["Harry", 40, None]],
        ),
        (
            """["name", "profession"]""",  # profession being the missing key.
            [["Tom", None], ["Dick", None], ["Harry", None]],
        ),
    ],
)
def test_missingkeys_nonstrict_read(list_of_dicts_json, template, expected_rows):
    er = EzReader(template, strict=False)
    assert expected_rows == er.read(list_of_dicts_json)
