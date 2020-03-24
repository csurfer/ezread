from json import loads
from typing import List, Dict, Any, Union


class EzReader:
    """Class to enable easy indexing into JSON list."""

    class KeyMapper:
        """Class to map keys to specific items in the dicts/lists."""

        def __init__(self, keys: List[Any], strict: bool) -> None:
            """Constructor.

            :param keys: Keys to fetch in JSON list.
            :param strict: If True fetches items using strict mode.
            """
            self.keys: List[Any] = keys
            self.strict: bool = strict

        def item_mapper(self, item: Union[Dict[str, Any], List[Any]]) -> Any:
            """Method to map keys to values within dictionary/list.

            :param item: Dictionary/List to fetch the value for key from.
            """
            it = item
            for key in self.keys:
                it = it[key]
            return it

        def __call__(self, item: Union[Dict[str, Any], List[Any]]) -> Any:
            try:
                return self.item_mapper(item)
            except Exception as e:
                if self.strict:
                    raise e
                return None

    def __init__(self, template: str, strict: bool = True) -> None:
        """Constructor.

        :param template: JSON string template.
        :param strict: If True fetches items using strict mode.
        """
        assert template, "Template cannot be None or Empty"
        self.mappers: List[EzReader.KeyMapper] = []
        for key in loads(template):
            if type(key) == list:
                self.mappers.append(EzReader.KeyMapper(key, strict))
            else:
                self.mappers.append(EzReader.KeyMapper([key], strict))

    def read_row(self, item: Union[Dict[str, Any], List[Any]]) -> List[Any]:
        """Method to read a single row from item.

        :param item: Dictionary/List to fetch the value for key from.
        """
        return [mapper(item) for mapper in self.mappers]

    def read(self, json_text: str) -> List[List[Any]]:
        """Method to read rows of data from JSON list.

        :param json_text: To fetch data from.
        """
        return [self.read_row(item) for item in loads(json_text)]
