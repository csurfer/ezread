import pytest
from ezread import EzReader
from json.decoder import JSONDecodeError


@pytest.mark.parametrize(
    "template, expected_rows",
    [
        ("""[0, 1, 2]""", [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
        ("""[0, 9]""", [[1, 10], [2, 20], [3, 30]]),
    ],
)
def test_read(list_of_lists_json, template, expected_rows):
    er = EzReader(template)
    assert expected_rows == er.read(list_of_lists_json)


@pytest.mark.parametrize(
    "template",
    [
        """[0, 1, 20]""",  # 20 being the missing index.
        """[0, 11]""",  # 11 being the missing index.
    ],
)
def test_missingkeys_strict_read(list_of_lists_json, template):
    er = EzReader(template)
    with pytest.raises(IndexError):
        er.read(list_of_lists_json)


@pytest.mark.parametrize(
    "template, expected_rows",
    [
        ("""[0, 1, 20]""", [[1, 2, None], [2, 4, None], [3, 6, None]]),
        ("""[0, 11]""", [[1, None], [2, None], [3, None]]),
    ],
)
def test_missingkeys_nonstrict_read(list_of_lists_json, template, expected_rows):
    er = EzReader(template, strict=False)
    assert expected_rows == er.read(list_of_lists_json)
