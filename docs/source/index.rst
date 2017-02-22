`pyexcel-handsontable` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel-handsontable.git
:Issues: http://github.com/pyexcel/pyexcel-handsontable/issues
:License: New BSD License
:Development: |release|
:Released: |version|
:Generated: |today|

Introduction
--------------------------------------------------------------------------------

**pyexcel-handsontable** renders :class:`pyexcel.Sheet` and :class:`pyexcel.Book` into a `handsontable <https://handsontable.com>`_ in your web page.
As long as you have a browser, you could view the data. However, please note
that this library does not aim to replace any current excel softwares, such
as Micorsoft Office. But it aims to extends the capability of a
Python user/developer in viewing plain data.

Main features:

#. transform your excel sheets into excel alike html file.
#. embed your excel sheets into your web page

Here is one liner to use it with pyexcel:

.. code-block:: python

    import pyexcel as p

    p.save_as(file_name='your.xls', dest_file_name='your.handsontable')


Installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-handsontable


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/pyexcel/pyexcel-handsontable.git
    $ cd pyexcel-handsontable
    $ python setup.py install


Embed Setup
--------------------------------------------------------------------------------


Please copy the hightlighted lines into the head section of each of your web pages:

.. code-block:: html
   :linenos:
   :emphasize-lines: 3-7

    <html><head>
    ...
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.js"></script>
    <style>
    body{font-family:Lato,sans-serif;margin:2 0 0 0}.tab{text-align:center;list-style:none;padding:0 0 0 10px;line-height:24px;height:26px;overflow:hidden;font-size:12px;font-family:verdana;position:relative;margin:0}.tab li{float:left;height:24px;border:1px solid #aaa;background:#d1d1d1;background:linear-gradient(top, #ececec 50%, #d1d1d1);display:inline-block;position:relative;z-index:0;border-top-left-radius:6px;border-top-right-radius:6px;box-shadow:0 3px 3px rgba(0,0,0,0.4),inset 0 1px 0 #fff;text-shadow:0 1px #fff;margin:0 -5px;padding:0 20px}.tab li.active{background:#fff;color:#333;z-index:2}.tab li:before{left:-6px;border-width:0 1px 1px 0;box-shadow:2px 2px 0 #d1d1d1}.tab li:after{right:-6px;border-width:0 0 1px 1px;box-shadow:-2px 2px 0 #d1d1d1}.tab a{color:#555;text-decoration:none}.tab:before{position:absolute;content:" ";width:100%;bottom:0;left:0;border-bottom:1px solid #aaa;z-index:1}.tabcontent{margin-top:-1px}
    </style>
    ...
    <body>
    ...


Then pass on `embed=True` to pyexcel signature functions. It is as simple as that.

.. note::
   For latest handsontable releases, please visit `cdnjs <https://cdnjs.com/libraries/handsontable>`_
