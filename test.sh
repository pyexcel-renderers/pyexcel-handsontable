

pip freeze
nosetests --with-cov --cover-package pyexcel_handsontable --cover-package tests --with-doctest --doctest-extension=.rst tests README.rst docs/source pyexcel_handsontable && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
