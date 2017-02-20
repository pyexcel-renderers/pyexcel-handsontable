================================================================================
pyexcel-handsontable - Let you focus on data, instead of file formats
================================================================================

.. image:: https://api.travis-ci.org/pyexcel/pyexcel-handsontable.svg?branch=master
   :target: http://travis-ci.org/pyexcel/pyexcel-handsontable

.. image:: https://codecov.io/github/pyexcel/pyexcel-handsontable/coverage.png
    :target: https://codecov.io/github/pyexcel/pyexcel-handsontable

.. image:: https://readthedocs.org/projects/pyexcel-handsontable/badge/?version=latest
   :target: http://pyexcel-handsontable.readthedocs.org/en/latest/


The sphinx library uses pyexcel to read an excel files and renders into an excel-alike sheet in your sphinx documentation. The excel file formats are:

   #. csv, tsv, csvz, tsvz
   #. xls, xlsx, xlsm
   #. ods




Installation
================================================================================
You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-handsontable


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/pyexcel/pyexcel-handsontable.git
    $ cd pyexcel-handsontable
    $ python setup.py install



Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/pyexcel-handsontable.git
#. cd pyexcel-handsontable

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools "pip==7.1"

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt


In order to update test environment, and documentation, additional setps are
required:

#. pip install moban
#. git clone https://github.com/pyexcel/pyexcel-commons.git commons
#. make your changes in `.moban.d` directory, then issue command `moban`

What is rnd_requirements.txt
-------------------------------

Usually, it is created when a dependent library is not released. Once the dependecy is installed(will be released), the future version of the dependency in the requirements.txt will be valid.

What is pyexcel-commons
---------------------------------

Many information that are shared across pyexcel projects, such as: this developer guide, license info, etc. are stored in `pyexcel-commons` project.

What is .moban.d
---------------------------------

`.moban.d` stores the specific meta data for the library.

How to test your contribution
------------------------------

Although `nose` and `doctest` are both used in code testing, it is adviable that unit tests are put in tests. `doctest` is incorporated only to make sure the code examples in documentation remain valid across different development releases.

On Linux/Unix systems, please launch your tests like this::

    $ make test

On Windows systems, please issue this command::

    > test.bat

License
================================================================================

New BSD License
