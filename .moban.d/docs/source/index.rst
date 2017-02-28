{%include "header.rst.jj2" %}

Introduction
--------------------------------------------------------------------------------

{%include "handsontable.rst.jj2"%}

{%include "constraints.rst.jj2"%}

Installation
--------------------------------------------------------------------------------

{%include "installation.rst.jj2" %}


Rendering Options
--------------------------------------------------------------------------------

You can pass the following options to :meth:`~pyexcel.Sheet.save_as` and
:meth:`~pyexcel.Book.save_as`. The same options are applicable to
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
    {%+ include "handsontable/style.css.jj2" %}
    </style>
    ...
    <body>
    ...


Then pass on `embed=True` to pyexcel signature functions. It is as simple as that.

.. note::
   For latest handsontable releases, please visit `cdnjs <https://cdnjs.com/libraries/handsontable>`_

{%include "license.rst.jj2" %}
