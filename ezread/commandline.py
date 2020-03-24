import argparse

from .reader import EzReader
from json import dumps


def main():
    # Create command line parser.
    parser = argparse.ArgumentParser()
    # Adding command line arguments.
    parser.add_argument("--template_str", help="Template string", default=None)
    parser.add_argument("--template_file", help="Template file", default=None)
    parser.add_argument(
        "--nonstrict", help="Non strict mode", action="store_true", default=False
    )
    parser.add_argument("--separator", help="CSV separator", default=",")
    parser.add_argument(
        "jsonfile", help="JSON file with lists to be read", default=None
    )
    # Parse command line arguments.
    arguments = parser.parse_args()
    if arguments.jsonfile is not None and (
        arguments.template_str or arguments.template_file
    ):
        # Core functionality.
        rdr, template = None, None
        # Read template string.
        if arguments.template_str:
            template = arguments.template_str
        if arguments.template_file:
            with open(arguments.template_file, "r") as rf:
                template = rf.read()
        # Create EzReader object.
        if arguments.nonstrict:
            rdr = EzReader(template, strict=False)
        else:
            rdr = EzReader(template)
        # Get data rows
        data_rows = None
        with open(arguments.jsonfile, "r") as rf:
            data_rows = rdr.read(rf.read())
        for row in data_rows:
            print(f"{arguments.separator}".join(map(dumps, row)))
    else:
        # Print command help
        parser.print_help()


if __name__ == "__main__":
    main()
