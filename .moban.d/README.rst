{% extends "BASIC-README.rst.jj2" %}

{%block constraint%}
{%endblock%}

{%block features %}
{%include "handsontable.rst.jj2" %}
{%endblock%}


{%block custom_guide %}

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

{%endblock%}
