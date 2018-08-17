pip freeze
nosetests --with-coverage --cover-package pyexcel_handsontable --cover-package tests tests  docs/source pyexcel_handsontable && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
