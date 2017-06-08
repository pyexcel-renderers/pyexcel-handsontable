================================================================================
pyexcel-handsontable - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.travis-ci.org/pyexcel/pyexcel-handsontable.svg?branch=master
   :target: http://travis-ci.org/pyexcel/pyexcel-handsontable

.. image:: https://codecov.io/github/pyexcel/pyexcel-handsontable/coverage.png
   :target: https://codecov.io/github/pyexcel/pyexcel-handsontable

.. image:: https://readthedocs.org/projects/pyexcel-handsontable/badge/?version=latest
   :target: http://pyexcel-handsontable.readthedocs.org/en/latest/

Known constraints
==================

Fonts, colors and charts are not supported.

**pyexcel-handsontable** is a rendering plugin to
`pyexcel <http://pyexcel.readthedocs.org/en/latest>`_  and renders
:class:`pyexcel.Sheet` and :class:`pyexcel.Book` into a
`handsontable <https://handsontable.com>`_ in your web page. As long as you
have a browser, you could view the data. However, please note
that this library does not aim to replace any current excel softwares, such
as Micorsoft Office. But it aims to extends the capability of a
Python user/developer in viewing plain data.


Main features:

#. transform your excel sheets into excel alike html file.
#. embed your excel sheets into your web page

.. image:: https://github.com/pyexcel/pyexcel-handsontable/blob/master/demo/screenshot.png

Here is one liner to use it with pyexcel:

.. code-block:: python

    import pyexcel as p

    p.save_as(file_name='your.xls', dest_file_name='your.handsontable.html')


Please remember to give this file suffix always: **handsontable.html**. It is because `handsontable.html` triggers this plugin in pyexcel.



Installation
================================================================================
You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-handsontable


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-handsontable.git
    $ cd pyexcel-handsontable
    $ python setup.py install



Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please `support me on patreon <https://www.patreon.com/bePatron?u=5537627>`_ to
maintain the project and develop it further.

If you are an individual, you are welcome to support me too on patreon and for however long
you feel like to. As a patreon, you will receive
`early access to pyexcel related contents <https://www.patreon.com/pyexcel/posts>`_.

With your financial support, I will be able to invest
a little bit more time in coding, documentation and writing interesting posts.


Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/pyexcel-handsontable.git
#. cd pyexcel-handsontable

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools pip

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt


In order to update test environment, and documentation, additional steps are
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

    $ make

On Windows systems, please issue this command::

    > test.bat


Update styles
--------------------

`styles/style.scss` control the look and feel of the frame. In order to view the changes
in that file, you will need to compile, moban and install it. Here is the sequence
of commands::

    $ make css
    $ moban
    $ python setup.py install
    $ make -C demo

Then please open handsontable.html from demo directory.


License
================================================================================

New BSD License
