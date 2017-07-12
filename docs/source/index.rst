`pyexcel-handsontable` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel-handsontable.git
:Issues: http://github.com/pyexcel/pyexcel-handsontable/issues
:License: New BSD License
:Released: |version|
:Generated: |today|

Introduction
--------------------------------------------------------------------------------

**pyexcel-handsontable** is a rendering plugin to
`pyexcel <http://pyexcel.readthedocs.org/en/latest>`_  and renders
`pyexcel.Sheet` and `pyexcel.Book` into a
`handsontable <https://handsontable.com>`_ in your web page. As long as you
have a browser, you could view the data. However, please note
that this library does not aim to replace any current excel softwares, such
as Micorsoft Office. But it aims to extends the capability of a
Python user/developer in viewing plain data.


Main features:

#. transform your excel sheets into excel alike html file.
#. embed your excel sheets into your web page

.. image:: https://github.com/pyexcel/pyexcel-handsontable/raw/master/demo/screenshot.png

Here is one liner to use it with pyexcel:

.. code-block:: python

    import pyexcel as p

    p.save_as(file_name='your.xls', dest_file_name='your.handsontable.html')

Alternatively, you can use this library with pyexcel cli module::


    $ pip install pyexcel-cli
	$ pyexcel transcode your.xls your.handsontable.html


Please remember to give this file suffix always: **handsontable.html**. It is because `handsontable.html` triggers this plugin in pyexcel.

Known constraints
==================

Fonts, colors and charts are not supported.

Installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-handsontable


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-handsontable.git
    $ cd pyexcel-handsontable
    $ python setup.py install


Rendering Options
--------------------------------------------------------------------------------

You can pass the following options to :meth:`pyexcel.Sheet.save_as` and
:meth:`pyexcel.Book.save_as`. The same options are applicable to
pyexcel's signature functions, but please remember to add 'dest_' prefix. 

**js_url** The default url for handsontable javascript file points to cdnjs
version 0.31.0. You can replace it with your custom url

**css_url** The default url for handsontable style sheet points to cdnjs
version 0.31.0. You can replace it with your custom url

**embed** If it is set true, the resulting html will only contain a portion
of HTML without the HTML header. And it is expected that you, as the
developer to provide the necessary HTML header in your web page.

What's more, you could apply
`all handsontable's options <https://docs.handsontable.com/pro/1.10.0/Options.html>`_
to the rendering too. for example, 'readOnly'
was set to `True` as default in this library. In the demo, 'readOnly' was
overridden as `False`.


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
    body{font-family:Helvetica,sans-serif;margin:2 0 0 0}.tab{margin-bottom:0 !important;text-align:center;list-style:none;padding:0 0 0 10px;line-height:24px;height:26px;overflow:hidden;font-size:12px;font-family:verdana;position:relative;margin:0}.tab li{margin-left:0 !important;float:left;height:24px;border:1px solid #aaa;background:#d1d1d1;background:linear-gradient(top, #ececec 50%, #d1d1d1);display:inline-block;position:relative;z-index:0;border-top-left-radius:6px;border-top-right-radius:6px;box-shadow:0 3px 3px rgba(0,0,0,0.4),inset 0 1px 0 #fff;text-shadow:0 1px #fff;margin:0 -5px;padding:0 20px}.tab li.active{background:#fff;color:#333;z-index:2}.tab li:before{left:-6px;border-width:0 1px 1px 0;box-shadow:2px 2px 0 #d1d1d1}.tab li:after{right:-6px;border-width:0 0 1px 1px;box-shadow:-2px 2px 0 #d1d1d1}.tab a{color:#555;text-decoration:none}.tab:before{position:absolute;content:" ";width:100%;bottom:0;left:0;border-bottom:1px solid #aaa;z-index:1}.tabcontent{margin-top:-1px}
    </style>
    ...
    <body>
    ...


Then pass on `embed=True` to pyexcel signature functions. It is as simple as that.

CSS for readthedocs website
================================================================================

.. code-block:: html
   :linenos:
   :emphasize-lines: 3-7

    <html><head>
    ...
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.31.0/handsontable.full.min.js"></script>
    <style>
    body{font-family:Helvetica,sans-serif;margin:2 0 0 0}.tab{margin-bottom:0 !important;text-align:center;list-style:none;padding:0 0 0 10px;line-height:24px;height:26px;overflow:hidden;font-size:12px;font-family:verdana;position:relative;margin:0}.tab li{margin-left:0 !important;margin-top:2px !important;float:left;height:24px;border:1px solid #aaa;background:#d1d1d1;background:linear-gradient(top, #ececec 50%, #d1d1d1);display:inline-block;position:relative;z-index:0;border-top-left-radius:6px;border-top-right-radius:6px;box-shadow:0 3px 3px rgba(0,0,0,0.4),inset 0 1px 0 #fff;text-shadow:0 1px #fff;margin:0 -5px;padding:0 20px}.tab li.active{background:#fff;color:#333;z-index:2}.tab li:before{left:-6px;border-width:0 1px 1px 0;box-shadow:2px 2px 0 #d1d1d1}.tab li:after{right:-6px;border-width:0 0 1px 1px;box-shadow:-2px 2px 0 #d1d1d1}.tab a{color:#555;text-decoration:none}.tab:before{position:absolute;content:" ";width:100%;bottom:0;left:0;border-bottom:1px solid #aaa;z-index:1}.tabcontent{margin-top:-1px}
    </style>
    ...
    <body>
    ...


.. note::
   For latest handsontable releases, please visit `cdnjs <https://cdnjs.com/libraries/handsontable>`_

License
================================================================================

New BSD License
