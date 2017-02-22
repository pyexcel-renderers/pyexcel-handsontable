{%include "header.rst.jj2" %}

Introduction
--------------------------------------------------------------------------------

{%include "handsontable.rst.jj2"%}


Installation
--------------------------------------------------------------------------------

{%include "installation.rst.jj2" %}


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
    {%+ include "handsontable/style.css.jj2" %}
    </style>
    ...
    <body>
    ...


Then pass on `embed=True` to pyexcel signature functions. It is as simple as that.

.. note::
   For latest handsontable releases, please visit `cdnjs <https://cdnjs.com/libraries/handsontable>`_
