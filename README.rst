ezread
======

|pypiv| |pyv| |Build| |Coverage| |Licence|

------------------------------------------

ezread provides a ridiculously simple way to fetch items within the JSON list.

Features
--------

* Ridiculously simple interface.
* Known JSON format for indexing helps understand what we are fetching and how.
* Easily procure relevant data from the JSON list for further processing.
* Natively supported nested indexing.

Setup
-----

Using pip
~~~~~~~~~

.. code:: bash

    pip install ezread

Directly from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    git clone https://github.com/csurfer/ezread.git
    python ezread/setup.py install

Documentation
-------------

Modes of operation
~~~~~~~~~~~~~~~~~~

1. **Strict**: In this mode, the reader raises an exception if the "index" or the "key" to be read is not found.

2. **Non-Strict**: In this mode, the reader simply returns None if the "index" or the "key" to be read is not found.

API Usage
~~~~~~~~~

.. code:: python3

    from ezread import EzReader

    # For strict mode
    reader = EzReader(<template with index/key details>)
    reader.read(<json text with list of dicts or lists>)

    # For non strict mode
    reader = EzReader(<template with index/key details>, strict=False)
    reader.read(<json text with list of dicts or lists>)

Template Guide
~~~~~~~~~~~~~~

The template provided to EzReader is very important as it defines what "index" or "key" needs to be read. We expect the template to be in JSON format to provide it some structure. Let's take a few examples and understand how you can specify the items to read from the JSON list that you have.

Let's take the following JSON list of lists.

.. code:: json

    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    ]

**Say you want to fetch 0th index of every list, what would the template look like?**

.. code:: json

    [0]

The rows returned would be

.. code:: text

    [1]
    [2]
    [3]

**Say you want to fetch 0th, 2nd and 4th index of every list, what would the template look like?**

.. code:: json

    [0, 2, 4]

The rows returned would be

.. code:: text

    [1, 3, 5]
    [2, 6, 10]
    [3, 9, 15]

Let's delve a little deeper into index templates with the following JSON list of dicts.

.. code:: json

    [
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
    ]

**Say you want to fetch name from every dict in the list, what would the template look like?**

.. code:: json

    ["name"]

The rows returned would be

.. code:: text

    ["Tom"]
    ["Dick"]
    ["Harry"]

**Say you want to fetch name and age from every dict in the list, what would the template look like?**

.. code:: json

    ["name", "age"]

The rows returned would be

.. code:: text

    ["Tom", 30]
    ["Dick", 20]
    ["Harry", 40]

**Let's say your query is a little bit complicated. You want to fetch name and city a person lives in, what would the template look like?**

You can use lists for nested indexing. Here you want to use "address" and from within it you want to fetch "city". You can achieve it as follows

.. code:: json

    ["name", ["address", "city"]]

The rows returned would be

.. code:: text

    ["Tom", "New York"]
    ["Dick", "New York"]
    ["Harry", "San Fransisco"]

**Does nested indexing always have to be dictionary keys?**

No nested indexing can be dictionary keys or (0-indexed) index within a list. Let's fetch "name" and "first row of address" for each contact.

.. code:: json

    ["name", ["address", "street", 0]]

The rows returned would be

.. code:: text

    ["Tom", "124 Lincoln St"]
    ["Dick", "125 Lincoln St"]
    ["Harry", "50 Vinci Lane"]

Non-Strict mode of query
~~~~~~~~~~~~~~~~~~~~~~~~

**So how does Non-Strict mode of query behave?**

Say we asked for "name" and "hometown" from the previous JSON example. Since "hometown" is not a key in the JSON, it would fail with "KeyError" in strict mode. Similarly if we were accessing a list and tried to access an index which is not present it would end up throwing "IndexOutOfBoundsError" in strict mode.

The same query in non-srict mode would return the correct value for key/indexes it can fetch and None for others.

.. code:: json

    ["name", "hometown"]

The rows returned would be

.. code:: text

    ["Tom", None]
    ["Dick", None]
    ["Harry", None]


Commandline tool
~~~~~~~~~~~~~~~~

Commandline tool provided with this library serves as an easy way to fetch the needed items as CSV file output.

**Usage**

.. code:: bash

    # For help
    ezread --help

    # To use template string directly
    ezread --template_str <index template string> <json file to read>

    # To use template string from a file
    ezread --template_file <file with index template string> <json file to read>

    # By default it uses "," as the separator. If you want a different separator you can use --separator option.
    # We use the strict mode by default. If you want to use non-strict mode use --nonstrict

Contributing
------------

Bug Reports and Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please use `issue tracker`_ for reporting bugs or feature requests.

Development
~~~~~~~~~~~

Pull requests are most welcome.


Buy the developer a cup of coffee!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you found the utility helpful you can buy me a cup of coffee using

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-44px.png
   :target: https://paypal.me/csurfer

.. _issue tracker: https://github.com/csurfer/ezread/issues

.. |Licence| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/csurfer/ezread/master/LICENSE

.. |Build| image:: https://travis-ci.org/csurfer/ezread.svg?branch=master
   :target: https://travis-ci.org/csurfer/ezread

.. |Coverage| image:: https://coveralls.io/repos/github/csurfer/ezread/badge.svg?branch=master
   :target: https://coveralls.io/github/csurfer/ezread?branch=master

.. |pypiv| image:: https://img.shields.io/pypi/v/ezread.svg
   :target: https://pypi.python.org/pypi/ezread

.. |pyv| image:: https://img.shields.io/pypi/pyversions/ezread.svg
   :target: https://pypi.python.org/pypi/ezread
