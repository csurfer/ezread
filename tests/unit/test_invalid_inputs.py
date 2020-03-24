import pytest
from ezread import EzReader
from json.decoder import JSONDecodeError


@pytest.mark.parametrize(
    "template, error",
    [(None, AssertionError), ("", AssertionError), ("abc", JSONDecodeError)],
)
def test_invalid_template(template, error):
    with pytest.raises(error):
        EzReader(template)
